
import psycopg2
import pandas as pd

# class Load_to_Database that contains all the functions
class Load_to_Database():
    def __init__(self):
        self.flag=False
        pass


# Function to connect to postgres
    def connect_to_postgres(self,hostname,database_name,user_name,pwd):
        self.flag=False
        try:
            self.conn = psycopg2.connect(host=hostname,database=database_name,user=user_name,password=pwd)
            self.cursor = self.conn.cursor()
            print("connection Successful")
            self.flag=True
        except:
            print("connection failed")
            self.flag=False

# Function to load the data to postgres database
    def load_to_postgres(self,data):
        self.flag=False
        try:
            insert_query = "INSERT INTO public.books_details(book_code,book_title, book_author, book_description)VALUES (%s, %s, %s, %s);"
            data = data
            self.cursor.execute(insert_query, data)
            self.conn.commit()
            print("Data loaded to postgres")
            self.flag=True
        except (Exception, psycopg2.Error) as error:
            print("Error while loading data:", error)
            self.flag=False
            return 0

        pass

# Function to search in the database  
    def search_in_database(self):
        query = "SELECT * FROM public.books_details"
        try:
            df = pd.read_sql(query, self.conn)
            return df
        except:
            print("failed to fetch data")

# Function to update the records in the database
    def update_data_in_database(self,book_name,book_author,book_description,book_id):
        self.flag=False
        try:
            print(book_name,book_author,book_description,book_id)
            update_query = """UPDATE books_details SET book_title = %s, book_author = %s, book_description = %s WHERE book_code = %s"""
            self.cursor.execute(update_query, (book_name,book_author,book_description, book_id))
            self.conn.commit()
            print("Book data is updated")
            self.flag=True
        except (Exception, psycopg2.Error) as error:
            print("Error while updating data:", error)
            self.flag=False
            return 0
# Function to delete the records in the database
    def delete_record_in_database(self,book_id):
        self.flag=False
        try:
            delete_query = """DELETE FROM public.books_details where book_code=%s"""
            self.cursor.execute(delete_query, (book_id,))
            self.conn.commit()
            print("record is deleted")
            self.flag=True
        except (Exception, psycopg2.Error) as error:
            print("Error while deleting data:", error)
            self.flag=False
            return 0


