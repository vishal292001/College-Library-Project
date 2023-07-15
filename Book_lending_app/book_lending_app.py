import tkinter as tk
from tkinter import *
from tkinter import ttk
# from tkinter.ttk import *
from tkinter import Button

from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
from tkcalendar import Calendar
from tkcalendar import DateEntry

import urllib
import pandas as pd
import json
import pyodbc
import duckdb
import database_loaders
import add_new_student_window
import update_student_details_window
import delete_student_window
import add_new_book_window
import update_book_details_window
import delete_book_window
import book_lending_window
import update_lended_book_window
import delete_lended_book_window



class Book_lending_app():
    def __init__(self):
        self.root = Tk()
        self.root.title("Book Lending App")
        self.root.geometry('1150x700')
        self.root.configure(bg='white')

        self.add_baground_images()

       
        self.status_message_label = tk.Label(self.root, bd=0,text="",font=("Arial Bold", 9),fg="green",bg='white')
        self.status_message_label.place(x=382,y=75)
        self.load_to_db = database_loaders.Load_to_Database()
        self.add_new_student=add_new_student_window.add_new_student_in_database(self.root,self.load_to_db,self.status_message_label)
        self.update_student_details=update_student_details_window.update_student_details_window(self.root,self.load_to_db,self.status_message_label)
        self.delete_student=delete_student_window.delete_student_window(self.root,self.load_to_db,self.status_message_label)
        self.add_new_book = add_new_book_window.add_new_book_window(self.root,self.load_to_db,self.status_message_label)
        self.update_book_details = update_book_details_window.update_book_details_window(self.root,self.load_to_db,self.status_message_label)
        self.delete_book = delete_book_window.delete_book_window(self.root,self.load_to_db,self.status_message_label)
        self.lend_book = book_lending_window.book_lending_window(self.root,self.load_to_db,self.status_message_label)
        self.update_lended_book = update_lended_book_window.update_lended_book_window(self.root,self.load_to_db,self.status_message_label)
        self.delete_lended_book = delete_lended_book_window.delete_lended_book_window(self.root,self.load_to_db,self.status_message_label)


        self.add_buttons()
        self.add_user_inputs()

 

        self.diaplay_book_name_label_y_pos = 120

        self.student_table_name='student_details'
        self.book_table_name='books_details'
        self.book_lending_table_name = 'book_lending_details'
        
        self.total_book = tk.Label(text="", font=("Arial Bold", 11), fg="green", bg="white")
        self.total_book.place(x=900, y=178)
  
        self.total_student = tk.Label(text="", font=("Arial Bold", 11), fg="green", bg="white")
        self.total_student.place(x=1024, y=178)

        self.total_lended_books = tk.Label(text="", font=("Arial Bold", 11), fg="green", bg="white")
        self.total_lended_books.place(x=900, y=273)

        
        self.total_books_to_return = tk.Label(text="", font=("Arial Bold", 11), fg="green", bg="white")
        self.total_books_to_return.place(x=1024, y=273)




    
    def mainloop(self):
        self.root.mainloop()



    def update_analytics_count(self):
        book_count = self.load_to_db.get_book_details_count()
        student_count = self.load_to_db.get_student_details_count()
        total_lended_books_count = self.load_to_db.book_lend_details_count()
        total_book_to_return_count = self.load_to_db.get_return_dates_count()

        self.total_book.config(text=str(book_count))
        self.total_student.config(text=str(student_count))
        self.total_lended_books.config(text=str(total_lended_books_count))
        self.total_books_to_return.config(text=str(total_book_to_return_count))
        self.total_book.after(500,self.update_analytics_count)

    def add_baground_images(self):
        self.app_icon_img = tk.PhotoImage(file='./images/app_icon.png')
        self.app_icon_img_label = tk.Label(self.root, bd=0,image=self.app_icon_img)
        self.app_icon_img_label.place(x=0,y=-10)

        self.app_icon_img_plus = tk.PhotoImage(file='./images/app_icon_1.png')
        self.app_icon_img_label_plus = tk.Label(self.root, bd=0,image=self.app_icon_img_plus)
        self.app_icon_img_label_plus.place(x=600,y=-10)

        self.status_image = tk.PhotoImage(file='./images/status_bg_image.png')
        self.status_image_label = tk.Label(self.root, bd=0,image=self.status_image)
        self.status_image_label.place(x=260,y=60)

        self.buttons_bg_image_student = tk.PhotoImage(file='./images/button_white_bg_image.png')
        self.buttons_bg_image_student_label = tk.Label(self.root, bd=0,image=self.buttons_bg_image_student)
        self.buttons_bg_image_student_label.place(x=10,y=48)

        self.buttons_bg_image_book = tk.PhotoImage(file='./images/button_white_bg_image.png')
        self.buttons_bg_image_book_label = tk.Label(self.root, bd=0,image=self.buttons_bg_image_book)
        self.buttons_bg_image_book_label.place(x=10,y=245)

        self.buttons_bg_image_lend_book = tk.PhotoImage(file='./images/button_white_bg_image.png')
        self.buttons_bg_image_lend_book_label = tk.Label(self.root, bd=0,image=self.buttons_bg_image_lend_book)
        self.buttons_bg_image_lend_book_label.place(x=10,y=445)

        self.close_icon_img = Image.open("./images/close_icon.png")
        self.close_icon_img = self.close_icon_img.resize((20, 20))
        self.close_icon_img = ImageTk.PhotoImage(self.close_icon_img)
 
        self.search_icon_img = Image.open("./images/search_icon.png")
        self.search_icon_img = self.search_icon_img.resize((40, 40))
        self.search_icon_img = ImageTk.PhotoImage(self.search_icon_img)

        self.enter_student_id_image_lend_win = Image.open("./images/enter_student_id_img.png")
        self.enter_student_id_image_lend_win = self.enter_student_id_image_lend_win.resize((120, 50))
        self.enter_student_id_image_lend_win = ImageTk.PhotoImage(self.enter_student_id_image_lend_win)
 
        self.enter_book_code_image_lend_win = Image.open("./images/enter_book_code_img.png")
        self.enter_book_code_image_lend_win = self.enter_book_code_image_lend_win.resize((120, 50))
        self.enter_book_code_image_lend_win = ImageTk.PhotoImage(self.enter_book_code_image_lend_win)

        self.load_to_databse_details_bg_img = tk.PhotoImage(file='./images/load_database_details_bg_img.png')
        self.load_to_databse_details_bg_label = tk.Label(self.root, bd=0,image=self.load_to_databse_details_bg_img)
        self.load_to_databse_details_bg_label.place(x=820,y=400)


        self.analytics_bg_img = tk.PhotoImage(file='./images/analytics_bg_img.png')
        self.analytics_bg_img_label = tk.Label(self.root, bd=0,image=self.analytics_bg_img)
        self.analytics_bg_img_label.place(x=825,y=50)

        self.analytics_window_img = tk.PhotoImage(file='./images/analytics_window.png')
        self.analytics_window_img_label = tk.Label(self.root, bd=0,image=self.analytics_window_img)
        self.analytics_window_img_label.place(x=850,y=74)

        pass

    def add_buttons(self):
        self.add_new_student_button_image = Image.open("./images/add_new_student_img_light_blue.png")
        self.add_new_student_button_image = ImageTk.PhotoImage(self.add_new_student_button_image)
        self.add_new_student_button = Button(self.root,image=self.add_new_student_button_image,borderwidth=0,background='white',command=self.add_new_student.add_new_student_window)
        self.add_new_student_button.place(x=32,y=80)

        self.update_student_details_image = Image.open("./images/update_student_img_light_blue.png")
        self.update_student_details_image = ImageTk.PhotoImage(self.update_student_details_image)
        self.update_student_details_button = Button(self.root,image=self.update_student_details_image,borderwidth=0,background='white',command=self.update_student_details.update_student_details)
        self.update_student_details_button.place(x=32,y=130)

        self.delete_student_image = Image.open("./images/delete_student_img_light_blue.png")
        self.delete_student_image = ImageTk.PhotoImage(self.delete_student_image)
        self.delete_student_button = Button(self.root,image=self.delete_student_image,borderwidth=0,background='white',command=self.delete_student.delete_student_record)
        self.delete_student_button.place(x=32,y=175)

        self.add_new_book_button_image = Image.open("./images/add_new_book_img.png")
        self.add_new_book_button_image = ImageTk.PhotoImage(self.add_new_book_button_image)
        self.add_new_book_button = Button(self.root,image=self.add_new_book_button_image,borderwidth=0,background='white',command=self.add_new_book.add_new_book_in_database)
        self.add_new_book_button.place(x=32,y=270)

        self.update_book_button_image = Image.open("./images/update_book_img.png")
        self.update_book_button_image = ImageTk.PhotoImage(self.update_book_button_image)
        self.update_book_button = Button(self.root,image=self.update_book_button_image,borderwidth=0,background='white',command=self.update_book_details.update_book_details)
        self.update_book_button.place(x=32,y=320)

        self.delete_book_button_image = Image.open("./images/delete_book_img.png")
        self.delete_book_button_image = ImageTk.PhotoImage(self.delete_book_button_image)
        self.delete_book_button = Button(self.root,image=self.delete_book_button_image,borderwidth=0,background='white',command=self.delete_book.delete_book_record)
        self.delete_book_button.place(x=32,y=370)


        self.lend_book_button_image = Image.open("./images/lend_book_img_green_1.png")
        self.lend_book_button_image = ImageTk.PhotoImage(self.lend_book_button_image)
        self.lend_book_button = Button(self.root,image=self.lend_book_button_image,borderwidth=0,background='white',command=self.lend_book.lend_book_from_library)
        self.lend_book_button.place(x=32,y=470)

        self.update_student_book_button_image = Image.open("./images/update_student_book_img_green_1.png")
        self.update_student_book_button_image = ImageTk.PhotoImage(self.update_student_book_button_image)
        self.update_student_book_button = Button(self.root,image=self.update_student_book_button_image,borderwidth=0,background='white',command=self.update_lended_book.update_lended_book)
        self.update_student_book_button.place(x=32,y=520)

        self.delete_student_book_button_image = Image.open("./images/delete_student_book_img_green_1.png")
        self.delete_student_book_button_image = ImageTk.PhotoImage(self.delete_student_book_button_image)
        self.delete_student_book_button = Button(self.root,image=self.delete_student_book_button_image,borderwidth=0,background='white',command=self.delete_lended_book.delete_lended_book)
        self.delete_student_book_button.place(x=32,y=570)

        self.authenticate_button_image = Image.open("./images/authenticate_user.png")
        self.authenticate_button_image = self.authenticate_button_image.resize((200, 50))
        self.authenticate_button_image = ImageTk.PhotoImage(self.authenticate_button_image)
        self.authenticate_button = Button(self.root, text="Aithenticate",image=self.authenticate_button_image,borderwidth=0,background='white')
        self.authenticate_button.place(x=880,y=348)

    def add_user_inputs(self):
        self.select_database_tool_var = tk.StringVar()
        self.select_database_dropdown = ttk.Combobox(self.root, width = 26,values=['POSTGRES','MONGODB'], textvariable=self.select_database_tool_var)
        self.select_database_dropdown.place(x=880,y=440)
        # self.select_database_tool_var.trace("w",self.check_database)

        self.label_postgres_database_details_frame_username = Label(self.root,text = "user name",font=("Arial Bold", 11),bg='white',fg='#2e75b6')
        self.label_postgres_database_details_frame_username.place(x=860,y=490)
        self.text_box_postgres_username = tk.Text(self.root,bd=0, highlightthickness=1,height = 1,width = 16)
        self.text_box_postgres_username.place(x=940,y=490)

        self.label_postgres_database_details_frame_password = Label(self.root,text = "password",font=("Arial Bold", 11),bg='white',fg='#2e75b6')
        self.label_postgres_database_details_frame_password.place(x=860,y=520)
        self.text_box_postgres_password = tk.Entry(self.root,bd=0, highlightthickness=1,width = 21,show="*")
        self.text_box_postgres_password.place(x=940,y=520)

        self.authenticate_credentials_button = ttk.Button(self.root, text="Authenticate",command=self.authenticate_user)
        self.authenticate_credentials_button.place(x=900,y=580)

        self.cancel_authentication_button = ttk.Button(self.root, text="Cancel")
        self.cancel_authentication_button.place(x=985,y=580)


    def authenticate_user(self):
        self.database_tool_name = self.select_database_dropdown.get()
        if self.database_tool_name=="POSTGRES":
            self.postgres_username = self.text_box_postgres_username.get(1.0, "end-1c")
            self.postgres_password = self.text_box_postgres_password.get()
            self.load_to_db.connect_to_postgres('localhost','Library',self.postgres_username,self.postgres_password)

        if self.load_to_db.flag:
            self.status_message_label.config(text="Authentication Successful",fg='green')
            self.update_analytics_count()
        else:
            self.status_message_label.config(text="Authentication Failed",fg='red')




 


    def lend_book_window(self):
        if self.load_to_db.flag==False:
            messagebox.showinfo('information', 'User Authentication is Pending')
            return 0
        self.check_and_destroy_frame(self.root)

        self.selected_book_list = []
        self.diaplay_book_name_label_lst=[]
        self.close_book_name_label_button_lst =[]
        self.selected_student_to_lend_book_lst = []

        self.dataframe = self.load_to_db.search_in_database(self.student_table_name)
        self.student_name_lst_in_database=list(self.dataframe['student_name'])
        self.student_id_lst_in_database=list(self.dataframe['student_id'])

        self.book_data_dataframe = self.load_to_db.search_in_database(self.book_table_name)
        self.book_title_lst_in_database = list(self.book_data_dataframe['book_title'])
        self.book_code_lst_in_database = list(self.book_data_dataframe['book_code'])

        self.lend_book_frame = Frame(self.root,bg="white",borderwidth=6,width=500,height=500,name='lend_book_frame',highlightbackground="black",highlightthickness=2)
        self.lend_book_frame.place(x=260,y=140)

        self.sub_frame = Frame(self.lend_book_frame,bg="white",borderwidth=6,width=500,height=50,highlightbackground="black",highlightthickness=2)
        self.sub_frame.place(x=-8,y=442)

        self.enter_student_id_image_label = tk.Label(self.lend_book_frame, bd=0,image=self.enter_student_id_image_lend_win)
        self.enter_student_id_image_label.place(x=10,y=20)

        self.student_id_combobox_var = tk.StringVar()
        self.student_id_combobox = ttk.Combobox(self.lend_book_frame, width = 24,values=self.student_name_lst_in_database, textvariable=self.student_id_combobox_var)
        self.student_id_combobox.place(x=12,y=75)

        self.search_button_student = Button(self.lend_book_frame,image=self.search_icon_img,borderwidth=0,background='white',command=lambda:self.find_student_to_lend_book(self.lend_book_frame))
        self.search_button_student.place(x=140,y=22)

                
        self.enter_book_code_image_label = tk.Label(self.lend_book_frame, bd=0,image=self.enter_book_code_image_lend_win)
        self.enter_book_code_image_label.place(x=295,y=20)
        
        self.search_button_book = Button(self.lend_book_frame,image=self.search_icon_img,borderwidth=0,background='white',command=lambda:self.find_book_to_lend(self.lend_book_frame))
        self.search_button_book.place(x=420,y=22)

        self.book_code_combobox_var = tk.StringVar()
        self.book_code_combobox = ttk.Combobox(self.lend_book_frame, width = 24,values=self.book_title_lst_in_database, textvariable=self.book_code_combobox_var)
        self.book_code_combobox.place(x=295,y=75)


        self.from_date_calender=DateEntry(self.lend_book_frame,selectmode='day')
        self.from_date_calender.place(x=10,y=190)
        self.from_date_label = tk.Label(self.lend_book_frame, text="From Date",font=("Arial Bold", 11),fg="#2f5597",bg='white')
        self.from_date_label.place(x=110,y=190)

        self.to_date_calender=DateEntry(self.lend_book_frame,selectmode='day')
        self.to_date_calender.place(x=10,y=216)
        self.to_date_label = tk.Label(self.lend_book_frame, text="Return Date",font=("Arial Bold", 11),fg="#2f5597",bg='white')
        self.to_date_label.place(x=110,y=216)


        self.allot_book_button = ttk.Button(self.lend_book_frame, text="Allot Book",command=self.allot_book_to_student)
        self.allot_book_button.place(x=140,y=456)

        self.allot_book_cancel_button = ttk.Button(self.lend_book_frame, text="Cancel")
        self.allot_book_cancel_button.place(x=220,y=456)
        pass

    def update_student_book_window(self):

        if self.load_to_db.flag==False:
            messagebox.showinfo('information', 'User Authentication is Pending')
            return 0
        self.check_and_destroy_frame(self.root)

        self.selected_student_to_lend_book_lst = []
        self.dataframe = self.load_to_db.search_in_database(self.book_lending_table_name)
        self.student_name_lst_in_database=list(self.dataframe['student_name'])
        self.student_id_lst_in_database=list(self.dataframe['student_id'])

        self.filter_student_name_list = []
        [self.filter_student_name_list.append(x) for x in self.student_name_lst_in_database if x not in self.filter_student_name_list]

        self.update_student_book_frame = Frame(self.root,bg="white",borderwidth=6,width=500,height=400,name='update_student_book_frame',highlightbackground="black",highlightthickness=2)
        self.update_student_book_frame.place(x=260,y=140)

        self.enter_student_id_image_label = tk.Label(self.update_student_book_frame, bd=0,image=self.enter_student_id_image_lend_win)
        self.enter_student_id_image_label.place(x=10,y=20)

        self.student_id_combobox_var = tk.StringVar()
        self.student_id_combobox = ttk.Combobox(self.update_student_book_frame, width = 24,values=self.filter_student_name_list, textvariable=self.student_id_combobox_var)
        self.student_id_combobox.place(x=12,y=75)

        self.search_button_student = Button(self.update_student_book_frame,image=self.search_icon_img,borderwidth=0,background='white',command=lambda:self.find_student_to_lend_book(self.update_student_book_frame))
        self.search_button_student.place(x=140,y=22)

        self.enter_book_code_image_label = tk.Label(self.update_student_book_frame, bd=0,image=self.enter_book_code_image_lend_win)
        self.enter_book_code_image_label.place(x=295,y=20)
        
        self.search_button_book = Button(self.update_student_book_frame,image=self.search_icon_img,borderwidth=0,background='white',command=lambda:self.find_book_to_lend(self.update_student_book_frame))
        self.search_button_book.place(x=420,y=22)

        self.book_code_combobox_var = tk.StringVar()
        self.book_code_combobox = ttk.Combobox(self.update_student_book_frame, width = 24,values=['The Great Gatsby','Pride and Prejudice','Discovery of India','Harry Potter'], textvariable=self.book_code_combobox_var)
        self.book_code_combobox.place(x=295,y=75)

        self.update_student_book_button = ttk.Button(self.update_student_book_frame, text="update")
        self.update_student_book_button.place(x=140,y=350)

        self.cancel_Update_student_book_button = ttk.Button(self.update_student_book_frame, text="Cancel")
        self.cancel_Update_student_book_button.place(x=220,y=350)
        pass

    def find_student_to_lend_book(self,frame):
        self.frame = frame
        self.user_input = self.student_id_combobox.get()
        if self.user_input in self.student_name_lst_in_database or self.user_input in self.student_id_lst_in_database:
             if self.user_input in self.student_name_lst_in_database:
                 self.index_no = self.student_name_lst_in_database.index(self.user_input)
                 self.row_data = self.dataframe.loc[self.index_no]
                 self.user_input_id = self.row_data['student_id']
                 self.user_input=self.user_input
                 pass
             elif self.user_input in self.student_id_lst_in_database:
                 self.index_no = self.student_id_lst_in_database.index(self.user_input)
                 self.row_data = self.dataframe.loc[self.index_no]
                 self.user_input_id = self.user_input
                 self.user_input=self.row_data['student_name']

             pass
        else:
             messagebox.showinfo('information', 'Student not found')
             return 0


        if len(self.selected_student_to_lend_book_lst)>0:
            for i in self.selected_student_to_lend_book_lst:
                i.destroy()
            for j in self.selected_student_to_lend_book_lst:
                self.selected_student_to_lend_book_lst.pop()
                self.selected_student_to_lend_book_lst.pop()
                self.selected_student_to_lend_book_lst.pop()
                self.selected_student_to_lend_book_lst.pop()

        if len(self.selected_student_to_lend_book_lst)==0:
            self.diaplay_id_label = tk.Label(self.frame, text="Student ID:"+self.user_input_id,font=("Arial Bold", 11),fg="#2f5597",bg='white',borderwidth=1, relief="solid",width=18)
            self.diaplay_id_label.place(x=12,y=110)
    
            self.close_student_id_label_button = Button(self.frame,image=self.close_icon_img,borderwidth=0,background='white',command=self.remove_selected_student)
            self.close_student_id_label_button.place(x=180,y=110)

            self.diaplay_student_name_label = tk.Label(self.frame, text=self.user_input,font=("Arial Bold", 11),fg="#2f5597",bg='white',borderwidth=1, relief="solid",width=18)
            self.diaplay_student_name_label.place(x=12,y=140)

            self.close_student_name_label_button = Button(self.frame,image=self.close_icon_img,borderwidth=0,background='white',command=self.remove_selected_student)
            self.close_student_name_label_button.place(x=180,y=140)

            self.selected_student_to_lend_book_lst.append(self.diaplay_student_name_label)
            self.selected_student_to_lend_book_lst.append(self.close_student_name_label_button)
            self.selected_student_to_lend_book_lst.append(self.diaplay_id_label)
            self.selected_student_to_lend_book_lst.append(self.close_student_id_label_button)

            if self.frame.winfo_name()=='update_student_book_frame':
                self.diplay_previously_alloted_book(self.frame)
           
        pass

    def remove_selected_student(self):
        self.diaplay_student_name_label.destroy()
        self.close_student_name_label_button.destroy()
        self.diaplay_id_label.destroy()
        self.close_student_id_label_button.destroy()
        self.selected_student_to_lend_book_lst=[]

    def find_book_to_lend(self,frame):
        self.frame = frame

        self.book_user_input = self.book_code_combobox.get()
    
        if self.book_user_input in self.book_title_lst_in_database or self.book_user_input in self.book_code_lst_in_database:
             if self.book_user_input in self.book_title_lst_in_database:
                 pass
             elif self.book_user_input in self.book_code_lst_in_database:
                 self.index_no = self.book_code_lst_in_database.index(self.book_user_input)
                 self.row_data = self.book_data_dataframe.loc[self.index_no]
                 self.book_user_input=self.row_data['book_title']

             pass
        else:
             messagebox.showinfo('information', 'Book not found')
             return 0

        if len(self.selected_book_list)==4:
            messagebox.showinfo('information', 'maximum four book can be assigne to student')
            return 0

        if self.book_user_input not in self.selected_book_list:
            self.selected_book_list.append(self.book_user_input)
            self.diaplay_book_name_label = tk.Label(self.frame, text=self.book_user_input,font=("Arial Bold", 11),fg="#2f5597",bg='white',borderwidth=1, relief="solid",width=18)
            self.diaplay_book_name_label.place(x=295,y=self.diaplay_book_name_label_y_pos)

            self.label_var=tk.StringVar()
            self.close_book_name_label_button = tk.Label(self.frame,image=self.close_icon_img,textvariable=self.label_var)
            self.close_book_name_label_button.place(x=465,y=self.diaplay_book_name_label_y_pos)
            self.close_book_name_label_button.bind("<Button-1>", lambda event,book_name_label =self.diaplay_book_name_label,close_book_name_icon=self.close_book_name_label_button,book_name=self.book_user_input: self.remove_selected_book(book_name_label,close_book_name_icon,book_name))

            self.diaplay_book_name_label_lst.append(self.diaplay_book_name_label)
            self.close_book_name_label_button_lst.append(self.close_book_name_label_button)
            self.diaplay_book_name_label_y_pos+=40

    def remove_selected_book(self,book_name_label,close_book_name_icon,book_name):
        book_name_label.destroy()
        close_book_name_icon.destroy()
        self.selected_book_list.remove(book_name)
        self.diaplay_book_name_label_lst.remove(book_name_label)
        self.close_book_name_label_button_lst.remove(close_book_name_icon)
        self.diaplay_book_name_label_y_pos-=40
        self.diaplay_book_name_label_y_pos=120
        if len(self.selected_book_list)>0:
            self.diaplay_book_name_label_y_pos=120
            for i in self.diaplay_book_name_label_lst:
                i.place(x=295,y=self.diaplay_book_name_label_y_pos)
                self.diaplay_book_name_label_y_pos+=40
            self.diaplay_book_name_label_y_pos=120
            for j in self.close_book_name_label_button_lst:
                j.place(x=465,y=self.diaplay_book_name_label_y_pos)
                self.diaplay_book_name_label_y_pos+=40

    def diplay_previously_alloted_book(self,frame):
        self.frame = frame
        book_lending_details_dataframe=self.load_to_db.search_in_database(self.book_lending_table_name)
        # duckdb.query("select count(*) as billable_cnt from df where dm_name = 'sanket' and Exection_hub='iDEAS-DIGITAL-EXECUTION HUB-EUROPE' and billable_cat='%s'" %i).df()
        self.previously_alloted_book_df = duckdb.query("select * from book_lending_details_dataframe where student_id='1001'").df()
        self.previously_alloted_book_list = list(self.previously_alloted_book_df['book_title'])
        print(self.previously_alloted_book_df)
        self.diaplay_book_name_label_y_pos=120
        for book_name in self.previously_alloted_book_list:
            self.diaplay_book_name_label = tk.Label(self.frame, text=book_name,font=("Arial Bold", 11),fg="#2f5597",bg='white',borderwidth=1, relief="solid",width=18)
            self.diaplay_book_name_label.place(x=295,y=self.diaplay_book_name_label_y_pos)

            self.label_var=tk.StringVar()
            self.close_book_name_label_button = tk.Label(self.frame,image=self.close_icon_img,textvariable=self.label_var)
            self.close_book_name_label_button.place(x=465,y=self.diaplay_book_name_label_y_pos)
            self.close_book_name_label_button.bind("<Button-1>", lambda event,book_name_label =self.diaplay_book_name_label,close_book_name_icon=self.close_book_name_label_button,book_name=book_name: self.remove_selected_book(book_name_label,close_book_name_icon,book_name))

            self.diaplay_book_name_label_y_pos+=35
        pass







    def allot_book_to_student(self):
        print('---------------------------')
        print(self.selected_book_list)
        print(self.diaplay_student_name_label.cget("text"))
        print(self.diaplay_id_label.cget("text"))
        self.selected_student_id=str(self.diaplay_id_label.cget("text")).split(':')
        self.selected_student_id_list=[]
        self.selected_student_name_list =[]
        self.selected_book_code_list=[]
        self.selected_book_author_list=[]
        self.selected_book_description_list=[]
        self.from_date_list=[]
        self.to_date_list=[]
        self.selected_data_dataframe= self.load_to_db.search_in_database(self.book_table_name)
        self.book_data_book_title_list = list(self.selected_data_dataframe['book_title'])
        for i in self.selected_book_list:
            self.index = self.book_data_book_title_list.index(i)
            self.record = self.selected_data_dataframe.loc[self.index]
            self.selected_book_code_list.append(self.record['book_code'])
            self.selected_book_author_list.append(self.record['book_author'])
            self.selected_book_description_list.append(self.record['book_description'])
            self.selected_student_id_list.append(self.selected_student_id[1])
            self.selected_student_name_list.append(self.diaplay_student_name_label.cget("text"))
            self.from_date_list.append(self.from_date_calender.get_date())
            self.to_date_list.append(self.to_date_calender.get_date())

        self.book_lending_data_to_be_load={'student_id':self.selected_student_id_list,
                                           'student_name':self.selected_student_name_list,
                                           'book_code':self.selected_book_code_list,
                                           'book_title':self.selected_book_list,
                                           'book_author':self.selected_book_author_list,
                                           'book_description':self.selected_book_description_list,   
                                           'assigne_date':self.from_date_list,
                                           'return_date':self.to_date_list
                                           }
        
        
        self.book_lending_data_to_be_load_dataframe = pd.DataFrame(self.book_lending_data_to_be_load)
        print(self.book_lending_data_to_be_load_dataframe)
        self.load_to_db.load_book_lending_details(self.book_lending_data_to_be_load_dataframe)


        
        if len(self.selected_book_list)==0:
             messagebox.showinfo('information', 'please select book from dropdown')
             return 0


        pass



    def check_and_destroy_frame(self,root):
        self.status_message_label.config(text='',font=("Arial Bold", 9))
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):
                if child.winfo_name() in ['add_student_frame','update_student_frame','delete_student_frame','add_book_frame','update_book_frame','delete_book_frame','lend_book_frame','update_student_book_frame','delete_lended_book_frame']:
                    child.destroy()



app_instance = Book_lending_app()
app_instance.mainloop()