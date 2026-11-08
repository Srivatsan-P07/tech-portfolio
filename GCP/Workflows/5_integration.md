
# **Integration in GCP Workflows**

Integration allows your workflow to act as an orchestrator by calling external REST APIs, Google Cloud services, or serverless functions (like Cloud Run).

* **`call`**: Specifies the service or method to invoke (e.g., `http.get`, `http.post`).
* **`args`**: Passes parameters like URL, headers, query parameters, or request bodies.
* **`result`**: Captures the API's response into a variable for later steps.
* **`Authentication`**: Secures calls to Google Cloud resources (using built-in OIDC tokens).

---

### **Example: Calling an HTTP API**

```yaml
main:
  steps:
    - callExternalApi:
        call: http.get
        args:
          url: https://api.example.com/users/123
          headers:
            Accept: "application/json"
        result: apiResponse

    - processResult:
        return: ${apiResponse.body.username}

```

> **Summary:** Use `call` with `http.get`/`http.post` to interact with any external API or Cloud service, use `args` to configure the request, and store the output using `result`.
