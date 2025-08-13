import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database connection parameters
db_params = {
    "dbname": "sample_db",
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "host": "postgres-app",
    "port": "5432"
}

try:
    # Establish connection
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    
    # Test query to verify connection
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Connected to database successfully! PostgreSQL version: {db_version[0]}")
    
    # Optional: Create a test table and insert data to verify functionality
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100)
        );
    """)
    cursor.execute("INSERT INTO test_table (name) VALUES (%s) RETURNING id;", ("Test User",))
    inserted_id = cursor.fetchone()[0]
    print(f"Inserted test record with ID: {inserted_id}")
    
    # This is to ensure changes are saved
    conn.commit()
    
except psycopg2.Error as e:
    print(f"Error connecting to the database: {e}")
    
finally:
    # Clean up
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
        print("Database connection closed.")
