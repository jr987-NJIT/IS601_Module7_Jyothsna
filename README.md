# QR Code Generator (Dockerized)

This repository contains a small QR Code Generator application in Python and the Docker configuration to build and run it.

Files added:
- `main.py` - small CLI program that generates a QR code image for a given URL and saves it in `qr_codes/`.
- `requirements.txt` - Python dependencies.
- `Dockerfile` - secure, minimal image using a non-root user.
- `.github/workflows/docker-image.yml` - GitHub Actions workflow to build and push the Docker image to DockerHub (requires secrets).

Quick local usage

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

Notes about GitHub Actions

The workflow `docker-image.yml` uses the following secrets which you must set in your GitHub repository settings:
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN` (use a Docker Hub access token or password)

The workflow builds and pushes `jr987-NJIT/qr-code-generator-app:latest`. Update the image name if you want a different DockerHub repository.

Repository SSH link (provided by user): `git@github.com:jr987-NJIT/IS601_Module7_Jyothsna.git`

Reflection and screenshots

Please add screenshots of the container logs and a successful GitHub Actions run, and fill `reflection.md` with your notes about the process.
