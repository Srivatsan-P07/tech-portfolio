@echo off

echo.
echo ==================================================
echo        FULL DOCKER RESET STARTING 
echo ==================================================
echo.

:: Stop all running containers
echo [1/6] Stopping all running containers...
for /f %%i in ('docker ps -q') do docker stop %%i >nul 2>&1
echo Done.
echo.

:: Remove all containers
echo [2/6]  Removing all containers...
for /f %%i in ('docker ps -aq') do docker rm -f %%i >nul 2>&1
echo Done.
echo.

:: Remove all images
echo [3/6]  Removing all Docker images...
:: for /f %%i in ('docker images -q') do docker rmi -f %%i >nul 2>&1
echo Done.
echo.

:: Remove all volumes
echo [4/6]  Removing all Docker volumes...
for /f %%i in ('docker volume ls -q') do docker volume rm %%i >nul 2>&1
echo Done.
echo.

:: Remove all networks (except default ones)
echo [5/6]  Removing all user-defined Docker networks...
for /f %%i in ('docker network ls -q ^| findstr /v "bridge host none"') do docker network rm %%i >nul 2>&1
echo Done.
echo.

:: Remove builder cache
echo [6/6]  Removing Docker builder cache...
docker builder prune -a -f >nul 2>&1
echo Done.
echo.

echo ==================================================
echo        DOCKER RESET COMPLETE 
echo ==================================================
echo.

pause