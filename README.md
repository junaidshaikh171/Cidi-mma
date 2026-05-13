# MMA Fighter Hub 🥊

A simple MMA website built using Python, Flask, HTML, CSS, and Docker.

## Features

- View MMA fighters
- Display wins, losses, and weight class
- Simple responsive UI
- Docker support

---

# Technologies Used

- Python
- Flask
- HTML
- CSS
- Docker

---

# Project Structure

```bash
scratchtoend/
│
├── app.py
├── Dockerfile
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

# Run Project Locally

## Install Flask

```bash
python -m pip install flask
```

## Run Flask App

```bash
python app.py
```

Open in browser:

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

Open in browser:

```bash
http://localhost:3000
```

---

# Author

Junaid Shaikh
