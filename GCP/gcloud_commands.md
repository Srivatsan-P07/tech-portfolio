# gcloud Command Briefing

A quick reference for common `gcloud` commands related to configuration and authentication.

## Add New Account
*   **Command:** `gcloud auth login`
*   **Explanation:** Authenticates your CLI with a new Google account.
*   **Command:** `gcloud config configurations create <NAME>`
*   **Explanation:** Creates a new named configuration profile to keep settings for different accounts separate.

## See / Switch between Existing Account
*   **List:** `gcloud config configurations list`
*   **Switch:** `gcloud config configurations activate <NAME>`
*   **Explanation:** Use these to see all your profiles and toggle between them (e.g., switching from a personal account to a work account).

---

### `gcloud config configurations list`
*   **Explanation:** Lists all the named `gcloud` configurations on your machine.
*   **Use Case:** Useful for managing and switching between different profiles, where each profile can have its own default project, account, and compute zone.

---

### `gcloud auth login`
*   **Explanation:** Authorizes the `gcloud` CLI to access Google Cloud using your personal user account.
*   **Use Case:** This is the primary command for a developer to log in and manage resources from the command line. It opens a browser for you to complete the authentication flow.

---

### `gcloud auth application-default login`
*   **Explanation:** Generates and stores user credentials for Application Default Credentials (ADC).
*   **Use Case:** Allows local applications and scripts using Google Cloud client libraries to automatically find and use your credentials for authentication, simplifying local development.

---

### `gcloud auth application-default set-quota-project <PROJECT_ID>`
*   **Explanation:** Specifies a project to be used for billing and API usage quotas for requests made with Application Default Credentials that are not otherwise associated with a project.
*   **Use Case:** When an application makes an API call that isn't tied to a specific project, this command tells Google which project to bill for that usage.