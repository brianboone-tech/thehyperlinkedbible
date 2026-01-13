import { computePosition, flip, inline, shift } from "@floating-ui/dom"
import { normalizeRelativeURLs } from "../../util/path"
import { fetchCanonical } from "./util"

const p = new DOMParser()
let activeAnchor: HTMLAnchorElement | null = null

async function mouseEnterHandler(
  this: HTMLAnchorElement,
  { clientX, clientY }: { clientX: number; clientY: number },
) {
  const link = (activeAnchor = this)
  if (link.dataset.noPopover === "true") {
    return
  }

  async function setPosition(popoverElement: HTMLElement) {
    const { x, y } = await computePosition(link, popoverElement, {
      strategy: "fixed",
      middleware: [inline({ x: clientX, y: clientY }), shift(), flip()],
    })
    Object.assign(popoverElement.style, {
      transform: `translate(${x.toFixed()}px, ${y.toFixed()}px)`,
    })
  }

  function showPopover(popoverElement: HTMLElement) {
    clearActivePopover()
    popoverElement.classList.add("active-popover")
    setPosition(popoverElement as HTMLElement)
    // No need to scroll - we now show only the linked section
  }

  const targetUrl = new URL(link.href)
  const hash = decodeURIComponent(targetUrl.hash)
  targetUrl.hash = ""
  targetUrl.search = ""
  const popoverId = `popover-${link.pathname}`
  const prevPopoverElement = document.getElementById(popoverId)

  // dont refetch if there's already a popover
  if (!!document.getElementById(popoverId)) {
    showPopover(prevPopoverElement as HTMLElement)
    return
  }

  const response = await fetchCanonical(targetUrl).catch((err) => {
    console.error(err)
  })

  if (!response) return
  const [contentType] = response.headers.get("Content-Type")!.split(";")
  const [contentTypeCategory, typeInfo] = contentType.split("/")

  const popoverElement = document.createElement("div")
  popoverElement.id = popoverId
  popoverElement.classList.add("popover")
  const popoverInner = document.createElement("div")
  popoverInner.classList.add("popover-inner")
  popoverInner.dataset.contentType = contentType ?? undefined
  popoverElement.appendChild(popoverInner)

  switch (contentTypeCategory) {
    case "image":
      const img = document.createElement("img")
      img.src = targetUrl.toString()
      img.alt = targetUrl.pathname

      popoverInner.appendChild(img)
      break
    case "application":
      switch (typeInfo) {
        case "pdf":
          const pdf = document.createElement("iframe")
          pdf.src = targetUrl.toString()
          popoverInner.appendChild(pdf)
          break
        default:
          break
      }
      break
    default:
      const contents = await response.text()
      const html = p.parseFromString(contents, "text/html")
      normalizeRelativeURLs(html, targetUrl)
      // prepend all IDs inside popovers to prevent duplicates
      html.querySelectorAll("[id]").forEach((el) => {
        const targetID = `popover-internal-${el.id}`
        el.id = targetID
      })
      const elts = [...html.getElementsByClassName("popover-hint")]
      if (elts.length === 0) return

      // If linking to a specific header, show only that section
      if (hash !== "") {
        const targetAnchor = `popover-internal-${hash.slice(1)}`
        let foundHeader: Element | null = null
        let headerLevel = 0

        // Find the target header in the content
        for (const elt of elts) {
          foundHeader = elt.querySelector(`#${CSS.escape(targetAnchor)}`)
          if (foundHeader) {
            // Determine header level (h1=1, h2=2, etc.)
            const tagName = foundHeader.tagName.toLowerCase()
            if (tagName.match(/^h[1-6]$/)) {
              headerLevel = parseInt(tagName.charAt(1))
            }
            break
          }
        }

        if (foundHeader && headerLevel > 0) {
          // Create a container for just this section
          const sectionContainer = document.createElement("div")
          sectionContainer.classList.add("popover-hint")

          // Clone the header
          sectionContainer.appendChild(foundHeader.cloneNode(true))

          // Collect content until next header of same or higher level
          let sibling = foundHeader.nextElementSibling
          while (sibling) {
            const siblingTag = sibling.tagName.toLowerCase()
            // Stop if we hit another header of same or higher level
            if (siblingTag.match(/^h[1-6]$/)) {
              const siblingLevel = parseInt(siblingTag.charAt(1))
              if (siblingLevel <= headerLevel) {
                break
              }
            }
            sectionContainer.appendChild(sibling.cloneNode(true))
            sibling = sibling.nextElementSibling
          }

          popoverInner.appendChild(sectionContainer)
        } else {
          // Fallback: show all content if header not found
          elts.forEach((elt) => popoverInner.appendChild(elt))
        }
      } else {
        // No hash - show full page content
        elts.forEach((elt) => popoverInner.appendChild(elt))
      }
  }

  if (!!document.getElementById(popoverId)) {
    return
  }

  document.body.appendChild(popoverElement)
  if (activeAnchor !== this) {
    return
  }

  // Attach popover listeners to links inside the popover (enables nested popovers)
  const popoverLinks = popoverElement.querySelectorAll("a.internal") as NodeListOf<HTMLAnchorElement>
  for (const popoverLink of popoverLinks) {
    popoverLink.addEventListener("mouseenter", mouseEnterHandler)
    popoverLink.addEventListener("mouseleave", clearActivePopover)
  }

  showPopover(popoverElement)
}

function clearActivePopover() {
  activeAnchor = null
  const allPopoverElements = document.querySelectorAll(".popover")
  allPopoverElements.forEach((popoverElement) => popoverElement.classList.remove("active-popover"))
}

document.addEventListener("nav", () => {
  const links = [...document.querySelectorAll("a.internal")] as HTMLAnchorElement[]
  for (const link of links) {
    link.addEventListener("mouseenter", mouseEnterHandler)
    link.addEventListener("mouseleave", clearActivePopover)
    window.addCleanup(() => {
      link.removeEventListener("mouseenter", mouseEnterHandler)
      link.removeEventListener("mouseleave", clearActivePopover)
    })
  }
})
