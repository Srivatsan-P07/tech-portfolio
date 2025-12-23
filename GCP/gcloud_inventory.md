# Cloud Asset Inventory API

### Prerequisites

1. **Enable the API:** Go to the [Cloud Asset API page](https://www.google.com/search?q=https://console.cloud.google.com/apis/library/cloudasset.googleapis.com) and click **Enable**.
2. **Authentication:** Ensure you are logged in via the gcloud CLI:
```bash
gcloud auth application-default login
```


3. **Install the Library:**
```bash
pip install google-cloud-asset
```

---

### The Python Script

This script will list all resources in your project. I've designed it to specifically look for the common "billable" types you mentioned like VMs, Buckets, and Databases.

```python
from google.cloud import asset_v1

def list_active_resources(project_id):
    client = asset_v1.AssetServiceClient()
    
    # Define the scope (your project)
    scope = f"projects/{project_id}"
    
    # We leave query empty to find "everything", 
    # but you can filter if you have thousands of items.
    query = "" 

    # Fetching all resource types
    # Note: This includes disks, networks, addresses, etc.
    try:
        response = client.search_all_resources(
            request={
                "scope": scope,
                "query": query,
            }
        )

        print(f"{'TYPE':<40} | {'NAME':<30}")
        print("-" * 75)

        found_any = False
        for resource in response:
            found_any = True
            # Shorten the type name for readability
            short_type = resource.asset_type.split('/')[-1]
            print(f"{short_type:<40} | {resource.display_name:<30}")
            
        if not found_any:
            print("No active resources found.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # REPLACE with your actual Project ID
    MY_PROJECT_ID = "your-project-id-here"
    list_active_resources(MY_PROJECT_ID)

```

---

### What this will catch:

When you run this, keep an eye out for these specific `asset_type` labels in the output:

* **Compute Engine:** `Instance`, `Disk`, `Address` (Static IPs cost money even if not attached!).
* **Cloud Storage:** `Bucket`.
* **BigQuery:** `Dataset`, `Table`.
* **Firestore/Datastore:** `Index`, `Database`.
* **Cloud SQL:** `Instance`.

### Important Tips for "Cleaning Up"

1. **Check Static IPs:** Often, people delete a VM but forget the **Static IP address**. These are charged at a higher rate when *unattached*. Look for `compute.googleapis.com/Address` in your results.
2. **Check Disks:** Deleting a VM doesn't always delete the **Boot Disk**. Look for `compute.googleapis.com/Disk`.
3. **Cloud Storage Versions:** If you have "Object Versioning" on a bucket, even if you delete a file, old versions might still be taking up space and costing money.

### Alternative: The "Quick View" Command

If you don't want to run a full Python script, you can run this one-liner in your terminal to get a quick summary of what's running:

```bash
gcloud asset search-all-resources --scope=projects/YOUR_PROJECT_ID --format="table(assetType, displayName, location)"
```