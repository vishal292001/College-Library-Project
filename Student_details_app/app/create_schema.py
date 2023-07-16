import psycopg2

# PostgreSQL connection details
host = "student_db"
database = "Library"
user = "postgres"
password = "1234"
port= "5432"

# SQL statement to create the table
create_table_query = """
    CREATE TABLE IF NOT EXISTS student_details (
        student_id VARCHAR(20) PRIMARY KEY,
        student_name VARCHAR(100),
        student_email VARCHAR(100),
        student_phone VARCHAR(20)
    )
"""


def create_student_table():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Execute the CREATE TABLE query
        cursor.execute(create_table_query)

        # Commit the changes to the database
        conn.commit()

        print("Table 'student_details' created successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)


