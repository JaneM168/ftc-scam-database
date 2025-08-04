# FTC Scam Database Backup

This package contains a **complete PostgreSQL database backup** with 6.45 million FTC scam complaint records from 2022-2025.

## 📊 Package Contents

- **Database Backup**: 6.45M FTC complaint records
- **Size**: 146.8MB
- **Format**: PostgreSQL custom format (.dump)
- **Date Range**: 2022-05-27 to 2025-07-31

## 🚀 How to Use

### Option 1: Download and Restore

1. **Download the backup**:
   ```bash
   # Extract from Docker image
   docker run --rm -v $(pwd):/backup ghcr.io/janem168/ftc-scam-database-backup:1.0.0 cp /backup/ftc_database_backup.dump /backup/
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
   git clone https://github.com/janem168/ftc-scam-database.git
   cd ftc-scam-database
   ```

2. **Download and run restoration**:
   ```bash
   # Download backup from package
   docker run --rm -v $(pwd):/backup ghcr.io/janem168/ftc-scam-database-backup:1.0.0 cp /backup/ftc_database_backup.dump /backup/
   
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
1. Check the main repository: https://github.com/janem168/ftc-scam-database
2. Review the restoration script and documentation
3. Contact the development team

---

**Package Version**: 1.0.0
**Created**: 2025-08-04 17:05:25
**Status**: ✅ Ready for Restoration
