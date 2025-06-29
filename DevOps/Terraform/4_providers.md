# 🧱 Providers & Resources in Terraform

### 🔹 **Provider**

Defines **which platform/service** Terraform will interact with.
In your case: `google` (GCP provider)

### 🔹 **Resource**

Defines **what infrastructure** you want to create (e.g., a GCS bucket, BigQuery dataset, VM instance)

---

## ✅ Step-by-Step: Provision GCP Resources with Terraform

### 1. **main.tf**

```hcl
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_storage_bucket" "my_bucket" {
  name     = var.bucket_name
  location = var.region
  uniform_bucket_level_access = true
}
```

---

### 2. **variables.tf**

```hcl
variable "project_id" {
  type        = string
  description = "GCP project ID"
}

variable "region" {
  type        = string
  description = "GCP region"
  default     = "us-central1"
}

variable "bucket_name" {
  type        = string
  description = "Globally unique bucket name"
}
```

---

### 3. **terraform.tfvars**

```hcl
project_id  = "your-gcp-project-id"
bucket_name = "my-unique-bucket-2025"
```

---

### 4. **outputs.tf** (optional)

```hcl
output "bucket_url" {
  value = "gs://${google_storage_bucket.my_bucket.name}"
}
```

---

## 🧪 Commands to Run

In your folder:

```bash
docker-compose run terraform
```

Inside the container shell:

```bash
terraform init          # Download provider
terraform plan          # See what will be created
terraform apply         # Create the bucket
```

---

## 📦 Resource Examples

Here are more resources you can create with the GCP provider:

| Resource Type     | Terraform Block           |
| ----------------- | ------------------------- |
| GCS Bucket        | `google_storage_bucket`   |
| BigQuery Dataset  | `google_bigquery_dataset` |
| Compute Engine VM | `google_compute_instance` |
| Pub/Sub Topic     | `google_pubsub_topic`     |
| Service Account   | `google_service_account`  |

---

## 🔐 Auth Reminder

Make sure your Docker Compose mounts your GCP credentials and sets:

```yaml
environment:
  - GOOGLE_APPLICATION_CREDENTIALS=/root/.config/gcloud/application_default_credentials.json
```
