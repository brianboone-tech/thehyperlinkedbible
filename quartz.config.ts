import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "The Hyperlinked Bible",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "en-US",
    baseUrl: "quartz.jzhao.xyz",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Schibsted Grotesk",
        body: "Source Sans Pro",
        code: "IBM Plex Mono",
      },
      colors: {
        // Rosé Pine Dawn (Light) - matching AnuPpuccin rosepine-light
        lightMode: {
          light: "#faf4ed",        // Base
          lightgray: "#f2e9e1",    // Overlay
          gray: "#9893a5",         // Muted
          darkgray: "#575279",     // Text
          dark: "#286983",         // Pine
          secondary: "#1A7DA4",    // Custom teal accent
          tertiary: "#56949f",     // Foam
          highlight: "rgba(26, 125, 164, 0.12)",
          textHighlight: "#ea9d3488", // Gold
        },
        // Catppuccin Frappé (Dark) - matching AnuPpuccin ctp-frappe
        darkMode: {
          light: "#303446",        // Base
          lightgray: "#414559",    // Surface0
          gray: "#737994",         // Overlay0
          darkgray: "#c6d0f5",     // Text
          dark: "#f2d5cf",         // Rosewater
          secondary: "#11B7C5",    // Custom teal accent
          tertiary: "#81c8be",     // Teal
          highlight: "rgba(17, 183, 197, 0.12)",
          textHighlight: "#e5c89088", // Yellow
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
