$scriptureFiles = Get-ChildItem -Path "C:\Obsidian Vaults\thehyperlinkedbible\content\Home\Scripture" -Filter "*.md" -File | Where-Object { $_.Name -match "^\d{2} - " }

$fixedCount = 0

foreach ($file in $scriptureFiles) {
    $content = Get-Content $file.FullName -Raw
    
    # Remove the TOSK row from the Browse All Resources table
    $pattern = '\| 📖 \*\*TOSK References\*\* \| [^|]+ \| \[\[Home/Scripture/TOSK/[^\]]+\|View all →\]\] \|\r?\n'
    
    if ($content -match $pattern) {
        $newContent = $content -replace $pattern, ''
        Set-Content -Path $file.FullName -Value $newContent -NoNewline
        Write-Host "Fixed: $($file.Name)"
        $fixedCount++
    }
}

Write-Host "`nTotal files fixed: $fixedCount"
