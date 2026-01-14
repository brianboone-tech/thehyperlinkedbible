# Script to find broken internal links in markdown files

$contentPath = 'C:\Obsidian Vaults\thehyperlinkedbible\content'

# Get all markdown files
$allFiles = Get-ChildItem -Path $contentPath -Recurse -Filter '*.md'

# Build a lookup of all file paths (without extension, normalized)
$existingFiles = @{}
foreach ($file in $allFiles) {
    $relativePath = $file.FullName.Substring($contentPath.Length + 1) -replace '\\', '/'
    $pathWithoutExt = $relativePath -replace '\.md$', ''
    $existingFiles[$pathWithoutExt.ToLower()] = $true

    # Also add just the filename without path
    $filename = $file.BaseName
    $existingFiles[$filename.ToLower()] = $true
}

# Track broken links by folder
$brokenByFolder = @{}

foreach ($file in $allFiles) {
    $content = Get-Content $file.FullName -Raw
    $relativePath = $file.FullName.Substring($contentPath.Length + 1) -replace '\\', '/'
    $folder = Split-Path $relativePath -Parent
    if (-not $folder) { $folder = "(root)" }

    # Find all wiki links: [[path]] or [[path|display]]
    $matches = [regex]::Matches($content, '\[\[([^\]|#]+)')

    foreach ($match in $matches) {
        $linkTarget = $match.Groups[1].Value.Trim()

        # Skip external links and embeds that start with http
        if ($linkTarget -match '^https?://') { continue }

        # Normalize the link target
        $normalizedTarget = $linkTarget -replace '\\', '/'

        # Check if target exists
        $found = $false

        # Try exact match
        if ($existingFiles.ContainsKey($normalizedTarget.ToLower())) {
            $found = $true
        }

        # Try with .md extension removed if present
        $targetWithoutExt = $normalizedTarget -replace '\.md$', ''
        if ($existingFiles.ContainsKey($targetWithoutExt.ToLower())) {
            $found = $true
        }

        # Try just the filename
        $justFilename = Split-Path $normalizedTarget -Leaf
        if ($existingFiles.ContainsKey($justFilename.ToLower())) {
            $found = $true
        }

        if (-not $found) {
            if (-not $brokenByFolder.ContainsKey($folder)) {
                $brokenByFolder[$folder] = @()
            }
            $brokenByFolder[$folder] += [PSCustomObject]@{
                File = $relativePath
                BrokenLink = $linkTarget
            }
        }
    }
}

# Output results
Write-Host "=== BROKEN LINKS BY FOLDER ===" -ForegroundColor Red
Write-Host ""

$totalBroken = 0
foreach ($folder in ($brokenByFolder.Keys | Sort-Object)) {
    $links = $brokenByFolder[$folder]
    Write-Host "### $folder ($($links.Count) broken links)" -ForegroundColor Yellow

    # Group by unique broken link target
    $uniqueLinks = $links | Group-Object BrokenLink
    foreach ($group in ($uniqueLinks | Sort-Object Name)) {
        Write-Host "  - '$($group.Name)' (in $($group.Count) file(s))"
        $totalBroken += $group.Count
    }
    Write-Host ""
}

Write-Host "=== TOTAL: $totalBroken broken link references ===" -ForegroundColor Red
