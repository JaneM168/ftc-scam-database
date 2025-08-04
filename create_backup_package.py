#!/usr/bin/env python3

import os
import json
import shutil
import subprocess
from datetime import datetime

def create_backup_package():
    """Create a complete package with database backup and setup files"""
    
    print("📦 Creating FTC Scam Database Backup Package")
    print("============================================")
    
    # Check if backup file exists
    if not os.path.exists("ftc_database_backup.dump"):
        print("❌ Backup file not found: ftc_database_backup.dump")
        print("   Please run the backup command first.")
        return False
    
    # Get backup file size
    backup_size = os.path.getsize("ftc_database_backup.dump") / (1024 * 1024)  # MB
    print(f"✅ Backup file found: {backup_size:.1f}MB")
    
    # Create package directory
    package_dir = "ftc_scam_database_with_backup"
    if os.path.exists(package_dir):
        shutil.rmtree(package_dir)
    os.makedirs(package_dir)
    
    print(f"📁 Creating package directory: {package_dir}")
    
    # Copy essential files
    essential_files = [
        "docker-compose.yml",
        "init.sql", 
        "restore_database.sh",
        "ftc_database_backup.dump",
        "README.md",
        "TEAMMATE_INSTRUCTIONS.md"
    ]
    
    for file in essential_files:
        if os.path.exists(file):
            shutil.copy(file, package_dir)
            print(f"✅ Copied: {file}")
        else:
            print(f"⚠️  Missing: {file}")
    
    # Create package info
    package_info = {
        "name": "FTC Scam Database with Backup",
        "version": "1.0.0",
        "created": datetime.now().isoformat(),
        "backup_size_mb": round(backup_size, 1),
        "records": "6.45 million FTC complaint records",
        "date_range": "2022-2025",
        "setup_method": "restore_from_backup",
        "files_included": essential_files
    }
    
    with open(os.path.join(package_dir, "package_info.json"), "w") as f:
        json.dump(package_info, f, indent=2)
    
    # Create a simple README for the package
    package_readme = f"""# FTC Scam Database - Complete Package

This package contains a **complete PostgreSQL database** with 6.45 million FTC scam complaint records.

## 📊 What's Included

- **Database Backup**: 6.45M records (2022-2025)
- **Setup Files**: Docker configuration and restoration script
- **Documentation**: Complete instructions

## 🚀 Quick Setup (5 minutes)

1. **Extract the package**:
   ```bash
   tar -xzf ftc_scam_database_with_backup.tar.gz
   cd ftc_scam_database_with_backup
   ```

2. **Restore the database**:
   ```bash
   chmod +x restore_database.sh
   ./restore_database.sh
   ```

3. **Connect to database**:
   - Host: localhost
   - Port: 5433
   - Database: ftc_scam_data
   - Username: ftc_user
   - Password: ftc_password

## 📈 Database Statistics

- **Total Records**: 6,451,793
- **Unique Phone Numbers**: 4,912,815
- **States Affected**: 70
- **Date Range**: 2022-05-27 to 2025-07-31
- **Robocall Complaints**: 3,659,873

## 🔍 Sample Queries

```sql
-- Get total complaints
SELECT COUNT(*) FROM ftc_complaints;

-- Get top scam phone numbers
SELECT company_phone_number, COUNT(*) as complaints
FROM ftc_complaints 
GROUP BY company_phone_number 
ORDER BY complaints DESC 
LIMIT 10;

-- Get complaints by state
SELECT consumer_state, COUNT(*) 
FROM ftc_complaints 
GROUP BY consumer_state 
ORDER BY COUNT(*) DESC 
LIMIT 10;
```

## 🌐 Web Interface

Access pgAdmin at: http://localhost:8080
- Email: admin@example.com
- Password: admin

---

**Package Created**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Backup Size**: {backup_size:.1f}MB
**Status**: ✅ Ready to Restore
"""
    
    with open(os.path.join(package_dir, "PACKAGE_README.md"), "w") as f:
        f.write(package_readme)
    
    # Create compressed package
    print("📦 Creating compressed package...")
    result = subprocess.run(f"tar -czf {package_dir}.tar.gz {package_dir}", shell=True)
    
    if result.returncode == 0:
        package_size = os.path.getsize(f"{package_dir}.tar.gz") / (1024 * 1024)  # MB
        print(f"✅ Package created: {package_dir}.tar.gz ({package_size:.1f}MB)")
        print("")
        print("🎉 Backup Package Ready!")
        print("=======================")
        print("")
        print("📁 Package contents:")
        for file in essential_files:
            if os.path.exists(os.path.join(package_dir, file)):
                print(f"   ✅ {file}")
        print("")
        print("📤 Share this file with your teammate:")
        print(f"   {package_dir}.tar.gz")
        print("")
        print("📖 Teammate instructions:")
        print("   1. Extract the .tar.gz file")
        print("   2. Run: ./restore_database.sh")
        print("   3. Connect to localhost:5433")
        return True
    else:
        print("❌ Failed to create package")
        return False

if __name__ == "__main__":
    create_backup_package() 