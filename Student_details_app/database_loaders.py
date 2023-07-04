
import pyodbc
import psycopg2
import pandas as pd



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

    def load_to_postgres(self,data):
        insert_query = "INSERT INTO student_details (student_id, student_name, student_email, student_phone) VALUES (%s, %s, %s, %s)"
        data = data
        self.cursor.execute(insert_query, data)
        self.conn.commit()
        print("data loaded to postgres")

        pass
       
    def search_in_database(self):
        query = "SELECT * FROM student_details"
        try:
            df = pd.read_sql(query, self.conn)
            return df
        except:
            print("failed to fetch data")

    def update_data_in_database(self,student_id,student_name,student_email,student_phone):
        update_query = """UPDATE student_details SET student_name = %s, student_email = %s, student_phone = %s WHERE student_id = %s"""
        self.cursor.execute(update_query, (student_name,student_email,student_phone, student_id))
        self.conn.commit()
        print("student data is updated")

    def delete_record_in_database(self,student_id):
        delete_query = """DELETE FROM student_details where student_id=%s"""
        self.cursor.execute(delete_query, (student_id,))
        self.conn.commit()
        print("record is deleted")



# db = Load_to_Database()
# db.connect_to_postgres('localhost','Library','postgres','1234')
# # db.search_in_database()
# db.delete_record_in_database(1001)