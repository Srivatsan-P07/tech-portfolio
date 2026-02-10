Docker images are the building blocks of containers. Think of an **image** as a blueprint or a snapshot of a file system (including your code, libraries, and settings), and a **container** as a running instance of that blueprint.

---

## 1. Pulling Images

Before you build your own, you often start with a "Base Image" from **Docker Hub** (a public registry).

The `docker pull` command downloads an image to your local machine so you can use it.

* **Command:** `docker pull <image_name>:<tag>`
* **Example:** To get the official Python image:
* `docker pull python:3.9-slim`



> **Note:** If you don't specify a tag (like `:3.9-slim`), Docker defaults to `:latest`, which isn't always recommended for production because it can change unexpectedly.

---

## 2. The Dockerfile

A **Dockerfile** is a text document containing all the commands a user could call on the command line to assemble an image. It automates the setup process.

### The Example: A Simple "Hello World" Python App

Imagine you have a file named `app.py`:

```python
print("Hello from inside the Docker container!")
```

To containerize this, you create a file named `Dockerfile` (no extension) in the same folder:

```dockerfile
# 1. Use an existing image as a starting point
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy your local files into the container
COPY app.py .

# 4. Define the command to run when the container starts
CMD ["python", "app.py"]

```

---

## 3. Creating (Building) Images

Once your Dockerfile is ready, you use the `docker build` command to turn that script into a runnable image.

* **Command:** `docker build -t <name-of-image> <path-to-dockerfile>`
* **Example:**
* `docker build -t my-python-app .`



The `.` at the end tells Docker to look for the Dockerfile in the current directory. The `-t` flag stands for "tag," giving your image a friendly name.

---

## 4. Running Your Image

After building, you can verify your image exists with `docker images`. To turn that image into a running container:

* **Command:** `docker run my-python-app`
* **Output:** `Hello from inside the Docker container!`

---

### Summary Table

| Action | Command | Purpose |
| --- | --- | --- |
| **Pull** | `docker pull nginx` | Downloads a pre-made image from the cloud. |
| **Define** | (Create a `Dockerfile`) | Lists instructions to build your environment. |
| **Build** | `docker build -t my-img .` | Executes the Dockerfile to create a local image. |
| **Run** | `docker run my-img` | Starts a container based on your image. |