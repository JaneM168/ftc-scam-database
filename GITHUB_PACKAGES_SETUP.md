# GitHub Packages Setup for Database Backup

## 🎉 Success! Repository Pushed

Your FTC scam database repository has been successfully pushed to GitHub:
**https://github.com/JaneM168/ftc-scam-database**

## 📦 Next Step: Push Database Backup to GitHub Packages

Your database backup (146.8MB) is too large for GitHub's regular file storage, so we'll use **GitHub Packages** (Docker Container Registry) to share it.

### Step 1: Create GitHub Personal Access Token

1. **Go to GitHub Settings**: https://github.com/settings/tokens
2. **Click "Generate new token (classic)"**
3. **Select scopes**:
   - ✅ `write:packages` (required for pushing packages)
   - ✅ `read:packages` (for reading packages)
4. **Click "Generate token"**
5. **Copy the token** (you won't see it again!)

### Step 2: Set the Token

```bash
export GITHUB_TOKEN=your_token_here
```

Replace `your_token_here` with the token you just created.

### Step 3: Push to GitHub Packages

```bash
# Make sure Docker is running
export PATH="/Applications/Docker.app/Contents/Resources/bin:$PATH"

# Run the push script
python3 push_to_github_packages.py
```

### Step 4: Verify the Package

After successful push, you can view your package at:
**https://github.com/JaneM168/ftc-scam-database/packages**

## 🚀 How Your Teammate Gets the Database

### Option 1: Using GitHub Packages (Recommended)

Your teammate can get the database by:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/JaneM168/ftc-scam-database.git
   cd ftc-scam-database
   ```

2. **Pull the database backup**:
   ```bash
   docker pull ghcr.io/janem168/ftc-scam-database-backup:1.0.0
   ```

3. **Extract the backup**:
   ```bash
   docker run --rm -v $(pwd):/backup ghcr.io/janem168/ftc-scam-database-backup:1.0.0 cp /backup/ftc_database_backup.dump /backup/
   ```

4. **Restore the database**:
   ```bash
   chmod +x restore_database.sh
   ./restore_database.sh
   ```

### Option 2: Direct File Sharing

If GitHub Packages doesn't work, you can share the backup file directly:

1. **Send the file**: `ftc_database_backup.dump` (146.8MB)
2. **Via**: Email, Google Drive, Dropbox, USB drive, etc.
3. **Teammate runs**: `./restore_database.sh`

## 📊 What's Included

### Repository Files (on GitHub)
- `docker-compose.yml` - Database setup
- `init.sql` - Database schema
- `restore_database.sh` - Restoration script
- `README.md` - Instructions
- `push_to_github_packages.py` - Package push script

### Package Contents (GitHub Packages)
- `ftc_database_backup.dump` - Complete 6.45M record database
- Documentation and metadata

## 🔍 Troubleshooting

### "Permission denied" Error
- Make sure your GitHub token has `write:packages` scope
- Check that you're logged in: `docker login ghcr.io`

### "Docker not found" Error
- Start Docker Desktop
- Add Docker to PATH: `export PATH="/Applications/Docker.app/Contents/Resources/bin:$PATH"`

### "Large file" Error
- The backup file is excluded from Git (as intended)
- Use GitHub Packages instead of Git for large files

## ✅ Success Checklist

- [ ] Repository pushed to GitHub
- [ ] GitHub Personal Access Token created with `write:packages` scope
- [ ] Database backup pushed to GitHub Packages
- [ ] Teammate can access the package
- [ ] Teammate can restore the database

## 🎯 Result

Your teammate will have:
- **Complete database**: 6.45M FTC scam records
- **Easy setup**: One-command restoration
- **Web interface**: pgAdmin at localhost:8080
- **Full documentation**: README and instructions

---

**Status**: ✅ Repository Ready | 🔄 Package Setup Pending 