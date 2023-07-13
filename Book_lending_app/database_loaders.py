
import psycopg2
import pandas as pd
import psycopg2.extras as extras



class Load_to_Database():
    def __init__(self):
        self.flag=False
        pass


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

    def load_student_to_database(self,data):
        self.flag=False
        try:
            insert_query = "INSERT INTO student_details (student_id, student_name, student_email, student_phone) VALUES (%s, %s, %s, %s)"
            data = data
            self.cursor.execute(insert_query, data)
            self.conn.commit()
            self.flag=True
            print("data loaded to postgres")
        except (Exception, psycopg2.Error) as error:
            self.flag=False
            self.conn.close()            
            print("Error while loading data:", error)

    def load_book_to_database(self,data):
        self.flag=False
        try:
            insert_query = "INSERT INTO books_details (book_code, book_title, book_author, book_description) VALUES (%s, %s, %s, %s)"
            data = data
            self.cursor.execute(insert_query, data)
            self.conn.commit()
            self.flag=True
            print("data loaded to postgres")
        except (Exception, psycopg2.Error) as error:
            self.flag=False
            self.conn.close()            
            print("Error while loading data:", error)
  
       
    def search_in_database(self,table_name):
        query = f"SELECT * FROM {table_name}"
        try:
            df = pd.read_sql(query, self.conn)
            return df
        except:
            print("failed to fetch data")

    def update_student_details_in_database(self,student_id,student_name,student_email,student_phone):
        self.flag=False
        try:
            update_query = """UPDATE student_details SET student_name = %s, student_email = %s, student_phone = %s WHERE student_id = %s"""
            self.cursor.execute(update_query, (student_name,student_email,student_phone, student_id))
            self.conn.commit()
            print("student data is updated")
            self.flag=True
        except (Exception, psycopg2.Error) as error:
            self.flag=False
            print("Error while updating data:", error)

    def update_book_details_in_database(self,book_code,book_title,book_author,book_description):
        self.flag=False
        try:
            update_query = """UPDATE books_details SET book_title = %s, book_author = %s, book_description = %s WHERE book_code = %s"""
            self.cursor.execute(update_query, (book_title,book_author,book_description, book_code))
            self.conn.commit()
            print("book details is updated")
            self.flag=True
        except (Exception, psycopg2.Error) as error:
            self.flag=False
            print("Error while updating data:", error)

    def delete_student_record_in_database(self,student_id):
        self.flag=False
        try:
            delete_query = """DELETE FROM student_details where student_id=%s"""
            self.cursor.execute(delete_query, (student_id,))
            self.conn.commit()
            print("record is deleted")
            self.flag=True
        except (Exception, psycopg2.Error) as error:
            self.flag=False
            print("Error while deleting data:", error)

    def delete_book_from_database(self,book_code):
        self.flag=False
        try:
            delete_query = """DELETE FROM books_details where book_code=%s"""
            self.cursor.execute(delete_query, (book_code,))
            self.conn.commit()
            print("book is deleted")
            self.flag=True
        except (Exception, psycopg2.Error) as error:
            self.flag=False
            print("Error while deleting data:", error)


    def load_book_lending_details(self,data):
        tuples = [tuple(x) for x in data.to_numpy()]
        cols = ','.join(list(data.columns))
        query = "INSERT INTO %s(%s) VALUES %%s" % ('public.book_lending_details', cols)
        extras.execute_values(self.cursor , query, tuples)
        self.conn.commit()
        pass


# db = Load_to_Database()
# db.connect_to_postgres('localhost','Library','postgres','1234')
# # db.search_in_database()
# db.delete_record_in_database(1001)