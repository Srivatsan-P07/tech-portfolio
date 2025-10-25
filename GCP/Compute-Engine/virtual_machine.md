# GCP Compute Engine Details

## Basic Information

| Name | Value | Meaning |
| :--- | :--- | :--- |
| **Name** | gce-jenkins | The user-defined name for the instance. |
| **Instance Id** | 8898559056480179261 | A unique, system-generated identifier for this instance. |
| **Description** | None | An optional, user-provided text description of the instance. |
| **Type** | Instance | The general resource type; in this case, a virtual machine **instance**. |
| **Status** | **Stopped** | The current operational state of the instance.<br>**Stopped** means the virtual machine is powered off and not consuming CPU/RAM resources<br>(storage still incurs cost). |
| **Creation time** | Oct 24, 2025, 10:05:34 PM UTC+05:30 | The date and time when the instance was created. |
| **Location** | **asia-south1-b** | The **zone** where the instance is hosted, determining its physical location and network latency. |
| **Boot disk source image** | debian-12-bookworm-v20251014 | The **operating system image** used to create the instance's boot disk (the disk containing the OS). |
| **Boot disk architecture** | X86\_64 | The **processor architecture** of the boot disk and the virtual machine, which is the standard 64-bit architecture. |
| **Boot disk license type** | Free | Indicates the licensing model for the operating system on the boot disk. |
| **Instance template** | None | A reference to an optional resource used to define the configuration when the instance was created. |
| **In use by** | None | Shows if the instance is currently managed or utilized by another service (e.g., an Instance Group). |
| **Physical host** | None | Typically relevant for sole-tenant nodes; indicates the dedicated physical server the VM runs on. |
| **Maintenance status** | — | Indicates the instance's readiness or current state during platform maintenance events. |
| **Reservations** | Don't use | Specifies whether this instance should consume an existing compute reservation. |
| **Labels** | None | **Key-value pairs** used for organizing, searching, and managing resources (e.g., for billing or automation). |
| **Tags** | — | **Network tags** used to apply firewall rules or route traffic to and from the instance. |
| **Deletion protection** | Disabled | This feature, when **Enabled**, prevents the VM instance from being accidentally or maliciously **deleted**.<br>Since it is **Disabled**, the instance can be terminated by anyone with the necessary permissions. |
| **Confidential VM service** | Disabled | This indicates that the VM is **not** using a **Confidential VM**.<br>When enabled, Confidential VMs encrypt VM memory and data-in-transit, providing a layer of security that protects data *while it is being processed* from the cloud provider's infrastructure. |
| **Preserved state size** | 0 GB | This refers to the amount of data saved when the VM is set up to **suspend** or **stop** while preserving the contents of its memory (RAM). <br>The size is **0 GB**, which is expected since the instance status is **Stopped**, not suspended with preserved memory. |

## Machine Configuration

| Name | Value | Meaning |
| :--- | :--- | :--- |
| **Machine type** | e2-medium (2 vCPUs, 4 GB Memory) | The **predefined resource configuration** for the VM, specifying it has **2 virtual CPUs** and **4 GB of RAM (Memory)**. <br>The `e2` family is a general-purpose, cost-effective machine type. |
| **CPU platform** | Unknown CPU Platform | The **specific model of the underlying physical CPU** (e.g., Intel Skylake or Cascade Lake).<br>This is often "Unknown" when using machine types like E2, as the platform is automatically selected to optimize performance and availability. |
| **Minimum CPU platform** | None | An optional setting that lets you specify the **minimum required CPU architecture** (e.g., *Intel Ice Lake*) for performance-sensitive workloads. **None** means the platform is chosen automatically. |
| **Architecture** | x86/64 | The **instruction set architecture** of the virtual machine, which is the standard 64-bit architecture used by most modern computers. |
| **vCPUs to core ratio** | — | Relevant only on **sole-tenant nodes**, this controls how virtual CPUs are mapped to physical CPU cores. |
| **Custom visible cores** | — | Allows control over the number of cores the guest OS sees, relevant for licensing scenarios. |
| **All-core turbo-only mode** | — | An option to run all cores at the **maximum turbo frequency** when under load, available on specific compute-optimized machine types. |
| **Display device** | Disabled | A virtual **display adapter** is not attached to the instance. This is the default for headless (non-GUI) server instances. |
| **Enable to use screen capturing and recording tools** | | A description instructing the user that the **Display device** must be **enabled** if they need to capture screenshots or record the VM's console output. |
| **GPUs** | None | Indicates that no **Graphical Processing Units** are attached to the instance. |
| **Resource policies** | | A placeholder for any attached policies that manage scheduled events (e.g., automatic start/stop times) for the VM. |

## Firewall Rules

| Name | Value | Meaning |
| :--- | :--- | :--- |
| **Firewalls** | | This section controls network access (inbound traffic) to the instance. |
| **HTTP traffic** | Off | Indicates that the default firewall rule to allow inbound network traffic on **port 80** (used for standard, unencrypted web traffic) is **not active**.<br>If this were a public web server, it wouldn't be accessible over HTTP. |
| **HTTPS traffic** | Off | Indicates that the default firewall rule to allow inbound network traffic on **port 443** (used for secure, encrypted web traffic) is **not active**.<br>If this were a secure web server, it wouldn't be accessible over HTTPS. |
| **Allow Load Balancer Health checks** | Off | Indicates that the firewall rule required to allow a **Google Cloud Load Balancer** to check the status (or "health") of this instance is **not active**.<br>If this instance were part of a load-balanced group, it would likely fail health checks. |

```
In summary, all these settings being Off means the instance is not accessible for standard web traffic or health-check traffic from a Google Cloud Load Balancer. This is common for backend servers, internal tools, or instances that have specialized, manually configured firewall rules.
```

## Disks

| Name | Value | Meaning |
| :--- | :--- | :--- |
| **Type** | Balanced persistent disk | The disk's storage technology.<br>**Balanced Persistent Disks** offer a balance of performance (IOPS and throughput) and cost, suitable for most general-purpose workloads like boot disks. |
| **Size** | 10 GB | The **storage capacity** of the disk.<br>This is a small size, typical for a boot disk containing only the operating system. |
| **Architecture** | x86/64 | The **processor architecture** the disk is compatible with, which is the standard 64-bit architecture. |
| **Zone** | asia-south1-b | The **physical location** (zone) where the disk resides.<br>It must be in the same zone as the instance it's attached to. |
| **Labels** | None | **Key-value pairs** used for organizing and managing resources (e.g., for billing or automation). |
| **Tags** | — | **Network tags** that are typically applied to the VM instance, not the disk itself.<br>The disk usually inherits this field from the instance it's used by. |
| **In use by** | gce-jenkins | The **name of the VM instance** that is currently attached to and using this disk. |
| **Snapshot schedule** | None | Indicates that there is **no automated schedule** set up to regularly back up this disk's data via snapshots. |
| **Source image** | debian-12-bookworm-v20251014 | The **Operating System image** that was used to create the initial content of this disk. |
| **Encryption type** | Google-managed | Specifies that the data on the disk is automatically **encrypted** using keys managed by Google Cloud.<br>This is the default security setting. |
| **Consistency group** | None | A setting used to coordinate snapshots across multiple disks simultaneously to ensure data integrity for complex, multi-disk workloads. |
| **Storage pool** | None | This field is relevant when using specific types of storage like Hyperdisk, indicating the dedicated pool of storage resources it belongs to. |
| **Confidential Computing services** | Disabled | Indicates whether the disk is provisioned to be used with a **Confidential VM**, which requires specific security settings. In this case, it is **Disabled**. |

## Backup Plan

| Name | Value | Meaning |
| :--- | :--- | :--- |
| **Managed by** | Backup and DR Service | Indicates that the instance is **integrated with** (or eligible to be managed by) the **Google Cloud Backup and DR (Disaster Recovery) Service**. This service centralizes backup and recovery for your cloud and on-premises data. |
| **Backup schedule state** | Not configured | The current status of the backup process. **Not configured** means a recurring schedule for creating backups of this VM's disks has **not yet been set up** in the Backup and DR Service. |
| **Backup plan** | — | A placeholder for the specific named **policy or plan** within the Backup and DR Service that defines the frequency, retention, and location of backups. The dash (**—**) confirms that no plan is currently assigned. |

```
In summary, this instance is ready to use the Backup and DR Service, but a specific backup routine (schedule and plan) has not been activated yet.
```

## Shielded VM

| Name | Value | Meaning |
| :--- | :--- | :--- |
| **Shielded VM** | | **Shielded VM** is a collection of security enhancements designed to harden a VM instance against sophisticated malware and attacks that compromise the boot process and firmware. |
| **Secure Boot** | Off | When **Enabled**, this feature verifies the digital signature of all boot components (firmware, bootloader, kernel) against trusted keys before the VM starts. **Off** means this verification process is skipped, making the VM vulnerable to malicious code injected into the boot path. |
| **vTPM** | Off | **vTPM** stands for **Virtual Trusted Platform Module**. When **Enabled**, it provides a virtualized hardware security module that can be used to securely store keys and secrets, and perform a cryptographic "health check" of the boot process. **Off** means this hardware-backed security is unavailable. |
| **Integrity Monitoring** | Off | When **Enabled**, this feature continuously **monitors and verifies the integrity** of the VM's boot process and runtime binary baselines. If a deviation (a security-critical change) is detected, it generates a log alert so you can investigate potential threats. **Off** means the VM's state is not being actively monitored for integrity changes. |

```
In summary, because all Shielded VM features are Off, this instance is running with minimal security protections against firmware and boot-level compromise.
```

## SSH Keys

| Name | Value | Meaning |
| :--- | :--- | :--- |
| **SSH Keys** | None | This refers to **instance-specific SSH keys**.<br>**None** means no individual public SSH keys are explicitly stored on the VM instance to grant user access.<br>Access is likely being managed through project-wide keys or a different mechanism (like OS Login). |
| **Block project-wide SSH keys** | Off | This setting controls whether the instance accepts SSH keys defined at the **project level**.<br>Since it is **Off**, users who have their SSH keys registered at the Google Cloud project level will be able to log into this instance.<br>If it were **On**, only keys explicitly added directly to the instance would work. |

```
In summary, access to this VM instance is currently allowed for any user whose SSH key has been added to the overall Google Cloud project.
```

## API and identity management

| Name | Value | Meaning |
| :--- | :--- | :--- |
| **Service account** | gce-service-account@hawx-brahmin-db.iam.gserviceaccount.com | The **identity** assigned to the VM instance. This account is what the VM uses to authenticate and authorize requests to Google Cloud APIs. |
| **Cloud API access scopes** | Allow default access | A **legacy way** to grant permissions. **Default access** provides broad, but limited, read-only permissions for many services, and write permissions for Cloud Storage and Logging. |
| **BigQuery** | Disabled | The VM's service account **cannot** access or perform operations on the **BigQuery** data warehouse. |
| **Bigtable Admin** | Disabled | The VM's service account **cannot** manage **Bigtable** instances or clusters. |
| **Bigtable Data** | Disabled | The VM's service account **cannot** read or write data to a **Bigtable** instance. |
| **Cloud Datastore** | Disabled | The VM's service account **cannot** interact with the **Cloud Datastore** NoSQL database. |
| **Cloud Debugger** | Disabled | The VM's service account **cannot** use the **Cloud Debugger** service. |
| **Cloud Platform** | Disabled | This scope, often a catch-all, is **Disabled**, relying on the other specific scopes for access. |
| **Cloud Pub/Sub** | Disabled | The VM's service account **cannot** publish or subscribe to messages in **Cloud Pub/Sub**. |
| **Cloud Source Repositories** | Disabled | The VM's service account **cannot** access or interact with code stored in **Cloud Source Repositories**. |
| **Cloud SQL** | Disabled | The VM's service account **cannot** manage or interact with **Cloud SQL** instances. |
| **Compute Engine** | Disabled | The VM's service account **cannot** manage or perform operations on **Compute Engine** resources (like other VMs or disks). |
| **Service Control** | Enabled | The VM has permission to **report usage** to the **Service Control** API. |
| **Service Management** | Read Only | The VM can **view** information about services managed by the **Service Management** API. |
| **Stackdriver Logging API** | Write Only | The VM can **send log data** (e.g., application logs) to the **Cloud Logging** service. |
| **Stackdriver Monitoring API** | Write Only | The VM can **send monitoring metrics** to the **Cloud Monitoring** service. |
| **Stackdriver Trace** | Write Only | The VM can **send trace data** (used for performance analysis) to the **Cloud Trace** service. |
| **Storage** | Read Only | The VM can **read (view and download)** objects from **Cloud Storage buckets**, but cannot create, modify, or delete them. |
| **Task queue** | Disabled | The VM's service account **cannot** interact with the **Task Queue** service. |
| **User info** | Disabled | The VM's service account **cannot** retrieve user information. |

```
In summary: The VM has been granted **read-only access to Cloud Storage** and **write access to Cloud Logging/Monitoring/Trace**, which is typical for an application that needs to read configuration files and write logs, but does not have the permissions to manage other infrastructure or access databases.
```

## Data Encryption
| Name | Value | Meaning |
| :--- | :--- | :--- |
| **Key ID** | — | A placeholder for the unique identifier of the **encryption key** used to protect the disk data. The dash (**—**) indicates the disk is using the default encryption. |
| **Key name** | — | A placeholder for the descriptive **name of the encryption key**. Since the `Encryption type` was previously listed as **Google-managed**, these fields are empty because Google manages the key automatically, and it is not a **Customer-Managed Encryption Key (CMEK)** or **Customer-Supplied Encryption Key (CSEK)**. |

```
In summary, the disk's data is encrypted, which is the default for Google Cloud, and the encryption key is fully managed by Google. If a custom key were used, the Key ID and Key name would be populated here.
```

## Availability

| Name | Value | Meaning |
| :--- | :--- | :--- |
| **VM provisioning model** | Standard | Indicates a **standard, durable VM instance**. This provisioning model offers a high commitment from the cloud provider regarding uptime and resources, and it typically runs indefinitely until stopped. |
| **Max duration** | 2 hours | This setting is typically used for **Spot VMs (formerly Preemptible VMs)**. For a Standard VM, this value suggests an atypical setting, or may be a relic from a previous configuration, as Standard VMs do not have a hard duration limit. However, if applied, it would limit runtime to 2 hours. |
| **Preemptibility** | Off (Recommended) | The VM is **not a Spot VM**. Spot VMs are much cheaper but can be terminated (preempted) by Google Cloud at any time if the resources are needed elsewhere. **Off** means the VM is guaranteed to run until you stop it. |
| **On VM termination** | Stop | Specifies the action to take when the VM instance is automatically terminated (e.g., if it hits the `Max duration` or is manually stopped). **Stop** means the VM will be powered off, but the boot disk and configuration are preserved. |
| **Graceful shutdown maximum duration** | — | When terminating a VM, this is the **maximum time** the system waits for the guest OS to perform a graceful shutdown before forcing a power-off. The dash (**—**) suggests the default, which is usually a short period (e.g., 90 seconds). |
| **On host maintenance** | Migrate VM instance (Recommended) | This is the crucial setting for high availability. When the underlying physical server requires maintenance, the VM is **Live Migrated** to a different host without interrupting its operation or causing downtime. |
| **Host error timeout** | — | The time the system waits for the underlying physical host to recover from a hardware error before taking another action (e.g., restarting the VM). |
| **Automatic restart** | Off | Specifies whether the VM should **automatically start up** if it is terminated due to an unexpected host failure, error, or maintenance event. **Off** means the VM remains stopped after such an event, requiring manual intervention to restart. |
| **Customer Managed Encryption Key (CMEK) revocation policy** | Do nothing | This policy determines what happens to the VM if the customer-managed key used to encrypt its disk is revoked. **Do nothing** means the VM continues to run, but access to the disk (and starting/stopping the VM) may be blocked until the key is re-enabled. |

## Sole-Tenancy

| Name | Value | Meaning |
| :--- | :--- | :--- |
| **Sole-tenancy** | | This section relates to running the VM on a dedicated physical host (a **Sole-Tenant Node**), as opposed to the default shared host (multi-tenancy). |
| **CPU Overcommit** | Disabled | This setting, only relevant for VMs on **Sole-Tenant Nodes**, allows you to create more virtual CPUs (vCPUs) across your VMs than the physical cores available on the node. **Disabled** means the total number of vCPUs across all VMs on the host cannot exceed the physical core count of the Sole-Tenant Node. |
| **Custom metadata** | None | **Custom metadata** are optional **key-value pairs** that you can pass to the VM instance.<br>These are commonly used for:<br>- **Startup scripts:** Passing a script that the instance executes automatically when it boots up (e.g., to install software or configure the application).<br>- **Configuration:** Storing arbitrary configuration data that applications running on the VM can read. The value **None** means no custom key-value pairs have been defined for this instance. |

```
Since the original configuration in the prompt listed **Physical host: None**, these settings confirm that the instance is **not** currently running on dedicated Sole-Tenant hardware, making the "CPU Overcommit" status largely irrelevant to the instance's current operation.
```