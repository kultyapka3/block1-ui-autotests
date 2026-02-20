@echo off
setlocal

curl -s http://26.188.133.184:4444/status | findstr "message" >nul
if %errorlevel% neq 0 (
    echo Selenium Grid is not enabled. Please start selenium_grid.bat.
    exit /b 1
)

mkdir allure_results\grid 2>nul

echo Starting U1 tests (Node 1)...
start "U1 Tests" cmd /c "pytest -m U1 --run-mode=grid --grid-url=http://26.188.133.184:4444 --alluredir=./allure_results/grid -n 5 && exit"

echo Starting U3 tests (Node 2)...
start "U3 Tests" cmd /c "pytest -m U3 --run-mode=grid --grid-url=http://26.188.133.184:4444 --alluredir=./allure_results/grid && exit"

echo Starting U4 tests (Node 3)...
start "U4 Tests" cmd /c "pytest -m U4 --run-mode=grid --grid-url=http://26.188.133.184:4444 --alluredir=./allure_results/grid -n 2 && exit"

echo Starting U5 tests (Node 4)...
start "U5 Tests" cmd /c "pytest -m U5 --run-mode=grid --grid-url=http://26.188.133.184:4444 --alluredir=./allure_results/grid && exit"

echo Starting U6 tests (Node 5)...
start "U6 Tests" cmd /c "pytest -m U6 --run-mode=grid --grid-url=http://26.188.133.184:4444 --alluredir=./allure_results/grid && exit"

echo The tests are running in parallel mode.
echo To view the report after completing the tests, run:
echo   allure serve allure_results/grid
