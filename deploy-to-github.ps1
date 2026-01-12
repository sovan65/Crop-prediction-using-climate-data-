# Quick GitHub Deployment Script
# Run this after creating your GitHub repository

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  GitHub Deployment for Crop System  " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Get GitHub username and repository name
$username = Read-Host "Enter your GitHub username"
$repoName = Read-Host "Enter repository name (default: crop-recommendation-system)"

if ([string]::IsNullOrWhiteSpace($repoName)) {
    $repoName = "crop-recommendation-system"
}

$repoUrl = "https://github.com/$username/$repoName.git"

Write-Host ""
Write-Host "Repository URL: $repoUrl" -ForegroundColor Yellow
Write-Host ""

# Confirm
$confirm = Read-Host "Continue with deployment? (Y/N)"
if ($confirm -ne 'Y' -and $confirm -ne 'y') {
    Write-Host "Deployment cancelled." -ForegroundColor Red
    exit
}

Write-Host ""
Write-Host "Step 1: Checking Git status..." -ForegroundColor Green
git status --short

Write-Host ""
Write-Host "Step 2: Adding remote origin..." -ForegroundColor Green
git remote remove origin 2>$null
git remote add origin $repoUrl

if ($LASTEXITCODE -eq 0) {
    Write-Host "[OK] Remote added successfully" -ForegroundColor Green
} else {
    Write-Host "[ERROR] Failed to add remote" -ForegroundColor Red
    exit
}

Write-Host ""
Write-Host "Step 3: Renaming branch to 'main'..." -ForegroundColor Green
git branch -M main

Write-Host ""
Write-Host "Step 4: Pushing to GitHub..." -ForegroundColor Green
Write-Host "(You may be prompted for authentication)" -ForegroundColor Yellow
Write-Host ""

git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "  DEPLOYMENT SUCCESSFUL!  " -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Your repository is now live at:" -ForegroundColor Cyan
    Write-Host "https://github.com/$username/$repoName" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Next steps:" -ForegroundColor Cyan
    Write-Host "1. Visit your repository on GitHub" -ForegroundColor White
    Write-Host "2. Add topics/tags for better discoverability" -ForegroundColor White
    Write-Host "3. Create a release (v1.0.0)" -ForegroundColor White
    Write-Host "4. Share your project!" -ForegroundColor White
    Write-Host ""
    
    # Ask if user wants to open repository in browser
    $openBrowser = Read-Host "Open repository in browser? (Y/N)"
    if ($openBrowser -eq 'Y' -or $openBrowser -eq 'y') {
        Start-Process "https://github.com/$username/$repoName"
    }
} else {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Red
    Write-Host "  DEPLOYMENT FAILED  " -ForegroundColor Red
    Write-Host "========================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "Common issues:" -ForegroundColor Yellow
    Write-Host "1. Repository doesn't exist on GitHub - Create it first!" -ForegroundColor White
    Write-Host "2. Authentication failed - Set up GitHub credentials" -ForegroundColor White
    Write-Host "3. Repository not empty - Make sure it's a new empty repo" -ForegroundColor White
    Write-Host ""
    Write-Host "See GITHUB_DEPLOYMENT.md for detailed troubleshooting" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
