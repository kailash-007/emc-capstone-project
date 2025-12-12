# 📘 EMC Capstone Project – Notes Management Web App

A simple, secure, and Dockerized Flask-based Notes Management Application that allows users to register, log in, and manage personal notes.  
This project demonstrates end-to-end DevOps + Web Development, including:

- Flask backend
- SQLite data storage
- Docker containerization
- Jenkins CI/CD pipeline
- AWS EC2 deployment

## 🚀 Project Overview

The project is designed for educational and demonstration purposes, showing how to build, containerize, and deploy a real-world web application with full automation.  
It includes:

- Flask web application with user authentication
- Secure password hashing using Flask-Bcrypt
- Deployment-ready Docker image
- Automated CI/CD pipeline using Jenkins
- Continuous deployment to an AWS EC2 instance

## 🧰 Tech Stack

**Backend**
- Python 3.12
- Flask (web framework)
- Flask-Bcrypt (password hashing)
- SQLite (database)
- Jinja2 (HTML templates)

**DevOps / Deployment**
- Docker
- Docker Hub
- Jenkins (CI/CD)
- AWS EC2

## 📁 Repository Structure

<img width="439" height="397" alt="image" src="https://github.com/user-attachments/assets/4a04d3a7-d286-470a-b5c5-9ba7b841898f" />

bash
Copy code

## 🛠 Installation & Setup Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/kailash-007/emc-capstone-project.git
cd emc-capstone-project```
2️⃣ Set Up Locally (Without Docker)
```bash
Copy code
cd emc-capstone-project-src
pip install -r requirements.txt
python3 app.py
Open in browser: http://localhost:5000```

3️⃣ Docker Setup (Local or Production)
Build Docker Image

```bash
Copy code
docker build -t emc-capstone.```

Run the Container

```bash
Copy code
docker run -d -p 5000:5000 --name emc-capstone emc-capstone
Open in browser: http://localhost:5000``

⚙️ CI/CD Pipeline (Jenkins) Overview
The CI/CD pipeline automates:

Pulling the latest code from GitHub

Building a new Docker image

Pushing it to Docker Hub

Deploying automatically into AWS EC2

🔄 CI/CD Workflow Summary
GitHub → Jenkins
Webhook triggers Jenkins on push.

Jenkins Pipeline Stages
Checkout repository
Build Docker image
Login to Docker Hub
Push image
Deploy to EC2 via SSH

Deployment Commands on EC2

bash
Copy code
docker stop emc-capstone || true
docker rm emc-capstone || true
docker pull <dockerhub-image>
docker run -d -p 5000:5000 --name emc-capstone <dockerhub-image>
🖥️ Manual Deployment on AWS EC2
bash
Copy code
ssh -i your-key.pem ubuntu@<EC2-PUBLIC-IP>
docker pull <dockerhub-image>
docker run -d -p 5000:5000 --name emc-capstone <dockerhub-image>
