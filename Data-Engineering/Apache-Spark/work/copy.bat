@echo off
setlocal

REM Define paths
set "WORK_DIR=C:\Users\parthasarathys\Desktop\Srivatsan_Parthasarathy\0.Work_Related_Files\GitHub_Repositories\tech-portfolio\Data-Engineering\Apache-Spark\work"
set "DOWNLOADS_DIR=%USERPROFILE%\Downloads"

echo Deleting contents of WORK directory...
if exist "%WORK_DIR%" (
    del /f /s /q "%WORK_DIR%\*"
    for /d %%x in ("%WORK_DIR%\*") do rd /s /q "%%x"
) else (
    echo WORK directory does not exist.
    goto :end
)

echo Copying files from Downloads to WORK directory...
xcopy "%DOWNLOADS_DIR%\*" "%WORK_DIR%\" /e /h /c /i /y

echo Done!

:end
pause