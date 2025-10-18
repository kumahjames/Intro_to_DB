import pymysql

def create_database():
    try:
        # Connect to MySQL server without specifying database
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Kumahjames12#'
        )
        
        cursor = connection.cursor()
        
        # Create database if not exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
        
    except pymysql.Error as e:
        print(f"Error: {e}")
    finally:
        # Close connection
        if 'connection' in locals() and connection.open:
            cursor.close()
            connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    create_database()