#!/usr/bin/env python3

import subprocess
import os
import sys
from datetime import datetime

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✅ {description} completed")
        return result.stdout.strip()
    else:
        print(f"❌ {description} failed:")
        print(f"   Error: {result.stderr}")
        return None

def push_to_github_packages():
    """Push database backup to GitHub Packages"""
    
    print("📦 Pushing FTC Database Backup to GitHub Packages")
    print("=================================================")
    
    # Check if backup file exists
    if not os.path.exists("ftc_database_backup.dump"):
        print("❌ Backup file not found: ftc_database_backup.dump")
        print("   Please create the backup first.")
        return False
    
    # Get backup file size
    backup_size = os.path.getsize("ftc_database_backup.dump") / (1024 * 1024)  # MB
    print(f"✅ Backup file found: {backup_size:.1f}MB")
    
    # GitHub Packages configuration
    GITHUB_USERNAME = "janem168"  # Your GitHub username (lowercase for Docker)
    PACKAGE_NAME = "ftc-scam-database-backup"
    VERSION = "1.0.0"
    
    print(f"📋 Package Details:")
    print(f"   Repository: {GITHUB_USERNAME}/ftc-scam-database")
    print(f"   Package: {PACKAGE_NAME}")
    print(f"   Version: {VERSION}")
    print("")
    
    # Check if Docker is available
    docker_check = run_command("docker --version", "Checking Docker")
    if not docker_check:
        print("❌ Docker is required but not found")
        return False
    
    # Create Dockerfile for the package
    dockerfile_content = f"""# FTC Scam Database Backup Package
FROM alpine:latest

# Add metadata
LABEL org.opencontainers.image.title="FTC Scam Database Backup"
LABEL org.opencontainers.image.description="PostgreSQL database backup with 6.45M FTC scam complaint records (2022-2025)"
LABEL org.opencontainers.image.version="{VERSION}"
LABEL org.opencontainers.image.source="https://github.com/{GITHUB_USERNAME}/ftc-scam-database"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.url="https://github.com/{GITHUB_USERNAME}/ftc-scam-database"
LABEL org.opencontainers.image.vendor="FTC Data Project"

# Copy the backup file
COPY ftc_database_backup.dump /backup/ftc_database_backup.dump

# Add documentation
COPY PACKAGE_README.md /README.md

# Set working directory
WORKDIR /backup

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \\
  CMD test -f /backup/ftc_database_backup.dump || exit 1
"""
    
    with open("Dockerfile.package", "w") as f:
        f.write(dockerfile_content)
    
    # Create package README
    package_readme = f"""# FTC Scam Database Backup

This package contains a **complete PostgreSQL database backup** with 6.45 million FTC scam complaint records from 2022-2025.

## 📊 Package Contents

- **Database Backup**: 6.45M FTC complaint records
- **Size**: {backup_size:.1f}MB
- **Format**: PostgreSQL custom format (.dump)
- **Date Range**: 2022-05-27 to 2025-07-31

## 🚀 How to Use

### Option 1: Download and Restore

1. **Download the backup**:
   ```bash
   # Extract from Docker image
   docker run --rm -v $(pwd):/backup ghcr.io/{GITHUB_USERNAME}/{PACKAGE_NAME}:{VERSION} cp /backup/ftc_database_backup.dump /backup/
   ```

2. **Restore to PostgreSQL**:
   ```bash
   # Start PostgreSQL container
   docker compose up -d postgres
   
   # Restore the backup
   docker exec -i ftc_scam_db pg_restore -U ftc_user -d ftc_scam_data --verbose --clean --if-exists < ftc_database_backup.dump
   ```

### Option 2: Use the Restoration Script

1. **Clone the repository**:
   ```bash
   git clone https://github.com/{GITHUB_USERNAME}/ftc-scam-database.git
   cd ftc-scam-database
   ```

2. **Download and run restoration**:
   ```bash
   # Download backup from package
   docker run --rm -v $(pwd):/backup ghcr.io/{GITHUB_USERNAME}/{PACKAGE_NAME}:{VERSION} cp /backup/ftc_database_backup.dump /backup/
   
   # Run restoration script
   chmod +x restore_database.sh
   ./restore_database.sh
   ```

## 📈 Database Statistics

- **Total Records**: 6,451,793
- **Unique Phone Numbers**: 4,912,815
- **States Affected**: 70
- **Robocall Complaints**: 3,659,873

## 🔗 Connection Details

After restoration:
- **Host**: localhost
- **Port**: 5433
- **Database**: ftc_scam_data
- **Username**: ftc_user
- **Password**: ftc_password

## 📞 Support

For issues or questions:
1. Check the main repository: https://github.com/{GITHUB_USERNAME}/ftc-scam-database
2. Review the restoration script and documentation
3. Contact the development team

---

**Package Version**: {VERSION}
**Created**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Status**: ✅ Ready for Restoration
"""
    
    with open("PACKAGE_README.md", "w") as f:
        f.write(package_readme)
    
    # Build Docker image
    image_name = f"ghcr.io/{GITHUB_USERNAME}/{PACKAGE_NAME}:{VERSION}"
    build_result = run_command(f"docker build -f Dockerfile.package -t {image_name} .", "Building Docker image")
    if not build_result:
        return False
    
    # Check if GitHub token is available
    github_token = os.getenv('GITHUB_TOKEN')
    if not github_token:
        print("❌ GITHUB_TOKEN environment variable not set")
        print("   Please set your GitHub Personal Access Token:")
        print("   export GITHUB_TOKEN=your_token_here")
        print("")
        print("   Token needs 'write:packages' scope")
        return False
    
    # Login to GitHub Container Registry
    login_result = run_command(f"echo {github_token} | docker login ghcr.io -u {GITHUB_USERNAME} --password-stdin", "Logging into GitHub Container Registry")
    if not login_result:
        print("❌ Failed to login to GitHub Container Registry")
        return False
    
    # Push the image
    push_result = run_command(f"docker push {image_name}", "Pushing to GitHub Packages")
    if not push_result:
        return False
    
    print("")
    print("🎉 Successfully pushed to GitHub Packages!")
    print("==========================================")
    print("")
    print(f"📦 Package URL: https://github.com/{GITHUB_USERNAME}/ftc-scam-database/packages")
    print(f"🐳 Docker Image: {image_name}")
    print("")
    print("📤 Share with your teammate:")
    print(f"   docker pull {image_name}")
    print("")
    print("📖 Teammate instructions:")
    print("   1. Pull the image: docker pull " + image_name)
    print("   2. Extract backup: docker run --rm -v $(pwd):/backup " + image_name + " cp /backup/ftc_database_backup.dump /backup/")
    print("   3. Run restoration: ./restore_database.sh")
    
    return True

if __name__ == "__main__":
    push_to_github_packages() 