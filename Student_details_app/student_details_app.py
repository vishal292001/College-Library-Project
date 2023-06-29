import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox


from sqlalchemy import create_engine,text
import urllib
import pandas as pd
import sqlalchemy
import json
import pyodbc
import database_loaders




class Student_Details():
    def __init__(self):
        self.root = Tk()
        self.root.title("Student Details App")
        self.root.geometry('1050x650')
        self.root.configure(bg='white')

        self.load_to_db = database_loaders.Load_to_Database()

        self.add_buttons()

    
    def mainloop(self):
        self.root.mainloop()

    def add_buttons(self):
        self.add_student_button_image = Image.open("./images/add_student_button_img.png")
        self.add_student_button_image = self.add_student_button_image.resize((140, 60))
        self.add_student_button_image = ImageTk.PhotoImage(self.add_student_button_image)
        self.add_student_button = ttk.Button(self.root, text="add student",image=self.add_student_button_image,command=self.add_new_student_frame)
        self.add_student_button.place(x=100,y=50)

        self.update_student_button_image = Image.open("./images/update_student_button_img.png")
        self.update_student_button_image = self.update_student_button_image.resize((140, 60))
        self.update_student_button_image = ImageTk.PhotoImage(self.update_student_button_image)
        self.update_student_button = ttk.Button(self.root, text="update student",image=self.update_student_button_image,command=self.update_student_details)
        self.update_student_button.place(x=260,y=50)


        self.delete_student_button_image = Image.open("./images/delete_student_button_img.png")
        self.delete_student_button_image = self.delete_student_button_image.resize((140, 60))
        self.delete_student_button_image = ImageTk.PhotoImage(self.delete_student_button_image)
        self.delete_student_button = ttk.Button(self.root, text="delete student",image=self.delete_student_button_image)
        self.delete_student_button.place(x=420,y=50)

        
        self.authenticate_button_image = Image.open("./images/Authenticate_user_img.png")
        self.authenticate_button_image = self.authenticate_button_image.resize((140, 60))
        self.authenticate_button_image = ImageTk.PhotoImage(self.authenticate_button_image)
        self.authenticate_button = ttk.Button(self.root, text="Aithenticate",image=self.authenticate_button_image,command=self.database_details)
        self.authenticate_button.place(x=730,y=50)




        

        pass

    def add_new_student_frame(self):

        self.student_details_frame = Frame(self.root,bg="white",borderwidth=6,width=600,height=400)
        self.student_details_frame.place(x=40,y=140)

        self.student_details_bg_image = tk.PhotoImage(file='./images/student_details_bg_img.png')
        self.student_details_bg_image_label = tk.Label(self.student_details_frame, bd=0,image=self.student_details_bg_image)
        self.student_details_bg_image_label.place(x=0,y=0)

        self.student_details_image = tk.PhotoImage(file='./images/student_details_img.png')
        self.student_details_image_label = tk.Label(self.student_details_frame, bd=0,image=self.student_details_image)
        self.student_details_image_label.place(x=60,y=50)


        self.studen_id_text_box = tk.Text(self.student_details_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.studen_id_text_box.place(x=260,y=65)

        self.studen_name_text_box = tk.Text(self.student_details_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.studen_name_text_box.place(x=260,y=115)

        self.studen_email_text_box = tk.Text(self.student_details_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.studen_email_text_box.place(x=260,y=165)

        self.studen_phone_text_box = tk.Text(self.student_details_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.studen_phone_text_box.place(x=260,y=215)

        self.add_student_to_db_button = ttk.Button(self.student_details_frame, text="ADD", command=self.add_to_database)
        self.add_student_to_db_button.place(x=170,y=300)

        self.cancel_button = ttk.Button(self.student_details_frame, text="CANCEL", command=self.cancel)
        self.cancel_button.place(x=260,y=300)


    def update_student_details(self):

        self.update_student_details_frame = Frame(self.root,bg="white",borderwidth=6,width=600,height=400)
        self.update_student_details_frame.place(x=40,y=140)

        self.update_student_details_bg_image = tk.PhotoImage(file='./images/student_details_bg_img.png')
        self.update_student_details_bg_image_label = tk.Label(self.update_student_details_frame, bd=0,image=self.update_student_details_bg_image)
        self.update_student_details_bg_image_label.place(x=0,y=0)




        pass



    def add_to_database(self):
        self.student_details_list =[]
        self.student_details_list.append(self.studen_id_text_box.get("1.0", "end-1c"))
        self.student_details_list.append(self.studen_name_text_box.get("1.0", "end-1c"))
        self.student_details_list.append(self.studen_email_text_box.get("1.0", "end-1c"))
        self.student_details_list.append(self.studen_phone_text_box.get("1.0", "end-1c"))
        print(self.student_details_list)

        for i in self.student_details_list:
            if len(i)==0:
                messagebox.showinfo('information', 'Field is Empty')
                return 0
        
        if self.load_to_db.flag==False:
                messagebox.showinfo('information', 'User Authentication is Pending')
                return 0
        
        self.load_to_db.load_to_postgres(tuple(self.student_details_list))

            






    def database_details(self):

        self.load_to_databse_details_bg_img = tk.PhotoImage(file='./images/load_database_details_bg_img.png')
        self.load_to_databse_details_bg_label = tk.Label(self.root, bd=0,image=self.load_to_databse_details_bg_img)
        self.load_to_databse_details_bg_label.place(x=640,y=150)


        self.load_to_database_details_frame = Frame(self.root,bg="white",borderwidth=6,width=280,height=212)
        self.load_to_database_details_frame.place(x=678,y=175)

        self.select_database_tool_var = tk.StringVar()
        self.select_database_dropdown = ttk.Combobox(self.load_to_database_details_frame, width = 26,values=['SQL SERVER','ORACLE','POSTGRES','MONGODB'], textvariable=self.select_database_tool_var)
        self.select_database_dropdown.place(x=40,y=10)
        self.select_database_tool_var.trace("w",self.check_database)

        self.authenticate_credentials_button = ttk.Button(self.root, text="Authenticate", command=self.authenticate_user)
        self.authenticate_credentials_button.place(x=740,y=420)

        self.cancel_authentication_button = ttk.Button(self.root, text="Cancel", command=self.cancel)
        self.cancel_authentication_button.place(x=840,y=420)
            


    def detect_child_frames(self,parent_frame):
        self.child_frames = []
        for child in parent_frame.winfo_children():
            if isinstance(child, tk.Frame):
                child.destroy()


    def check_database(self,*args):
        self.detect_child_frames(self.load_to_database_details_frame)
        if self.select_database_dropdown.get()=="SQL SERVER":
            self.sql_server_database_details_frame = Frame(self.load_to_database_details_frame,bg="white",borderwidth=6,width=240,height=140,name='sql_server_database_details_frame')
            self.sql_server_database_details_frame.place(x=10,y=40)

            self.label_sql_server_database_details_frame_server_name = Label(self.sql_server_database_details_frame,text = "Server",font=("Arial", 11),bg='white')
            self.label_sql_server_database_details_frame_server_name.place(x=10,y=10)

            self.text_box_sql_server_server_name = tk.Text(self.sql_server_database_details_frame,bd=0, highlightthickness=1,height = 1,width = 16)
            self.text_box_sql_server_server_name.place(x=90,y=10)

            self.label_sql_server_database_details_frame_database_name = Label(self.sql_server_database_details_frame,text = "Database",font=("Arial", 11),bg='white')
            self.label_sql_server_database_details_frame_database_name.place(x=10,y=40)
            self.text_box_sql_server_database_name = tk.Text(self.sql_server_database_details_frame,bd=0, highlightthickness=1,height = 1,width = 16)
            self.text_box_sql_server_database_name.place(x=90,y=40)

            self.label_sql_server_database_details_frame_username = Label(self.sql_server_database_details_frame,text = "user name",font=("Arial", 11),bg='white')
            self.label_sql_server_database_details_frame_username.place(x=10,y=70)
            self.text_box_sql_server_username = tk.Text(self.sql_server_database_details_frame,bd=0, highlightthickness=1,height = 1,width = 16)
            self.text_box_sql_server_username.place(x=90,y=70)

            self.label_sql_server_database_details_frame_password = Label(self.sql_server_database_details_frame,text = "password",font=("Arial", 11),bg='white')
            self.label_sql_server_database_details_frame_password.place(x=10,y=100)
            self.text_box_sql_server_password = tk.Text(self.sql_server_database_details_frame,bd=0, highlightthickness=1,height = 1,width = 16)
            self.text_box_sql_server_password.place(x=90,y=100)

        elif self.select_database_dropdown.get()=="POSTGRES":
            self.postgres_database_details_frame = Frame(self.load_to_database_details_frame,bg="white",borderwidth=6,width=240,height=160)
            self.postgres_database_details_frame.place(x=10,y=40)

            self.label_postgres_database_details_frame_hostname_name = Label(self.postgres_database_details_frame,text = "hostname",font=("Arial", 11),bg='white')
            self.label_postgres_database_details_frame_hostname_name.place(x=10,y=10)
            self.text_box_postgres_hostname = tk.Text(self.postgres_database_details_frame,bd=0, highlightthickness=1,height = 1,width = 16)
            self.text_box_postgres_hostname.place(x=90,y=10)

            self.label_postgres_database_details_frame_database_name = Label(self.postgres_database_details_frame,text = "Database",font=("Arial", 11),bg='white')
            self.label_postgres_database_details_frame_database_name.place(x=10,y=40)
            self.text_box_postgres_database_name = tk.Text(self.postgres_database_details_frame,bd=0, highlightthickness=1,height = 1,width = 16)
            self.text_box_postgres_database_name.place(x=90,y=40)

            self.label_postgres_database_details_frame_username = Label(self.postgres_database_details_frame,text = "user name",font=("Arial", 11),bg='white')
            self.label_postgres_database_details_frame_username.place(x=10,y=70)
            self.text_box_postgres_username = tk.Text(self.postgres_database_details_frame,bd=0, highlightthickness=1,height = 1,width = 16)
            self.text_box_postgres_username.place(x=90,y=70)

            self.label_postgres_database_details_frame_password = Label(self.postgres_database_details_frame,text = "password",font=("Arial", 11),bg='white')
            self.label_postgres_database_details_frame_password.place(x=10,y=100)
            self.text_box_postgres_password = tk.Text(self.postgres_database_details_frame,bd=0, highlightthickness=1,height = 1,width = 16)
            self.text_box_postgres_password.place(x=90,y=100)

            # self.label_postgres_database_details_frame_port = Label(self.postgres_database_details_frame,text = "port",font=("Arial", 11),bg='white')
            # self.label_postgres_database_details_frame_port.place(x=10,y=130)
            # self.text_box_postgres_port = tk.Text(self.postgres_database_details_frame,bd=0, highlightthickness=1,height = 1,width = 16)
            # self.text_box_postgres_port.place(x=90,y=130)


        elif self.select_database_dropdown.get()=="ORACLE":
            self.oracle_database_details_frame = Frame(self.load_to_database_details_frame,bg="white",borderwidth=6,width=240,height=160)
            self.oracle_database_details_frame.place(x=10,y=40)

            self.label_oracle_database_details_frame_hostname_name = Label(self.oracle_database_details_frame,text = "hostname",font=("Arial", 11),bg='white')
            self.label_oracle_database_details_frame_hostname_name.place(x=10,y=10)
            self.text_box_oracle_hostname = tk.Text(self.oracle_database_details_frame,bd=0, highlightthickness=1,height = 1,width = 16)
            self.text_box_oracle_hostname.place(x=90,y=10)

            self.label_oracle_database_details_frame_username = Label(self.oracle_database_details_frame,text = "user name",font=("Arial", 11),bg='white')
            self.label_oracle_database_details_frame_username.place(x=10,y=40)
            self.text_box_oracle_username = tk.Text(self.oracle_database_details_frame,bd=0, highlightthickness=1,height = 1,width = 16)
            self.text_box_oracle_username.place(x=90,y=40)

            self.label_oracle_database_details_frame_password = Label(self.oracle_database_details_frame,text = "password",font=("Arial", 11),bg='white')
            self.label_oracle_database_details_frame_password.place(x=10,y=70)
            self.text_box_oracle_password = tk.Text(self.oracle_database_details_frame,bd=0, highlightthickness=1,height = 1,width = 16)
            self.text_box_oracle_password.place(x=90,y=70)

            self.label_oracle_database_details_frame_port = Label(self.oracle_database_details_frame,text = "port",font=("Arial", 11),bg='white')
            self.label_oracle_database_details_frame_port.place(x=10,y=100)
            self.text_box_oracle_port = tk.Text(self.oracle_database_details_frame,bd=0, highlightthickness=1,height = 1,width = 16)
            self.text_box_oracle_port.place(x=90,y=100)

            self.label_oracle_database_details_frame_sid = Label(self.oracle_database_details_frame,text = "sid",font=("Arial", 11),bg='white')
            self.label_oracle_database_details_frame_sid.place(x=10,y=130)
            self.text_box_oracle_sid = tk.Text(self.oracle_database_details_frame,bd=0, highlightthickness=1,height = 1,width = 16)
            self.text_box_oracle_sid.place(x=90,y=130)



        elif self.select_database_dropdown.get()=="MONGODB":
            self.mongo_database_details_frame = Frame(self.load_to_database_details_frame,bg="white",borderwidth=6,width=250,height=160)
            self.mongo_database_details_frame.place(x=10,y=40)

            self.label_mongo_database_details_frame_conn_string = Label(self.mongo_database_details_frame,text = "connection string",font=("Arial", 10),bg='white')
            self.label_mongo_database_details_frame_conn_string.place(x=0,y=10)
            self.text_box_mongo_conn_string = tk.Text(self.mongo_database_details_frame,bd=0, highlightthickness=1,height = 1,width = 16)
            self.text_box_mongo_conn_string.place(x=105,y=10)

            self.label_mongo_database_details_frame_database_name = Label(self.mongo_database_details_frame,text = "database",font=("Arial", 10),bg='white')
            self.label_mongo_database_details_frame_database_name.place(x=0,y=40)
            self.text_box_mongo_database_name = tk.Text(self.mongo_database_details_frame,bd=0, highlightthickness=1,height = 1,width = 16)
            self.text_box_mongo_database_name.place(x=105,y=40)

            self.label_mongo_database_details_frame_collection_name = Label(self.mongo_database_details_frame,text = "collection",font=("Arial", 10),bg='white')
            self.label_mongo_database_details_frame_collection_name.place(x=0,y=70)
            self.text_box_mongo_collection_name = tk.Text(self.mongo_database_details_frame,bd=0, highlightthickness=1,height = 1,width = 16)
            self.text_box_mongo_collection_name.place(x=105,y=70)
    

    def authenticate_user(self):
        self.database_tool_name = self.select_database_dropdown.get()
        if self.database_tool_name=="SQL SERVER":
            self.sql_server_server_name = self.text_box_sql_server_server_name.get(1.0, "end-1c")
            self.sql_server_database_name = self.text_box_sql_server_database_name.get(1.0, "end-1c")
            self.sql_server_username = self.text_box_sql_server_username.get(1.0, "end-1c")
            self.sql_server_password = self.text_box_sql_server_password.get(1.0, "end-1c")
            self.load_to_db.connect_to_sql_server(self.sql_server_server_name,self.sql_server_database_name,self.sql_server_username,self.sql_server_password)

        elif self.database_tool_name=="POSTGRES":
            self.postgres_hostname = self.text_box_postgres_hostname.get(1.0, "end-1c")
            self.postgres_database_name = self.text_box_postgres_database_name.get(1.0, "end-1c")
            self.postgres_username = self.text_box_postgres_username.get(1.0, "end-1c")
            self.postgres_password = self.text_box_postgres_password.get(1.0, "end-1c")
            self.postgres_port = self.text_box_postgres_port.get(1.0, "end-1c")
            self.load_to_db.connect_to_postgres(self.postgres_hostname,self.postgres_database_name,self.postgres_username,self.postgres_password)




        print(self.load_to_db.flag)
        if self.load_to_db.flag:
            self.authentication_success_image = tk.PhotoImage(file='./images/Auth_success.png')
            self.authentication_success_image_label = tk.Label(self.root, bd=0,image=self.authentication_success_image)
            self.authentication_success_image_label.place(x=660,y=460)
        else:
            self.authentication_failed_image = tk.PhotoImage(file='./images/Auth_failed.png')
            self.authentication_failed_image_label = tk.Label(self.root, bd=0,image=self.authentication_failed_image)
            self.authentication_failed_image_label.place(x=660,y=460)




    def cancel(self):
        self.student_details_frame.destroy()

    

app_instance = Student_Details()
app_instance.mainloop()









        
