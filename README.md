# FTC Scam Database

A comprehensive PostgreSQL database containing **6.45 million FTC scam complaint records** from 2022-2025.

## 📊 Database Statistics

- **Total Records**: 6,451,793
- **Unique Phone Numbers**: 4,912,815
- **States Affected**: 70
- **Date Range**: 2022-05-27 to 2025-07-31
- **Robocall Complaints**: 3,659,873

## 🚀 Quick Start

### For Teammates (5-minute setup)

1. **Clone this repository**:
   ```bash
   git clone https://github.com/joemo/ftc-scam-database.git
   cd ftc-scam-database
   ```

2. **Run the setup script**:
   ```bash
   chmod +x teammate_setup.sh
   ./teammate_setup.sh
   ```

3. **Connect to the database**:
   - **Host**: localhost
   - **Port**: 5433
   - **Database**: ftc_scam_data
   - **Username**: ftc_user
   - **Password**: ftc_password

### Manual Setup

1. **Start the database**:
   ```bash
   docker compose up -d
   ```

2. **Access pgAdmin** (web interface):
   - URL: http://localhost:8080
   - Email: admin@example.com
   - Password: admin

## 🔍 Sample Queries

### Get Total Complaints
```sql
SELECT COUNT(*) FROM ftc_complaints;
```

### Get Top Scam Phone Numbers
```sql
SELECT company_phone_number, COUNT(*) as complaint_count
FROM ftc_complaints 
GROUP BY company_phone_number 
ORDER BY complaint_count DESC 
LIMIT 20;
```

### Get Complaints by State
```sql
SELECT consumer_state, COUNT(*) 
FROM ftc_complaints 
GROUP BY consumer_state 
ORDER BY COUNT(*) DESC 
LIMIT 10;
```

### Get Recent Complaints
```sql
SELECT * FROM ftc_complaints 
WHERE created_date >= '2024-01-01' 
ORDER BY created_date DESC 
LIMIT 10;
```

## 🎯 Use Cases

### Phone Number Blocking
```sql
-- Get phone numbers with most complaints
SELECT company_phone_number, COUNT(*) as complaints
FROM ftc_complaints 
GROUP BY company_phone_number 
HAVING COUNT(*) > 10
ORDER BY complaints DESC;
```

### Geographic Analysis
```sql
-- Get states with most complaints
SELECT consumer_state, COUNT(*) as complaints
FROM ftc_complaints 
GROUP BY consumer_state 
ORDER BY complaints DESC;
```

### Trend Analysis
```sql
-- Get complaints by month
SELECT DATE_TRUNC('month', created_date) as month,
       COUNT(*) as complaints
FROM ftc_complaints 
GROUP BY month 
ORDER BY month;
```

## 📁 Project Structure

```
ftc-scam-database/
├── docker-compose.yml          # Database and pgAdmin setup
├── init.sql                    # Database schema
├── teammate_setup.sh           # Quick setup script
├── TEAMMATE_INSTRUCTIONS.md    # Detailed instructions
├── README.md                   # This file
└── .gitignore                  # Git ignore rules
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

## 📊 Data Schema

### ftc_complaints Table
- `company_phone_number`: The phone number that received the complaint
- `created_date`: When the complaint was created
- `violation_date`: When the violation occurred
- `consumer_city`: City of the consumer
- `consumer_state`: State of the consumer
- `consumer_area_code`: Area code of the consumer
- `subject`: Subject of the complaint
- `recorded_message_or_robocall`: Whether it was a robocall
- `source_file`: Original CSV file source
- `download_date`: When the data was downloaded
- `created_at`: Database record creation timestamp

## 🔗 Database Connection Details

### PostgreSQL
- **Host**: localhost
- **Port**: 5433
- **Database**: ftc_scam_data
- **Username**: ftc_user
- **Password**: ftc_password

### pgAdmin (Web Interface)
- **URL**: http://localhost:8080
- **Email**: admin@example.com
- **Password**: admin

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review `TEAMMATE_INSTRUCTIONS.md`
3. Check container logs with `docker logs ftc-scam-db`
4. Contact the development team

## 🎉 What You Get

This database provides:
- **Comprehensive Coverage**: Every FTC complaint since 2022
- **Real-time Access**: Instant query capabilities
- **Analytics Power**: Deep insights into scam patterns
- **Compliance Support**: Regulatory reporting capabilities
- **Competitive Advantage**: Unique, comprehensive dataset

---

**Database**: 6.45M FTC scam records  
**Coverage**: 2022-2025  
**Status**: ✅ Ready for Production 