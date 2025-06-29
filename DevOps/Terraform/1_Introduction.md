# 🛠️ What is Terraform?

**Terraform** is an open-source Infrastructure as Code (IaC) tool developed by **HashiCorp** that allows you to define and provision infrastructure using a declarative configuration language called **HCL (HashiCorp Configuration Language)**.

It enables:

* Version-controlled infrastructure
* Automation of cloud resources (compute, storage, networking, etc.)
* Infrastructure reproducibility across environments (dev, staging, prod)

---

### 📦 What are Providers in Terraform?

**Providers** are plugins in Terraform that allow it to interact with APIs of different platforms like:

* **Cloud**: AWS, Azure, GCP, Oracle Cloud
* **SaaS**: GitHub, Datadog, PagerDuty
* **Other Tools**: Docker, Kubernetes, Helm

**Example**:
To manage resources in Google Cloud, you use the `google` provider.

```hcl
provider "google" {
  project = "my-gcp-project"
  region  = "us-central1"
}
```

Each provider exposes resources (like `google_compute_instance`, `aws_s3_bucket`, etc.) and data sources.

---

### 📘 What is Infrastructure as Code (IaC)?

**IaC** is the practice of managing and provisioning infrastructure using machine-readable files, rather than manual processes or interactive configuration tools.

#### Benefits:

* **Consistency**: No drift between environments
* **Automation**: Eliminates manual setup
* **Versioning**: Track changes in Git
* **Reusability**: Modules and templates

---

### 🧩 How Terraform Fits into IaC

| Concept                  | Terraform's Role                              |
| ------------------------ | --------------------------------------------- |
| Define infrastructure    | Uses HCL code to declare resources            |
| Provision infrastructure | Runs `terraform apply` to create/update infra |
| Maintain state           | Tracks infra using a state file               |
| Reuse modules            | Supports modular, reusable code               |
| Cross-platform           | Works with many providers and services        |
