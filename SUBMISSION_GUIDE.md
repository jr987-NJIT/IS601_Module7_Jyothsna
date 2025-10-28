# IS601 Module 7 - Docker Assignment Submission Guide

## 📋 Verification Checklist

All files have been created and tested locally:
- ✅ `main.py` - QR Code Generator application
- ✅ `requirements.txt` - Python dependencies (qrcode, Pillow)
- ✅ `Dockerfile` - Secure Docker image configuration
- ✅ `.github/workflows/docker-image.yml` - CI/CD workflow
- ✅ `.gitignore` - Excludes logs, qr_codes, and Python cache
- ✅ `README.md` - Project documentation
- ✅ `reflection.md` - Assignment reflection (customize before submission)

## 🚀 Next Steps for Submission

### Step 1: Initialize Git Repository

```powershell
cd C:\Users\HP\Desktop\Module7

# Initialize git (if not already done)
git init

# Add all files
git add .

# Make initial commit
git commit -m "Initial commit of QR Code Generator application"

# Add your GitHub remote (SSH)
git remote add origin git@github.com:jr987-NJIT/IS601_Module7_Jyothsna.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 2: Configure GitHub Secrets for DockerHub

1. Go to your GitHub repository: `https://github.com/jr987-NJIT/IS601_Module7_Jyothsna`
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret** and add:
   - **Name**: `DOCKERHUB_USERNAME`  
     **Value**: Your DockerHub username (e.g., `jr987njit`)
   - **Name**: `DOCKERHUB_TOKEN`  
     **Value**: Your DockerHub password or access token

**To create a DockerHub Access Token** (recommended over password):
1. Log in to https://hub.docker.com
2. Click your username → **Account Settings** → **Security**
3. Click **New Access Token**
4. Give it a description (e.g., "GitHub Actions") and generate
5. Copy the token and use it as `DOCKERHUB_TOKEN`

### Step 3: Update DockerHub Image Name (if needed)

If your DockerHub username is different from `jr987-NJIT`, update the image tag in `.github/workflows/docker-image.yml`:

```yaml
tags: YOUR-DOCKERHUB-USERNAME/qr-code-generator-app:latest
```

### Step 4: Push to GitHub and Trigger Workflow

After pushing your code, GitHub Actions will automatically:
1. Build the Docker image
2. Push it to DockerHub as `jr987-NJIT/qr-code-generator-app:latest`

Monitor the workflow:
1. Go to your repository on GitHub
2. Click the **Actions** tab
3. Watch the "Build and push Docker image" workflow run

### Step 5: Manually Push to DockerHub (Alternative)

If you prefer to push manually instead of using GitHub Actions:

```powershell
# Log in to DockerHub
docker login

# Tag the image (replace with your DockerHub username)
docker tag qr-code-generator-app jr987-NJIT/qr-code-generator-app:latest

# Push to DockerHub
docker push jr987-NJIT/qr-code-generator-app:latest
```

Your image will be available at: `https://hub.docker.com/r/jr987-NJIT/qr-code-generator-app`

### Step 6: Capture Required Screenshots

#### Screenshot 1: Container Logs
Run the container and capture logs:

```powershell
# Run container
docker run -d --name qr-generator-submission -v ${PWD}\qr_codes:/app/qr_codes qr-code-generator-app --url https://www.njit.edu

# Get logs
docker logs qr-generator-submission
```

**Screenshot**: Capture the terminal showing the successful log output:
```
Saved QR to qr_codes/www.njit.edu_XXXXXXXXX.png
```

**Clean up**:
```powershell
docker stop qr-generator-submission
docker rm qr-generator-submission
```

#### Screenshot 2: GitHub Actions Workflow Success
1. Go to your repository on GitHub
2. Click **Actions** tab
3. Click on the successful workflow run
4. **Screenshot**: Capture the page showing all green checkmarks for the workflow steps

### Step 7: Customize and Finalize Reflection

Edit `reflection.md` and add your personal insights:
- Your name
- Specific challenges you faced
- What you learned
- Any additional improvements you'd suggest

### Step 8: Final Submission

Submit the following to your instructor:

1. **GitHub Repository Link**:  
   `https://github.com/jr987-NJIT/IS601_Module7_Jyothsna`

2. **DockerHub Image Link**:  
   `https://hub.docker.com/r/jr987-NJIT/qr-code-generator-app`

3. **Screenshots**:
   - Container logs showing successful QR generation
   - GitHub Actions workflow showing successful build and push

4. **Reflection Document**:
   - Submit the customized `reflection.md`

## 🧪 Testing Checklist

Before submission, verify:

- [ ] Local Python script runs: `python main.py --url https://example.com`
- [ ] Docker image builds: `docker build -t qr-code-generator-app .`
- [ ] Container runs successfully: `docker run --rm qr-code-generator-app`
- [ ] Volume mount works: QR codes appear in host `qr_codes/` directory
- [ ] Git repository pushed to GitHub
- [ ] GitHub Actions workflow completes successfully
- [ ] Docker image is available on DockerHub
- [ ] Reflection document is personalized and complete

## 📊 Grading Rubric Alignment

| Requirement | Points | Status |
|------------|--------|--------|
| GitHub Repository Link (accessible, complete) | 15 | ✅ Ready |
| DockerHub Image Link (tagged, pushed) | 15 | ✅ Ready (after push) |
| Container Logs Screenshot | 5 | ⏳ Capture needed |
| GitHub Actions Screenshot | 5 | ⏳ Capture needed |
| Reflection Document | 10 | ⏳ Customize needed |
| Docker Image Builds Successfully | 25 | ✅ Verified |
| Container Runs Correctly | 25 | ✅ Verified |
| **Total** | **100** | |

## 🐛 Troubleshooting

**Issue**: GitHub Actions fails with "denied: requested access to the resource is denied"
- **Solution**: Double-check that `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` secrets are set correctly in GitHub repository settings.

**Issue**: Container fails with permission errors
- **Solution**: The Dockerfile already uses a non-root user (`myuser`) with proper ownership. If issues persist, check volume mount paths.

**Issue**: QR code files not appearing in host directory
- **Solution**: Ensure you're using the correct volume mount syntax for PowerShell: `-v ${PWD}\qr_codes:/app/qr_codes`

**Issue**: "snapshot does not exist" error during Docker build
- **Solution**: Run `docker build --no-cache -t qr-code-generator-app .` to rebuild without cache.

## 📞 Support

If you encounter issues:
1. Review the `README.md` for usage instructions
2. Check Docker logs: `docker logs <container-name>`
3. Verify Docker version: `docker --version` (tested with 28.5.1)
4. Check GitHub Actions logs for CI/CD issues

---

**Good luck with your submission! 🚀**
