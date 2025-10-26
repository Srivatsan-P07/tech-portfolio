# For BASH
```bash
#!/bin/bash

# --- Configuration Variables ---
TEMPLATE_NAME="gce-jenkins-template"
INSTANCE_NAME="gce-jenkins"
DISK_NAME="gce-jenkins"
INSTANCE_ZONE="asia-south1-b"
STORAGE_LOCATION="asia-south1" # Single Region

# Get Disk ID dynamically
DISK_ID = $(gcloud compute disks describe "$DISK_NAME" --zone "$INSTANCE_ZONE" --format="value(id)")

#################################################################################################################################################################################
# 1. Create Template from running instance
echo "Creating instance template: $TEMPLATE_NAME from $INSTANCE_NAME..."

gcloud compute instance-templates create "$TEMPLATE_NAME" \
    --source-instance="$INSTANCE_NAME" \
    --source-instance-zone="$INSTANCE_ZONE"

echo "Template creation complete."
echo "----------------------------------------"



#################################################################################################################################################################################
# --- 2. Take Snapshot of Disk ---
echo "Taking snapshot of disk: $DISK_NAME..."

gcloud compute disks snapshot "$DISK_NAME" \
    --snapshot-names="jenkins-backup-$(date +%Y%m%d%H%M)" \
    --zone="$INSTANCE_ZONE" \
    --storage-location="$STORAGE_LOCATION"

echo "----------------------------------------"



#################################################################################################################################################################################
# 3. Get the name (URI) of the most recent snapshot for the disk
echo "Retrieving the URI of the latest snapshot for disk ID: $DISK_ID..."

LATEST_SNAPSHOT=$(gcloud compute snapshots list \
    --filter="sourceDiskId=($DISK_ID)" \
    --sort-by="creationTimestamp" \
    --limit=1 \
    --uri)

if [ -z "$LATEST_SNAPSHOT" ]; then
    echo "ERROR: Could not find a snapshot for disk ID: $DISK_ID. Exiting."
    exit 1
fi

echo "Latest Snapshot URI: $LATEST_SNAPSHOT"
echo "----------------------------------------"



#################################################################################################################################################################################
# 4. Delete Old Instance & Disk
gcloud compute instances stop $INSTANCE_NAME --zone=$INSTANCE_ZONE
gcloud compute instances delete $INSTANCE_NAME --zone=$INSTANCE_ZONE
gcloud compute disks delete $DISK_NAME --zone=$INSTANCE[INSTANCE_ZONE]



#################################################################################################################################################################################
# 5. Create a New Disk from the Snapshot
echo "Creating new disk: $DISK_NAME from snapshot: $LATEST_SNAPSHOT..."

gcloud compute disks create "$DISK_NAME" \
    --source-snapshot="$LATEST_SNAPSHOT" \
    --zone="$INSTANCE_ZONE"

echo "New disk creation complete."
echo "----------------------------------------"



#################################################################################################################################################################################
# 6. Create new instance with new disk
echo "Creating new instance: $INSTANCE_NAME using template: $TEMPLATE_NAME and new disk: $DISK_NAME..."

gcloud compute instances create "$INSTANCE_NAME" \
    --source-instance-template="$TEMPLATE_NAME" \
    --zone="$INSTANCE_ZONE" \
    --disk="name=$NEW_DISK_NAME,device-name=boot,mode=rw,boot=yes"

echo "Restoration process complete. New instance: $INSTANCE_NAME is being started in $INSTANCE_ZONE."
```

# For Windows

```bat
@echo off
setlocal

:: --- Configuration Variables ---
set TEMPLATE_NAME="gce-jenkins-template"
set INSTANCE_NAME="gce-jenkins"
set DISK_NAME="gce-jenkins"
set INSTANCE_ZONE="asia-south1-b"
set STORAGE_LOCATION="asia-south1" :: Single Region

:: Get Disk ID dynamically
echo Retrieving Disk ID for: %DISK_NAME% in zone: %INSTANCE_ZONE%...
FOR /F "tokens=*" %%a IN ('gcloud compute disks describe %DISK_NAME% --zone %INSTANCE_ZONE% --format="value(id)"') DO (
    set DISK_ID=%%a
)

IF NOT DEFINED DISK_ID (
    echo ERROR: Could not retrieve Disk ID. Exiting.
    exit /b 1
)
echo Disk ID: %DISK_ID%
echo ----------------------------------------



:: ################################################################################################################################################################################
:: 1. Create Template from running instance
echo Creating instance template: %TEMPLATE_NAME% from %INSTANCE_NAME%...

gcloud compute instance-templates create %TEMPLATE_NAME% ^
    --source-instance=%INSTANCE_NAME% ^
    --source-instance-zone=%INSTANCE_ZONE%
echo Template creation complete.
echo ----------------------------------------



:: ##################################################################################################################################################################################
:: --- 2. Take Snapshot of Disk ---
echo Taking snapshot of disk: %DISK_NAME%...

:: Create a timestamp for the snapshot name (YYYYMMDDHHMM)
FOR /F "tokens=1-4 delims=/ " %%i in ('date /t') do (set DATETOKEN=%%k%%j%%i)
FOR /F "tokens=1-2 delims=: " %%i in ('time /t') do (set TIMETOKEN=%%i%%j)
set SNAPSHOT_NAME_TS=jenkins-backup-%DATETOKEN%%TIMETOKEN%

gcloud compute disks snapshot %DISK_NAME% ^
    --snapshot-names=%SNAPSHOT_NAME_TS% ^
    --zone=%INSTANCE_ZONE% ^
    --storage-location=%STORAGE_LOCATION%
echo Snapshot taken: %SNAPSHOT_NAME_TS%
echo ----------------------------------------



:: ##################################################################################################################################################################################
:: 3. Get the name (URI) of the most recent snapshot for the disk
echo Retrieving the URI of the latest snapshot for disk ID: %DISK_ID%...

set LATEST_SNAPSHOT=
:: Using FOR /F to capture the output of the gcloud command
FOR /F "tokens=*" %%s IN ('gcloud compute snapshots list --filter="sourceDiskId=(%DISK_ID%)" --sort-by="creationTimestamp" --limit=1 --uri') DO (
    set LATEST_SNAPSHOT=%%s
)

IF NOT DEFINED LATEST_SNAPSHOT (
    echo ERROR: Could not find a snapshot for disk ID: %DISK_ID%. Exiting.
    exit /b 1
)
echo Latest Snapshot URI: %LATEST_SNAPSHOT%
echo ----------------------------------------



:: ##################################################################################################################################################################################
:: 4. Delete Old Instance & Disk
echo Stopping and deleting old instance and disk...
gcloud compute instances stop %INSTANCE_NAME% --zone=%INSTANCE_ZONE% --quiet
gcloud compute instances delete %INSTANCE_NAME% --zone=%INSTANCE_ZONE% --quiet
gcloud compute disks delete %DISK_NAME% --zone=%INSTANCE_ZONE% --quiet
echo Old instance and disk deleted.
echo ----------------------------------------



:: ##################################################################################################################################################################################
:: 5. Create a New Disk from the Snapshot
echo Creating new disk: %DISK_NAME% from snapshot: %LATEST_SNAPSHOT%...

gcloud compute disks create %DISK_NAME% ^
    --source-snapshot=%LATEST_SNAPSHOT% ^
    --zone=%INSTANCE_ZONE%
echo New disk creation complete.
echo ----------------------------------------



:: ##################################################################################################################################################################################
:: 6. Create new instance with new disk
echo Creating new instance: %INSTANCE_NAME% using template: %TEMPLATE_NAME% and new disk: %DISK_NAME%...

:: NOTE: The original
```