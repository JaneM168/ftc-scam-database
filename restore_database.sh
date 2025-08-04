#!/bin/bash

echo "🔄 FTC Scam Database - Restore from Backup"
echo "=========================================="
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker Desktop first."
    echo "   Download from: https://www.docker.com/products/docker-desktop"
    exit 1
fi

# Check if Docker is running
if ! docker info &> /dev/null; then
    echo "❌ Docker is not running. Please start Docker Desktop."
    exit 1
fi

echo "✅ Docker is running"

# Check if backup file exists
if [ ! -f "ftc_database_backup.dump" ]; then
    echo "❌ Backup file not found: ftc_database_backup.dump"
    echo "   Please make sure the backup file is in this directory."
    exit 1
fi

echo "✅ Backup file found (154MB)"

# Start the database container
echo "🐳 Starting PostgreSQL container..."
docker compose up -d postgres

# Wait for container to be ready
echo "⏳ Waiting for database to start..."
sleep 10

# Check if container is running
if ! docker ps | grep -q "ftc_scam_db"; then
    echo "❌ Database container failed to start"
    echo "   Check logs with: docker logs ftc_scam_db"
    exit 1
fi

echo "✅ Database container is running"

# Restore the database
echo "📥 Restoring database from backup..."
echo "   This may take a few minutes for 6.45M records..."

docker exec -i ftc_scam_db pg_restore -U ftc_user -d ftc_scam_data --verbose --clean --if-exists < ftc_database_backup.dump

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Database restored successfully!"
    echo "================================"
    echo ""
    echo "📊 Database Statistics:"
    echo "   - 6.45 million FTC scam records"
    echo "   - 2022-2025 date range"
    echo "   - 70 states affected"
    echo ""
    echo "🔗 Connect to database:"
    echo "   - Host: localhost"
    echo "   - Port: 5433"
    echo "   - Database: ftc_scam_data"
    echo "   - Username: ftc_user"
    echo "   - Password: ftc_password"
    echo ""
    echo "🌐 Web Interface (pgAdmin):"
    echo "   - URL: http://localhost:8080"
    echo "   - Email: admin@example.com"
    echo "   - Password: admin"
    echo ""
    echo "🔍 Quick test:"
    echo "   docker exec ftc_scam_db psql -U ftc_user -d ftc_scam_data -c \"SELECT COUNT(*) FROM ftc_complaints;\""
    echo ""
    echo "📖 For more information, see TEAMMATE_INSTRUCTIONS.md"
else
    echo "❌ Database restoration failed"
    echo "   Check logs with: docker logs ftc_scam_db"
    exit 1
fi 