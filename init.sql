-- Initialize FTC Scam Database
-- Note: Database is already created by Docker environment variables

-- Create the user if it doesn't exist (this will be run as postgres superuser)
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'ftc_user') THEN
        CREATE USER ftc_user WITH PASSWORD 'ftc_password';
    END IF;
END
$$;

-- Grant necessary privileges
ALTER USER ftc_user WITH SUPERUSER;
GRANT ALL PRIVILEGES ON DATABASE ftc_scam_data TO ftc_user;

-- Create the main complaints table
CREATE TABLE IF NOT EXISTS ftc_complaints (
    id SERIAL PRIMARY KEY,
    company_phone_number VARCHAR(20),
    created_date TIMESTAMP,
    violation_date TIMESTAMP,
    consumer_city VARCHAR(100),
    consumer_state VARCHAR(50),
    consumer_area_code VARCHAR(10),
    subject TEXT,
    recorded_message_or_robocall VARCHAR(10),
    source_file VARCHAR(255),
    download_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_company_phone ON ftc_complaints(company_phone_number);
CREATE INDEX IF NOT EXISTS idx_created_date ON ftc_complaints(created_date);
CREATE INDEX IF NOT EXISTS idx_violation_date ON ftc_complaints(violation_date);
CREATE INDEX IF NOT EXISTS idx_consumer_state ON ftc_complaints(consumer_state);
CREATE INDEX IF NOT EXISTS idx_subject ON ftc_complaints(subject);

-- Create a table to track downloaded files
CREATE TABLE IF NOT EXISTS downloaded_files (
    id SERIAL PRIMARY KEY,
    file_url VARCHAR(500) UNIQUE,
    file_name VARCHAR(255),
    download_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    records_count INTEGER,
    status VARCHAR(50) DEFAULT 'downloaded'
);

-- Grant permissions on tables
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO ftc_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO ftc_user;
GRANT ALL PRIVILEGES ON SCHEMA public TO ftc_user;

-- Create a view for summary statistics
CREATE OR REPLACE VIEW complaint_summary AS
SELECT 
    COUNT(*) as total_complaints,
    COUNT(DISTINCT company_phone_number) as unique_phone_numbers,
    COUNT(DISTINCT consumer_state) as states_affected,
    MIN(created_date) as earliest_complaint,
    MAX(created_date) as latest_complaint,
    COUNT(CASE WHEN recorded_message_or_robocall = 'Y' THEN 1 END) as robocall_complaints
FROM ftc_complaints; 