import psycopg2

# PostgreSQL connection details
host = "book_lending_db"
database = "Library"
user = "postgres"
password = "1234"

# SQL statement to create the table
create_book_table_query = """
    CREATE TABLE IF NOT EXISTS books_details (
        book_code VARCHAR(20),
        book_title VARCHAR(100),
        book_author VARCHAR(100),
        book_description VARCHAR(100)
    )
"""

create_student_table_query = """
    CREATE TABLE IF NOT EXISTS student_details (
        student_id VARCHAR(20),
        student_name VARCHAR(100),
        student_phone VARCHAR(100),
        student_email VARCHAR(100)
    )
"""

create_book_lending_table_query = """
    CREATE TABLE IF NOT EXISTS book_lending_details (
        student_id VARCHAR(20),
        student_name VARCHAR(100),
        book_code VARCHAR(100),
        book_title VARCHAR(100),
        book_author VARCHAR(100),
        book_description VARCHAR(100),
        assigne_date VARCHAR(100),
        return_date VARCHAR(100)
    )
"""

lst=[]
lst.append(create_book_table_query)
lst.append(create_student_table_query)
lst.append(create_book_lending_table_query)



def create_table(query):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Execute the CREATE TABLE query
        cursor.execute(query)

        # Commit the changes to the database
        conn.commit()

        print("Table  created successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)



for i in lst:
    create_table(i)