#!/bin/bash
set -e

echo "Starting CI4"

docker-compose down --remove-orphans || true

echo "Building test image..."
docker-compose build tests

echo "Starting Selenoid..."
docker-compose up -d selenoid

echo "Waiting for Selenoid..."
for i in {1..30}; do
    if curl -s http://localhost:4444/wd/hub/status | grep -q "ready"; then
        echo "Selenoid is ready!"
        break
    fi
    echo "  Attempt $i/30..."
    sleep 5
done

echo "Available browsers:"
curl -s http://localhost:4444/wd/hub/status | python3 -m json.tool | grep -E '"browserName"|"version"' || true

BROWSERS=("chrome" "firefox" "MicrosoftEdge")
EXIT_CODE=0

for browser in "${BROWSERS[@]}"; do
    echo "Running tests with $browser..."

    pytest_browser="${browser}"
    if [ "$browser" == "MicrosoftEdge" ]; then
        pytest_browser="edge"
    fi

    docker-compose run --rm tests \
        pytest tests/ \
        --run-mode=grid \
        --browser=$pytest_browser \
        --grid-url=http://selenoid:4444/wd/hub \
        --alluredir=allure_results/selenoid \
        -n 3 \
        -v || EXIT_CODE=$?
done

echo "Generating Allure report..."
allure generate allure_results/selenoid -o allure-report-selenoid --clean

echo "Stopping containers..."
docker-compose down

if [ $EXIT_CODE -eq 0 ]; then
    echo "All tests passed!"
else
    echo "Tests failed with exit code: $EXIT_CODE"
fi

exit $EXIT_CODE