$ErrorActionPreference = "Stop"

Write-Host "Starting CI4: Docker + Selenoid + Tests" -ForegroundColor Cyan

$workspace = $env:WORKSPACE
if ($workspace) {
    Set-Location $workspace
    Write-Host "  Working directory: $workspace"
}

Write-Host "Cleaning up old containers..."
docker compose down --remove-orphans 2>$null | Out-Null

Write-Host "Building test image..."
docker compose build tests
if ($LASTEXITCODE -ne 0) {
    Write-Host "Failed to build image!" -ForegroundColor Red
    exit 1
}

Write-Host "Starting Selenoid..."
docker compose up -d selenoid

Write-Host "Waiting for Selenoid..."
for ($i = 1; $i -le 30; $i++) {
    try {
        $status = curl -UseBasicParsing -Uri "http://localhost:4444/wd/hub/status" -TimeoutSec 5
        if ($status.Content -match '"ready":true') {
            Write-Host "Selenoid is ready!" -ForegroundColor Green
            break
        }
    } catch {

    }
    Write-Host "  Attempt $i/30..."
    Start-Sleep -Seconds 5
}

Write-Host "Available browsers:"
try {
    $browsers = curl -UseBasicParsing -Uri "http://localhost:4444/wd/hub/status" -TimeoutSec 5
    $browsers.Content | ConvertFrom-Json | Select-Object -ExpandProperty value -ErrorAction SilentlyContinue
} catch {
    Write-Host "  (Could not fetch browser list)"
}

$BROWSERS = @("chrome", "firefox", "MicrosoftEdge")
$EXIT_CODE = 0

foreach ($browser in $BROWSERS) {
    Write-Host "Running tests with $browser..." -ForegroundColor Yellow

    $pytest_browser = $browser
    if ($browser -eq "MicrosoftEdge") {
        $pytest_browser = "edge"
    }

    docker compose run --rm tests `
        pytest tests/ `
        --run-mode=grid `
        --browser=$pytest_browser `
        --grid-url=http://selenoid:4444/wd/hub `
        --alluredir=allure_results/selenoid `
        -n 3 `
        -v

    if ($LASTEXITCODE -ne 0) {
        Write-Host "  Tests failed for $browser" -ForegroundColor Red
        $EXIT_CODE = $LASTEXITCODE
    } else {
        Write-Host "  Tests passed for $browser" -ForegroundColor Green
    }
}

Write-Host "Generating Allure report..."
allure generate allure_results/selenoid -o allure-report-selenoid --clean
if ($LASTEXITCODE -ne 0) {
    Write-Host "Warning: Allure report generation failed" -ForegroundColor Yellow
}

Write-Host "Stopping containers..."
docker compose down

if ($EXIT_CODE -eq 0) {
    Write-Host "All tests passed!" -ForegroundColor Green
} else {
    Write-Host "Tests failed with exit code: $EXIT_CODE" -ForegroundColor Red
}

exit $EXIT_CODE