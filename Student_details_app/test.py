    
from sqlalchemy import create_engine,text
import urllib
import pandas as pd
import sqlalchemy
import json
import pyodbc



def load_to_database_sql_server(server_name, database_name, username, password):
        driver = "SQL Server Native Client 11.0"
        connection_string = f"DRIVER={driver};SERVER={server_name};DATABASE={database_name};UID={username};PWD={password}"
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        print(cursor)

        sql = "INSERT INTO Studen_Details (StudenID, STUDENT_NAME, STUDENT_EMAIL,STUDENT_PHONE) VALUES (?, ?, ?, ?)"
        data = ('1001', 'Vishal', 'vishal@gmail','7083264478')
        cursor.execute(sql, data)
        conn.commit()

        # StudenID INT PRIMARY KEY,
        # STUDENT_NAME VARCHAR(50),
        # STUDENT_EMAIL VARCHAR(50),
        # STUDENT_PHONE VARCHAR(50)




load_to_database_sql_server('GCS72-PC','Student','sa','Abcd1234@')