# MMA Fighter Hub 🥊

A simple MMA website built using Python, Flask, HTML, CSS, Docker, Jenkins, and Kubernetes.

---

# Features

- View MMA fighters
- Responsive frontend UI
- Docker containerization
- Kubernetes deployment
- CI/CD ready project
- Beginner DevOps project

---

# Technologies Used

- Python
- Flask
- HTML
- CSS
- Docker
- Kubernetes
- Jenkins
- GitHub

---

# Project Structure

```bash
scratchtoend/
│
├── app.py
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

# Run Locally

## Install Flask

```bash
python -m pip install flask
```

## Run Application

```bash
python app.py
```

Open:

```bash
http://localhost:3000
```

---

# Docker Setup

## Build Docker Image

```bash
docker build -t mma .
```

## Run Docker Container

```bash
docker run -d -p 3000:3000 --name mma-container mma
```

Open:

```bash
http://localhost:3000
```

---

# Kubernetes Deployment

## Apply Deployment

```bash
kubectl apply -f deployment.yaml
```

## Apply Service

```bash
kubectl apply -f service.yaml
```

## Check Pods

```bash
kubectl get pods
```

## Check Services

```bash
kubectl get svc
```

Open:

```bash
http://localhost:30007
```

---

# CI/CD Pipeline

This project can be integrated with Jenkins for automatic:

- GitHub webhook trigger
- Docker image build
- Kubernetes deployment

---

# Author

Junaid Shaikh
