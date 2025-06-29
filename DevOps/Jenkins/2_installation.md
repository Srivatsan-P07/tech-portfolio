## ✅ **Step-by-Step: Install Jenkins with Docker**

### 📁 1: Use Docker Compose

Create a `docker-compose.yml` file:

```yaml
version: '3.8'
services:
  jenkins:
    image: jenkins/jenkins:lts
    container_name: jenkins
    ports:
      - "8080:8080"
      - "50000:50000"
    volumes:
      - jenkins_home:/var/jenkins_home

volumes:
  jenkins_home:
```

Run with:

```bash
docker-compose up -d
```

---

### 🔓 2. **Access Jenkins UI**

Open your browser and go to:

```
http://localhost:8080
```

---

### 🔑 3. **Get Initial Admin Password**

Run this to get the admin password:

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Copy the password, paste it into the UI, and continue with setup (install plugins, create admin user, etc.)

Jenkins UserName: srivatsan
Password: password
