@echo off
setlocal enabledelayedexpansion

:: Set your GCP Project ID here
set GCP_PROJECT_ID=hawx-one

:: Check if a project ID is set
if "%GCP_PROJECT_ID%"=="" (
    echo ERROR: GCP_PROJECT_ID is not set. Please edit this batch file and set it.
    pause
    exit /b 1
)

echo Setting gcloud project to %GCP_PROJECT_ID%...
call gcloud config set project %GCP_PROJECT_ID%

if %errorlevel% neq 0 (
    echo ERROR: Failed to set gcloud project. Make sure you are authenticated and the project ID is correct.
    pause
    exit /b 1
)

echo.
echo Listing all enabled services for project %GCP_PROJECT_ID%...
echo This might take a moment.
echo.

:: Get the list of enabled services
for /f "tokens=*" %%a in ('gcloud services list --enabled --format="value(config.name)" ^| findstr /v /b "ERROR"') do (
    set "SERVICE_TO_DISABLE=%%a"
    echo Disabling !SERVICE_TO_DISABLE!...
    call gcloud services disable "!SERVICE_TO_DISABLE!" --force --quiet

    if !errorlevel! neq 0 (
        echo WARNING: Failed to disable !SERVICE_TO_DISABLE!. It might already be disabled or there's an issue.
    )
    echo.
)

echo.
echo All enabled GCP APIs have been processed.
echo Please review the output for any warnings or errors.
echo.
pause
endlocal
