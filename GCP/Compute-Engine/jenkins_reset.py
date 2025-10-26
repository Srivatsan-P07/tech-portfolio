import subprocess
import sys
from datetime import datetime
import json

# --- Configuration Variables ---
TEMPLATE_NAME = "gce-jenkins-template"
INSTANCE_NAME = "gce-jenkins"
DISK_NAME = "gce-jenkins"
INSTANCE_ZONE = "asia-south1-b"
STORAGE_LOCATION = "asia-south1" # Single Region

def execute_gcloud_command(cmd, failure_message, ignore_error=False, format_type='none'):
    """Executes a gcloud command and returns the output or handles errors."""
    try:
        if format_type == 'value':
            # Use check_output for commands where we expect a single value output
            result = subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.DEVNULL).strip()
            return result
        elif format_type == 'uri':
            # Use check_output for commands where we expect a URI
            result = subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.DEVNULL).strip()
            return result
        else:
            # Use run for commands that just execute an action
            process = subprocess.run(cmd, shell=True, check=True, text=True, capture_output=True)
            return process.stdout
    
    # Error Handling
    except subprocess.CalledProcessError as e:
        if ignore_error:
            print(f"  Warning: Command failed as expected (e.g., resource not found). Continuing.")
            return None
        else:
            print(f"\nFATAL ERROR: {failure_message}")
            print(f"Command: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
            print(f"Error Output:\n{e.stderr}")
            sys.exit(1)
    except FileNotFoundError:
        print("\nFATAL ERROR: 'gcloud' command not found. Ensure Google Cloud CLI is installed and in your PATH.")
        sys.exit(1)

print("Starting GCE Jenkins Instance and Disk Restoration Script (Python)")
print("----------------------------------------------------------------")

# --- Get Disk ID dynamically ---
print("=== 0. Retrieving Disk ID ===")
print(f"Retrieving Disk ID for: {DISK_NAME} in zone: {INSTANCE_ZONE}...")

# Command to get ID: gcloud compute disks describe DISK_NAME --zone ZONE --format="value(id)"
cmd_disk_id = f'gcloud compute disks describe {DISK_NAME} --zone {INSTANCE_ZONE} --format="value(id)"'
DISK_ID = execute_gcloud_command(cmd_disk_id, f"Could not retrieve Disk ID for {DISK_NAME}. Check if the disk exists.", format_type='value')

if not DISK_ID:
    print("ERROR: Disk ID is empty. Exiting.")
    sys.exit(1)

print(f"Disk ID retrieved: {DISK_ID}")
print("----------------------------------------")

# --- Pre-Step: Delete existing template if it exists ---
print("\n=== Pre-Step: Deleting Old Template (if present) ===")
print(f"Attempting to delete existing template: {TEMPLATE_NAME}...")

# Use ignore_error=True as failure is expected if the template doesn't exist
cmd_delete_template = f'gcloud compute instance-templates delete {TEMPLATE_NAME} --quiet'
execute_gcloud_command(cmd_delete_template, "Template deletion command failed.", ignore_error=True)

print("Template cleanup complete.")
print("----------------------------------------")


# --- 1. Create Template from running instance ---
print("\n=== 1. Creating Template ===")
print(f"Creating instance template: {TEMPLATE_NAME} from {INSTANCE_NAME}...")

cmd_create_template = (
    f'gcloud compute instance-templates create {TEMPLATE_NAME} '
    f'--source-instance={INSTANCE_NAME} '
    f'--source-instance-zone={INSTANCE_ZONE}'
)
execute_gcloud_command(cmd_create_template, f"Template creation failed for {TEMPLATE_NAME}.")

print("Template creation complete.")
print("----------------------------------------")


# --- 2. Take Snapshot of Disk ---
print("\n=== 2. Taking Disk Snapshot ===")
print(f"Taking snapshot of disk: {DISK_NAME}")
print(f"This may take a few minutes...")

SNAPSHOT_NAME = f"jenkins-backup-{datetime.now().strftime('%Y%m%d%H%M')}"
cmd_snapshot = (
    f'gcloud compute disks snapshot {DISK_NAME} '
    f'--snapshot-names={SNAPSHOT_NAME} '
    f'--zone={INSTANCE_ZONE} '
    f'--storage-location={STORAGE_LOCATION}'
)
execute_gcloud_command(cmd_snapshot, f"Snapshot creation failed for disk {DISK_NAME}.")

print(f"Snapshot taken: {SNAPSHOT_NAME}")
print("----------------------------------------")


# --- 3. Get the name (URI) of the most recent snapshot for the disk ---
print("\n=== 3. Retrieving Latest Snapshot URI ===")
print(f"Retrieving the URI of the latest snapshot for disk ID: {DISK_ID}...")

cmd_latest_snapshot = (
    f'gcloud compute snapshots list '
    f'--filter="sourceDiskId=({DISK_ID})" '
    f'--sort-by="creationTimestamp" '
    f'--limit=1 '
    f'--uri'
)
LATEST_SNAPSHOT = execute_gcloud_command(cmd_latest_snapshot, f"Could not find a snapshot for disk ID: {DISK_ID}.", format_type='uri')

if not LATEST_SNAPSHOT:
    print("ERROR: Could not retrieve latest snapshot URI. Exiting.")
    sys.exit(1)

print(f"Latest Snapshot URI: {LATEST_SNAPSHOT}")
print("----------------------------------------")


# --- 4. Delete Old Instance & Disk ---
print("\n=== 4. Deleting Old Instance and Disk ===")

print(f"Stopping instance {INSTANCE_NAME}...")
cmd_stop = f'gcloud compute instances stop {INSTANCE_NAME} --zone={INSTANCE_ZONE} --quiet'
execute_gcloud_command(cmd_stop, f"Failed to stop instance {INSTANCE_NAME}.")

print(f"Deleting instance {INSTANCE_NAME}...")
cmd_delete_instance = f'gcloud compute instances delete {INSTANCE_NAME} --zone={INSTANCE_ZONE} --quiet'
execute_gcloud_command(cmd_delete_instance, f"Failed to delete instance {INSTANCE_NAME}.")

print(f"Deleting disk {DISK_NAME}...")
cmd_delete_disk = f'gcloud compute disks delete {DISK_NAME} --zone={INSTANCE_ZONE} --quiet'
execute_gcloud_command(cmd_delete_disk, f"Failed to delete disk {DISK_NAME}.", ignore_error=True)

print("Old instance and disk deleted.")
print("----------------------------------------")


# --- 5. Create a New Disk from the Snapshot ---
print("\n=== 5. Creating New Disk from Snapshot ===")
print(f"Creating new disk: {DISK_NAME} from snapshot: {LATEST_SNAPSHOT}...")

cmd_create_disk = (
    f'gcloud compute disks create {DISK_NAME} '
    f'--source-snapshot={LATEST_SNAPSHOT} '
    f'--zone={INSTANCE_ZONE}'
)
execute_gcloud_command(cmd_create_disk, f"New disk creation failed for {DISK_NAME}.")

print("New disk creation complete.")
print("----------------------------------------")


# --- 6. Create new instance with new disk ---
print("\n=== 6. Creating New Instance ===")
print(f"Creating new instance: {INSTANCE_NAME} using template: {TEMPLATE_NAME} and new disk: {DISK_NAME}...")

# Note: Using DISK_NAME, which is correct for the newly created disk.
cmd_create_instance = (
    f'gcloud compute instances create {INSTANCE_NAME} '
    f'--source-instance-template={TEMPLATE_NAME} '
    f'--zone={INSTANCE_ZONE} '
    f'--disk="name={DISK_NAME},device-name=boot,mode=rw,boot=yes"'
)
execute_gcloud_command(cmd_create_instance, f"New instance creation failed for {INSTANCE_NAME}.")

print(f"\nRestoration process complete. New instance: {INSTANCE_NAME} is being started in {INSTANCE_ZONE}.")
print("----------------------------------------")