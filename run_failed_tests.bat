@echo off
setlocal

if not exist "allure_results" (
    echo No previous run results were found. Run the tests first.
    exit /b 1
)

echo Running only dropped tests.
pytest --last-failed --alluredir=./allure_results/failed_tests %*

echo To generate a report for failed tests, run:
echo   allure serve allure_results/failed_tests
