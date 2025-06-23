import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',       # Or your DB server IP
            user='root',   # MySQL username
            password='12345', # MySQL password
            database='axi_db'  # Database name
        )

        if connection.is_connected():
            print("✅ Successfully connected to the database")
            return connection

    except Error as e:
        print(f"❌ Error while connecting to MySQL: {e}")
        return None

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("🔒 MySQL connection closed.")

if __name__ == "__main__":
    conn = create_connection()

    if conn:
        # You can now run queries here
        # Example: print(conn)
        
        close_connection(conn)
