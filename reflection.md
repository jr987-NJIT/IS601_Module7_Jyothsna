# Reflection — Dockerizing the QR Code Generator

## Overview
This project successfully containerized a Python-based QR Code Generator application using Docker, implementing security best practices and CI/CD automation with GitHub Actions.

## What Went Well
- **Local Development**: The application ran perfectly locally with Python 3.11, generating QR codes from URLs and saving them to the `qr_codes/` directory.
- **Docker Image Build**: The Dockerfile built successfully on the first attempt using `python:3.12-slim-bullseye` as the base image.
- **Container Execution**: The containerized application ran smoothly with volume mounts, allowing QR code files to persist on the host system.
- **Security Implementation**: Successfully implemented a non-root user (`myuser`) to run the application, reducing the attack surface.

## Challenges Faced
- **Deprecation Warning**: Initially encountered a deprecation warning with `datetime.datetime.utcnow()`. Fixed by updating to `datetime.datetime.now(datetime.UTC)` for Python 3.12 compatibility.
- **Docker Layer Caching Issue**: Encountered a snapshot error during rebuild, resolved by using `--no-cache` flag.
- **Volume Mounting Syntax**: Had to ensure proper PowerShell syntax for volume mounts using `${PWD}\qr_codes:/app/qr_codes`.

## Security Considerations Implemented
1. **Non-Root User**: Created and switched to `myuser` to run the application, minimizing potential damage from vulnerabilities.
2. **Minimal Base Image**: Used `python:3.12-slim-bullseye` instead of the full Python image, reducing the attack surface by ~700MB.
3. **Directory Ownership**: Properly set ownership of `logs/` and `qr_codes/` directories to the non-root user.
4. **No-Cache Installs**: Used `pip install --no-cache-dir` to reduce image size and avoid cached vulnerabilities.

## Future Improvements
1. **Automated Testing**: Add unit tests and integrate with GitHub Actions to run tests before building the Docker image.
2. **Multi-Architecture Support**: Build images for both AMD64 and ARM64 architectures for broader compatibility.
3. **Image Scanning**: Integrate Docker image vulnerability scanning (e.g., Trivy, Snyk) in the CI/CD pipeline.
4. **Versioning**: Implement semantic versioning and tag images with version numbers instead of just `latest`.
5. **Health Checks**: Add Docker HEALTHCHECK instruction to monitor container health.
6. **Environment Variables**: Allow URL and output path configuration via environment variables for more flexibility.

## Lessons Learned
- Docker layer caching is powerful but can occasionally cause issues requiring `--no-cache` rebuilds.
- Security in containerization goes beyond just creating images — proper user permissions and minimal dependencies are crucial.
- GitHub Actions provides a seamless way to automate Docker builds and pushes to DockerHub.
- Volume mounts are essential for persisting data generated inside containers.

---

**Author**: [Your Name]  
**Date**: October 27, 2025  
**Course**: IS601 Module 7
