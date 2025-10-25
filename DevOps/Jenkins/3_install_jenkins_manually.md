# 🛠️ Manual Jenkins Installation (Debian/Ubuntu)

## ☕ 1. Install Java (OpenJDK 17)

```bash
sudo apt update
sudo apt install openjdk-17-jdk -y
```

## 🏗️ 2. Install Jenkins

### 2.1 Add Repository and Key

This script **sets up the Jenkins stable repository** on a Debian-based system by performing two steps:

```bash
# It **downloads the official Jenkins GPG key** (`jenkins.io-2023.key`) and saves it to `/usr/share/keyrings/jenkins-keyring.asc` to enable package verification.
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
```


```bash
# It **adds the Jenkins repository line** to a new file, `/etc/apt/sources.list.d/jenkins.list`, instructing the APT package manager to use this repository, verifying packages with the imported key. 🔑
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
```
### 2.2 Final Installation

```bash
# Update and Install
sudo apt update
sudo apt install jenkins -y
```

### 3.1 Modify Configuration

```bash
# Edit Jenkins Configuration file
sudo nano /etc/default/jenkins

# Bind to Local Host
JENKINS_ARGS="--webroot=/var/cache/jenkins/war --httpListenAddress=127.0.0.1 --httpPort=8080"

# Restart to run with new settings
sudo systemctl restart jenkins

# Obtain Initial Admin Password
# Username Admin
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

# 3. Secure Access SSH

```bash
# gcloud compute ssh [VM_NAME] --project=[PROJECT_ID] --zone=[ZONE] -- -L 8080:localhost:8080 -N
gcloud compute ssh gce-jenkins --project=hawx-brahmin-db --zone=asia-south1-b -- -L 8080:localhost:8080 -N
```