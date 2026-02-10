# Architecture

Docker's architecture is designed to simplify the process of building, sharing, and running applications in containers. Here’s how the key components work under the hood:

### 1.  **Docker Engine** :

Docker Engine is the core of Docker's architecture. It has three main components:

* **Server (Daemon)** : This is the background service that manages Docker objects, such as images, containers, networks, and volumes.
* **REST API** : The API allows Docker to communicate with other applications and helps developers control the Daemon programmatically.
* **CLI (Command-Line Interface)** : The Docker CLI enables users to interact with Docker using commands.

### 2.  **Images** :

Docker Images are lightweight, standalone, and executable packages that include everything needed to run an application—code, runtime, libraries, environment variables, and more. They act as blueprints for containers. Images can be built from scratch or customized using a `Dockerfile`.

### 3.  **Containers** :

Containers are running instances of Docker Images. They are isolated from each other and the host system, ensuring consistent behavior regardless of where they are deployed. Containers leverage the host's OS kernel, making them faster and more efficient compared to virtual machines.

### 4.  **Docker Hub** :

Docker Hub is a cloud-based registry where users can find and share Docker Images. It's a centralized platform to pull pre-built images or push custom-built images, making collaboration easier.

**How It All Works:**
Docker simplifies software development by enabling developers to package applications into containers. Docker Engine runs the containers, Docker Images define the container environment, and Docker Hub connects the community by providing access to image repositories.

Want to dive deeper into any of these components? Just let me know!
