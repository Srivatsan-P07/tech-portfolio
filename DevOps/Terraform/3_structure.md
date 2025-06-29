# 📁 Typical Terraform Project Structure

```bash
my-terraform-project/
├── main.tf         # Main logic (resources, modules, providers)
├── variables.tf    # Input variables (with types and defaults)
├── outputs.tf      # Output values (for chaining or user reference)
├── terraform.tfvars  # Actual values for the variables (optional)
├── backend.tf      # (optional) Backend config for remote state
└── provider.tf     # (optional) Provider block (can be merged into main.tf)
```

---

## 🧾 1. **main.tf** – Core Configuration

This is where you define **resources**, **providers**, and **modules**.

```hcl
provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_storage_bucket" "example" {
  name     = "my-unique-bucket-name"
  location = var.region
}
```

> Think of `main.tf` as the **execution plan** of what Terraform will build.

---

## 🎛 2. **variables.tf** – Input Parameters

Declare all configurable inputs here.

```hcl
variable "project_id" {
  description = "GCP project ID"
  type        = string
}

variable "region" {
  description = "GCP region"
  type        = string
  default     = "us-central1"
}
```

> You can override these using `terraform.tfvars` or CLI arguments.

---

## 📤 3. **outputs.tf** – Result Values

Define **what you want Terraform to show you** after a successful `apply`.

```hcl
output "bucket_name" {
  value = google_storage_bucket.example.name
}
```

> Outputs are great for passing data between modules or surfacing key values like URLs, IPs, or resource names.

---

## 🔧 Optional: `terraform.tfvars`

Set actual values here (instead of passing them via CLI):

```hcl
project_id = "my-dev-project"
region     = "us-central1"
```

---

## 🧠 Why Split Files?

| File               | Purpose                | Why?                                    |
| ------------------ | ---------------------- | --------------------------------------- |
| `main.tf`          | Core logic             | Clean separation of concern             |
| `variables.tf`     | Inputs with validation | Reusability and safety                  |
| `outputs.tf`       | Key outputs            | Useful in CI/CD pipelines and modules   |
| `terraform.tfvars` | Input values           | Local overrides, no hardcoding in `.tf` |

---

## 🚀 Workflow Summary

```bash
terraform init         # Setup plugins
terraform validate     # Check syntax
terraform plan         # Preview changes
terraform apply        # Deploy infra
terraform destroy      # Tear down
```