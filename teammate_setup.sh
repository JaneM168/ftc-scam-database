#!/bin/bash

echo "🚀 FTC Scam Database - Quick Setup"
echo "=================================="
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

# Check if the package file exists
if [ ! -f "ftc_scam_database_simple.tar.gz" ]; then
    echo "❌ Package file not found. Please make sure ftc_scam_database_simple.tar.gz is in this directory."
    exit 1
fi

echo "✅ Package file found"

# Extract the package
echo "📦 Extracting package..."
tar -xzf ftc_scam_database_simple.tar.gz
cd ftc_scam_database_simple

echo "✅ Package extracted"

# Start the database
echo "🐳 Starting database..."
docker compose up -d

# Wait a moment for containers to start
sleep 5

# Check if containers are running
if docker ps | grep -q "ftc-scam-db"; then
    echo "✅ Database is running!"
    echo ""
    echo "🎉 Setup Complete!"
    echo "=================="
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
    echo "   docker exec ftc-scam-db psql -U ftc_user -d ftc_scam_data -c \"SELECT COUNT(*) FROM ftc_complaints;\""
    echo ""
    echo "📖 For more information, see TEAMMATE_INSTRUCTIONS.md"
else
    echo "❌ Database failed to start. Check logs with:"
    echo "   docker logs ftc-scam-db"
    exit 1
fi 