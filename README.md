# QR Code Generator (Dockerized)

[![Docker Image](https://img.shields.io/badge/docker-jyothsnaravi%2Fqr--code--generator--app-blue)](https://hub.docker.com/r/jyothsnaravi/qr-code-generator-app)

A secure, containerized Python application that generates QR codes from URLs. This project demonstrates Docker best practices including multi-stage builds, non-root users, and CI/CD automation with GitHub Actions.

## 📁 Project Structure

- `main.py` - CLI application that generates QR code images from URLs
- `requirements.txt` - Python dependencies (qrcode, Pillow)
- `Dockerfile` - Secure, minimal Docker image configuration
- `.github/workflows/docker-image.yml` - CI/CD workflow for automated builds
- `.dockerignore` - Optimizes Docker build context
- `.gitignore` - Excludes logs, generated files, and Python cache

## 🚀 Quick Start

### Pull from DockerHub (Recommended)

```powershell
docker pull jyothsnaravi/qr-code-generator-app:latest
docker run --rm -v ${PWD}\qr_codes:/app/qr_codes jyothsnaravi/qr-code-generator-app:latest --url https://example.com
```

### Local Development

1. Install dependencies (optional, for local runs):

```powershell
pip install -r requirements.txt
```

2. Run locally:

```powershell
python main.py --url https://example.com
```

3. Build Docker image:

```powershell
docker build -t qr-code-generator-app .
```

4. Run container (detached):

```powershell
docker run -d --name qr-generator -v ${PWD}\\qr_codes:/app/qr_codes qr-code-generator-app --url https://example.com
```

## 🔐 GitHub Actions CI/CD

The workflow automatically builds and pushes the Docker image to DockerHub on every push to `main`.

**Required GitHub Secrets:**
- `DOCKERHUB_USERNAME` - Set to: `jyothsnaravi`
- `DOCKERHUB_TOKEN` - Your DockerHub access token

**DockerHub Image:** https://hub.docker.com/r/jyothsnaravi/qr-code-generator-app

## 🔒 Security Features

1. **Non-Root User** - Application runs as `myuser` (not root)
2. **Minimal Base Image** - Uses `python:3.12-slim-bullseye` (~150MB vs 1GB full image)
3. **No-Cache Pip Installs** - Reduces image size and avoids cached vulnerabilities
4. **Proper File Ownership** - Logs and output directories owned by non-root user
5. **Docker Ignore** - Excludes unnecessary files from build context

## 📦 Docker Image Details

- **Base Image:** python:3.12-slim-bullseye
- **Architecture:** linux/amd64
- **Size:** ~200MB
- **User:** myuser (non-root)
- **Working Directory:** /app
- **Volumes:** `/app/qr_codes`, `/app/logs`

## 📝 Assignment Information

**Course:** IS601 Module 7 - Docker Containerization  
**Repository:** https://github.com/jr987-NJIT/IS601_Module7_Jyothsna  
**Student:** Jyothsna Ravi
