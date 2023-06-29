
import pyodbc
import psycopg2




class Load_to_Database():
    def __init__(self):
        self.flag=False
        pass

    def connect_to_sql_server(self,server_name, database_name, username, password):
        driver = "SQL Server Native Client 11.0"
        connection_string = f"DRIVER={driver};SERVER={server_name};DATABASE={database_name};UID={username};PWD={password}"
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        print("connection successful")
        self.flag = True

        # sql = "INSERT INTO Studen_Details (StudenID, STUDENT_NAME, STUDENT_EMAIL,STUDENT_PHONE) VALUES (?, ?, ?, ?)"
        # # data = ('1001', 'Vishal', 'vishal@gmail','7083264478')
        # cursor.execute(sql, data)
        # conn.commit()

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
       
