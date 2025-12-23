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
    GCP_NOISE_TYPES = [
        "serviceusage.googleapis.com/Service",         # Indicates an API is enabled
        "compute.googleapis.com/Route",               # Default networking paths
        "compute.googleapis.com/Subnetwork",          # Regional networking containers
        "compute.googleapis.com/Network",             # The VPC itself
        "compute.googleapis.com/Firewall",            # Security rule configurations
        "compute.googleapis.com/InstanceSettings",    # VM Metadata/Configs
        #"iam.googleapis.com/ServiceAccount",          # Identity principals
        #"iam.googleapis.com/ServiceAccountKey",       # Identity keys
        "logging.googleapis.com/LogSink",             # Logging routes
        #"logging.googleapis.com/LogBucket",           # Standard log storage (first 50GB free)
        #"firebaserules.googleapis.com/Ruleset",       # Firestore/Firebase config rules
        #"firebaserules.googleapis.com/Release",       # Versioning for Firebase rules
        #"cloudbilling.googleapis.com/ProjectBillingInfo", # Your billing association
        #"cloudresourcemanager.googleapis.com/Project"  # The project container itself
    ]
    
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
            short_type = resource.asset_type
            if short_type in GCP_NOISE_TYPES:
                continue  # Skip noisy types
            print(f"{short_type:<40} | {resource.display_name:<30}")
            
        if not found_any:
            print("No active resources found.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check resources in the specified project
    list_active_resources("hawx-brahmin-db")
    print("\n" + "="*80 + "\n")
    list_active_resources("srivatsan-paid-learning")