EMC Capstone Project – Notes Management Web App

A simple, secure, Dockerized Flask application that allows users to register, log in, and manage personal notes.
The project includes a full CI/CD pipeline using Jenkins that automatically builds, pushes, and deploys the application to an AWS EC2 instance.

🚀 Project Overview

The EMC Capstone Project is a lightweight notes application built for educational and demonstration purposes.
It showcases:

Web application development using Flask

Secure password management using Flask-Bcrypt

Data persistence using SQLite

Containerized deployment with Docker

Automated CI/CD pipeline using Jenkins

Cloud deployment using AWS EC2

🧰 Tech Stack
Backend

Python 3.12

Flask (web framework)

Flask-Bcrypt (password hashing)

SQLite (database)

Jinja2 (templating)

DevOps & Deployment

Docker (container packaging)

Docker Hub (image registry)

Jenkins (CI/CD pipeline)

AWS EC2 (deployment target)

📁 Repository Structure
emc-capstone-project/
│
├── emc-capstone-project-src/
│   ├── app.py             # Main Flask application
│   ├── models.py          # User & notes data operations
│   ├── database.py        # SQLite initialization
│   ├── templates/         # HTML templates (UI)
│   ├── static/            # CSS / JS (if needed)
│   └── requirements.txt   # Python dependencies
│
├── Dockerfile             # Docker build configuration
├── Jenkinsfile            # CI/CD pipeline script
└── README.md              # Project documentation

📝 Application Features
🔐 User Authentication

New users can register an account.

Secure password hashing using Bcrypt.

Session-based login handling.

🗒️ Notes Management

Users can add new notes.

Previously saved notes are listed automatically.

Notes are stored in an SQLite database.

🐳 Containerized Deployment

Full application runs inside a Docker container.

Uses a lightweight python:3.12-slim base image.

Exposes port 5000 for web access.

⚙️ Automated CI/CD Pipeline

Jenkins pipeline performs the following:

Pulls the latest code from GitHub

Builds a new Docker image

Pushes image to Docker Hub

SSH deploys to EC2

Stops old container

Runs updated container automatically

🔄 CI/CD Workflow Overview
1. GitHub → Jenkins (Webhook)

Whenever you push to GitHub, Jenkins automatically triggers a new build.

2. Jenkins Pipeline Stages

Checkout: pulls the repository

Build: creates Docker image

Login: authenticates to Docker Hub

Push: publishes image to registry

Deploy: connects to EC2 → pulls image → restarts container

3. EC2 Deployment

The EC2 instance runs:

docker stop emc-capstone

docker rm emc-capstone

docker pull <latest image>

docker run -d -p 5000:5000 emc-capstone
