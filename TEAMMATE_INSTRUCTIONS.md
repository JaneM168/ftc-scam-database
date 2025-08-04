# FTC Scam Database - Teammate Setup Instructions

## 🎯 What You're Getting
A **PostgreSQL database** with **6.45 million FTC scam complaint records** from 2022-2025!

## 📦 What's Included
- Complete database setup
- Docker configuration
- Sample queries
- Documentation

## 🚀 Quick Setup (5 minutes)

### Step 1: Extract the Package
```bash
tar -xzf ftc_scam_database_simple.tar.gz
cd ftc_scam_database_simple
```

### Step 2: Start the Database
```bash
docker compose up -d
```

### Step 3: Verify It's Working
```bash
docker ps
```
You should see containers running for PostgreSQL and pgAdmin.

## 🔗 Connect to the Database

### Option A: Using pgAdmin (Web Interface)
1. Open your browser
2. Go to: http://localhost:8080
3. Login:
   - Email: `admin@example.com`
   - Password: `admin`
4. Add server:
   - Host: `ftc-scam-db` (or `localhost`)
   - Port: `5432`
   - Database: `ftc_scam_data`
   - Username: `ftc_user`
   - Password: `ftc_password`

### Option B: Using Command Line
```bash
docker exec -it ftc-scam-db psql -U ftc_user -d ftc_scam_data
```

### Option C: Using Any PostgreSQL Client
- **Host**: localhost
- **Port**: 5433
- **Database**: ftc_scam_data
- **Username**: ftc_user
- **Password**: ftc_password

## 📊 Database Statistics
- **Total Records**: 6,451,793
- **Unique Phone Numbers**: 4,912,815
- **States Affected**: 70
- **Date Range**: 2022-05-27 to 2025-07-31
- **Robocall Complaints**: 3,659,873

## 🔍 Sample Queries to Try

### Get Total Complaints
```sql
SELECT COUNT(*) FROM ftc_complaints;
```

### Get Complaints by State
```sql
SELECT consumer_state, COUNT(*) 
FROM ftc_complaints 
GROUP BY consumer_state 
ORDER BY COUNT(*) DESC 
LIMIT 10;
```

### Get Top Scam Phone Numbers
```sql
SELECT company_phone_number, COUNT(*) as complaint_count
FROM ftc_complaints 
GROUP BY company_phone_number 
ORDER BY complaint_count DESC 
LIMIT 20;
```

### Get Recent Complaints
```sql
SELECT * FROM ftc_complaints 
WHERE created_date >= '2024-01-01' 
ORDER BY created_date DESC 
LIMIT 10;
```

## 🛠️ Troubleshooting

### Port Already in Use
If port 5433 is busy, change it in `docker-compose.yml`:
```yaml
ports:
  - "5434:5432"  # Change 5433 to 5434
```

### Container Won't Start
Check logs:
```bash
docker logs ftc-scam-db
```

### Can't Connect
Verify the container is running:
```bash
docker ps | grep ftc-scam-db
```

## 🎯 Use Cases

### For Phone Number Blocking
```sql
-- Get phone numbers with most complaints
SELECT company_phone_number, COUNT(*) as complaints
FROM ftc_complaints 
GROUP BY company_phone_number 
HAVING COUNT(*) > 10
ORDER BY complaints DESC;
```

### For Geographic Analysis
```sql
-- Get states with most complaints
SELECT consumer_state, COUNT(*) as complaints
FROM ftc_complaints 
GROUP BY consumer_state 
ORDER BY complaints DESC;
```

### For Trend Analysis
```sql
-- Get complaints by month
SELECT DATE_TRUNC('month', created_date) as month,
       COUNT(*) as complaints
FROM ftc_complaints 
GROUP BY month 
ORDER BY month;
```

## 📞 Support
If you have issues:
1. Check the troubleshooting section above
2. Make sure Docker is running
3. Check the container logs
4. Contact the team

## 🎉 You're All Set!
You now have access to one of the largest scam phone number databases available, with millions of records from the FTC!

---
**Database**: 6.45M FTC scam records  
**Coverage**: 2022-2025  
**Ready for**: Phone blocking, analysis, compliance 