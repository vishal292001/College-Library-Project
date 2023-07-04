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
        self.update_student_button = ttk.Button(self.root, text="update student",image=self.update_student_button_image,command=self.update_student_details_window)
        self.update_student_button.place(x=260,y=50)


        self.delete_student_button_image = Image.open("./images/delete_student_button_img.png")
        self.delete_student_button_image = self.delete_student_button_image.resize((140, 60))
        self.delete_student_button_image = ImageTk.PhotoImage(self.delete_student_button_image)
        self.delete_student_button = ttk.Button(self.root, text="delete student",image=self.delete_student_button_image,command=self.delete_student_window)
        self.delete_student_button.place(x=420,y=50)

        
        self.authenticate_button_image = Image.open("./images/Authenticate_user_img.png")
        self.authenticate_button_image = self.authenticate_button_image.resize((140, 60))
        self.authenticate_button_image = ImageTk.PhotoImage(self.authenticate_button_image)
        self.authenticate_button = ttk.Button(self.root, text="Aithenticate",image=self.authenticate_button_image,command=self.database_details)
        self.authenticate_button.place(x=730,y=50)




        

        pass

    def add_new_student_frame(self):
        self.check_and_destroy_frame(self.root)
        self.student_details_frame = Frame(self.root,bg="white",borderwidth=6,width=600,height=400,name='add_student_frame')
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


    def check_and_destroy_frame(self,root):
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):
                if child.winfo_name() in ['add_student_frame','update_student_frame']:
                    child.destroy()


    def update_student_details_window(self):
        self.check_and_destroy_frame(self.root)
        self.update_student_details_frame = Frame(self.root,bg="white",borderwidth=6,width=600,height=400)
        self.update_student_details_frame.place(x=40,y=140)

        self.update_student_details_bg_image = tk.PhotoImage(file='./images/student_details_bg_img.png')
        self.update_student_details_bg_image_label = tk.Label(self.update_student_details_frame, bd=0,image=self.update_student_details_bg_image)
        self.update_student_details_bg_image_label.place(x=0,y=0)


        self.enter_student_id_img = tk.PhotoImage(file='./images/enter_student_id_img.png')
        self.enter_student_id_img_label = tk.Label(self.update_student_details_frame, bd=0,image=self.enter_student_id_img)
        self.enter_student_id_img_label.place(x=40,y=65)

        self.enter_studen_id_text_box = tk.Text(self.update_student_details_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.enter_studen_id_text_box.place(x=210,y=75)


        self.search_student_img = Image.open("./images/search_img.png")
        self.search_student_img = self.search_student_img.resize((70, 40))
        self.search_student_img = ImageTk.PhotoImage(self.search_student_img)
        self.search_student_button = ttk.Button(self.update_student_details_frame,text="search student",image=self.search_student_img,command=lambda:self.search_student_in_database('update'))
        self.search_student_button.place(x=440,y=60)




        pass

    def delete_student_window(self):
        self.check_and_destroy_frame(self.root)
        self.delete_student_frame = Frame(self.root,bg="white",borderwidth=6,width=600,height=400)
        self.delete_student_frame.place(x=40,y=140)

        self.delete_student_bg_image = tk.PhotoImage(file='./images/student_details_bg_img.png')
        self.delete_student_bg_image_label = tk.Label(self.delete_student_frame, bd=0,image=self.delete_student_bg_image)
        self.delete_student_bg_image_label.place(x=0,y=0)


        self.enter_student_id_img = tk.PhotoImage(file='./images/enter_student_id_img.png')
        self.enter_student_id_img_label = tk.Label(self.delete_student_frame, bd=0,image=self.enter_student_id_img)
        self.enter_student_id_img_label.place(x=40,y=65)

        self.enter_studen_id_text_box = tk.Text(self.delete_student_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.enter_studen_id_text_box.place(x=210,y=75)


        self.search_student_img_in_delete_win = Image.open("./images/search_img.png")
        self.search_student_img_in_delete_win = self.search_student_img_in_delete_win.resize((70, 40))
        self.search_student_img_in_delete_win = ImageTk.PhotoImage(self.search_student_img_in_delete_win)
        self.search_student_button_in_delete_win = ttk.Button(self.delete_student_frame,text="search student",image=self.search_student_img_in_delete_win,command=lambda:self.search_student_in_database('delete'))
        self.search_student_button_in_delete_win.place(x=440,y=60)




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
        self.select_database_dropdown = ttk.Combobox(self.load_to_database_details_frame, width = 26,values=['POSTGRES','MONGODB'], textvariable=self.select_database_tool_var)
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

        if self.select_database_dropdown.get()=="POSTGRES":
            self.postgres_database_details_frame = Frame(self.load_to_database_details_frame,bg="white",borderwidth=6,width=240,height=160)
            self.postgres_database_details_frame.place(x=10,y=40)

            # self.label_postgres_database_details_frame_hostname_name = Label(self.postgres_database_details_frame,text = "hostname",font=("Arial", 11),bg='white')
            # self.label_postgres_database_details_frame_hostname_name.place(x=10,y=10)
            # self.text_box_postgres_hostname = tk.Text(self.postgres_database_details_frame,bd=0, highlightthickness=1,height = 1,width = 16)
            # self.text_box_postgres_hostname.place(x=90,y=10)

            # self.label_postgres_database_details_frame_database_name = Label(self.postgres_database_details_frame,text = "Database",font=("Arial", 11),bg='white')
            # self.label_postgres_database_details_frame_database_name.place(x=10,y=40)
            # self.text_box_postgres_database_name = tk.Text(self.postgres_database_details_frame,bd=0, highlightthickness=1,height = 1,width = 16)
            # self.text_box_postgres_database_name.place(x=90,y=40)

            self.label_postgres_database_details_frame_username = Label(self.postgres_database_details_frame,text = "user name",font=("Arial", 11),bg='white')
            self.label_postgres_database_details_frame_username.place(x=10,y=70)
            self.text_box_postgres_username = tk.Text(self.postgres_database_details_frame,bd=0, highlightthickness=1,height = 1,width = 16)
            self.text_box_postgres_username.place(x=90,y=70)

            self.label_postgres_database_details_frame_password = Label(self.postgres_database_details_frame,text = "password",font=("Arial", 11),bg='white')
            self.label_postgres_database_details_frame_password.place(x=10,y=100)
            self.text_box_postgres_password = tk.Text(self.postgres_database_details_frame,bd=0, highlightthickness=1,height = 1,width = 16)
            self.text_box_postgres_password.place(x=90,y=100)




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
        
        if self.database_tool_name=="POSTGRES":
        # self.postgres_hostname = self.text_box_postgres_hostname.get(1.0, "end-1c")
        # self.postgres_database_name = self.text_box_postgres_database_name.get(1.0, "end-1c")
            self.postgres_username = self.text_box_postgres_username.get(1.0, "end-1c")
            self.postgres_password = self.text_box_postgres_password.get(1.0, "end-1c")
            self.load_to_db.connect_to_postgres('localhost','Library',self.postgres_username,self.postgres_password)


        print(self.load_to_db.flag)
        if self.load_to_db.flag:
            self.authentication_success_image = tk.PhotoImage(file='./images/Auth_success.png')
            self.authentication_success_image_label = tk.Label(self.root, bd=0,image=self.authentication_success_image)
            self.authentication_success_image_label.place(x=660,y=460)
        else:
            self.authentication_failed_image = tk.PhotoImage(file='./images/Auth_failed.png')
            self.authentication_failed_image_label = tk.Label(self.root, bd=0,image=self.authentication_failed_image)
            self.authentication_failed_image_label.place(x=660,y=460)




    def search_student_in_database(self,operation):

        if self.load_to_db.flag==False:
            messagebox.showinfo('information', 'User Authentication is Pending')
            return 0
        self.student_id = int(self.enter_studen_id_text_box.get(1.0, "end-1c"))
        self.df = self.load_to_db.search_in_database()
        print(self.df)
        self.student_id_list = list(self.df['student_id'])

        if operation=='update':
            self.frame = self.update_student_details_frame
        if operation=='delete':
            self.frame=self.delete_student_frame
        self.student_details_image_opration = tk.PhotoImage(file='./images/update_student_img.png')
        self.student_details_image_opration_label = tk.Label(self.frame, bd=0,image=self.student_details_image_opration)
        self.student_details_image_opration_label.place(x=40,y=140)

        self.student_name_text_box = tk.Text(self.frame,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.student_name_text_box.place(x=210,y=150)

        self.student_email_text_box = tk.Text(self.frame,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.student_email_text_box.place(x=210,y=200)

        self.student_phone_text_box = tk.Text(self.frame,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.student_phone_text_box.place(x=210,y=250)


        if self.student_id in self.student_id_list:
            self.row_index = self.student_id_list.index(self.student_id)
            self.row = self.df.loc[self.row_index]

            self.student_name_text_box.insert(tk.END,self.row['student_name'])
            self.student_email_text_box.insert(tk.END,self.row['student_email'])
            self.student_phone_text_box.insert(tk.END,self.row['student_phone'])

            if operation=='update':
                self.student_to_db_button = ttk.Button(self.frame, text="Update",command=self.update_student_details)
                self.student_to_db_button.place(x=190,y=300)

                self.cancel_update_button = ttk.Button(self.frame, text="Cancel",command=self.close_update_student_details_window)
                self.cancel_update_button.place(x=280,y=300)
            if operation=='delete':
                self.student_to_db_button = ttk.Button(self.frame, text="Delete",command=self.delete_student)
                self.student_to_db_button.place(x=190,y=300)

                self.cancel_update_button = ttk.Button(self.frame, text="Cancel",command=self.close_delete_student_details_window)
                self.cancel_update_button.place(x=280,y=300)


        else:
             messagebox.showinfo('information', 'Student not found')
             print("student is not found")






    def update_student_details(self):

        self.student_name = self.student_name_text_box.get("1.0", "end-1c")
        self.student_email = self.student_email_text_box.get("1.0", "end-1c")
        self.student_phone = self.student_phone_text_box.get("1.0", "end-1c")
        self.load_to_db.update_data_in_database(self.student_id,self.student_name,self.student_email,self.student_phone)

    def delete_student(self):
        self.load_to_db.delete_record_in_database(self.student_id)


    def cancel(self):
        self.student_details_frame.destroy()

    def close_update_student_details_window(self):
        self.update_student_details_frame.destroy()

    def close_delete_student_details_window(self):
        self.delete_student_frame.destroy()
    

app_instance = Student_Details()
app_instance.mainloop()









        
