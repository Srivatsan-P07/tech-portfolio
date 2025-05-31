# Docker Command-Line Interface

The **Docker CLI (Command-Line Interface)** is a primary way to interact with Docker and manage containers, images, networks, and more. Here’s an overview of the most common Docker commands and their purposes:

---

### **1. Basic Commands:**

* **`docker version`** : Displays Docker version information.
* **`docker info`** : Shows detailed information about the Docker installation.

---

### **2. Working with Containers:**

* **`docker run <image-name>`** : Creates and starts a container based on an image.
* Example: `docker run ubuntu:latest`
* **`docker ps`** : Lists running containers.
* Add `-a` to list all containers (including stopped ones): `docker ps -a`
* **`docker stop <container-id>`** : Stops a running container.
* **`docker start <container-id>`** : Starts a stopped container.
* **`docker rm <container-id>`** : Removes a container.

---

### **3. Managing Images:**

* **`docker images`** : Lists all available Docker images on the system.
* **`docker pull <image-name>`** : Downloads an image from a registry (like Docker Hub).
* Example: `docker pull nginx:latest`
* **`docker build -t <image-name> <path>`** : Builds a new image from a Dockerfile.
* Example: `docker build -t my-app .`
* **`docker rmi <image-id>`** : Removes an image.

---

### **4. Working with Volumes:**

* **`docker volume create <volume-name>`** : Creates a volume for persistent data storage.
* **`docker volume ls`** : Lists all volumes.
* **`docker volume rm <volume-name>`** : Removes a volume.

---

### **5. Networking:**

* **`docker network ls`** : Lists all Docker networks.
* **`docker network create <network-name>`** : Creates a new network.
* **`docker network rm <network-name>`** : Removes a network.

---

### **6. Logs and Debugging:**

* **`docker logs <container-id>`** : Displays logs from a container.
* **`docker exec -it <container-id> <command>`** : Runs a command inside a running container.
* Example: `docker exec -it my-container bash`

---

These commands are fundamental to managing Docker environments efficiently. Let me know if you'd like to try out an example or explore any of them in detail!
