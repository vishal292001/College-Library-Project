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
import database_loaders





class Book_lending_app():
    def __init__(self):
        self.root = Tk()
        self.root.title("Book Lending App")
        self.root.geometry('1150x700')
        self.root.configure(bg='white')

        self.load_to_db = database_loaders.Load_to_Database()
        self.add_baground_images()
        self.add_buttons()
        self.add_user_inputs()

        self.diaplay_book_name_label_y_pos = 120
        self.selected_book_list = []
        self.diaplay_book_name_label_lst=[]
        self.close_book_name_label_button_lst =[]
        self.selected_student_to_lend_book_lst = []
        self.student_table_name='student_details'
        self.book_table_name='books_details'

        self.status_message_label = tk.Label(self.root, bd=0,text="",font=("Arial Bold", 14),fg="green",bg='white')
        self.status_message_label.place(x=382,y=75)


    
    def mainloop(self):
        self.root.mainloop()


    def add_baground_images(self):
        self.app_icon_img = tk.PhotoImage(file='./images/app_icon.png')
        self.app_icon_img_label = tk.Label(self.root, bd=0,image=self.app_icon_img)
        self.app_icon_img_label.place(x=0,y=-1)

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



        pass

    def add_buttons(self):
        self.add_new_student_button_image = Image.open("./images/add_new_student_img_light_blue.png")
        self.add_new_student_button_image = ImageTk.PhotoImage(self.add_new_student_button_image)
        self.add_new_student_button = Button(self.root,image=self.add_new_student_button_image,borderwidth=0,background='white',command=self.add_new_student_window)
        self.add_new_student_button.place(x=32,y=80)

        self.update_student_details_image = Image.open("./images/update_student_img_light_blue.png")
        self.update_student_details_image = ImageTk.PhotoImage(self.update_student_details_image)
        self.update_student_details_button = Button(self.root,image=self.update_student_details_image,borderwidth=0,background='white',command=self.update_student_details_window)
        self.update_student_details_button.place(x=32,y=130)

        self.delete_student_image = Image.open("./images/delete_student_img_light_blue.png")
        self.delete_student_image = ImageTk.PhotoImage(self.delete_student_image)
        self.delete_student_button = Button(self.root,image=self.delete_student_image,borderwidth=0,background='white',command=self.delete_student_window)
        self.delete_student_button.place(x=32,y=175)

        self.add_new_book_button_image = Image.open("./images/add_new_book_img.png")
        self.add_new_book_button_image = ImageTk.PhotoImage(self.add_new_book_button_image)
        self.add_new_book_button = Button(self.root,image=self.add_new_book_button_image,borderwidth=0,background='white',command=self.add_new_book_window)
        self.add_new_book_button.place(x=32,y=270)

        self.update_book_button_image = Image.open("./images/update_book_img.png")
        self.update_book_button_image = ImageTk.PhotoImage(self.update_book_button_image)
        self.update_book_button = Button(self.root,image=self.update_book_button_image,borderwidth=0,background='white',command=self.update_book_details_window)
        self.update_book_button.place(x=32,y=320)

        self.delete_book_button_image = Image.open("./images/delete_book_img.png")
        self.delete_book_button_image = ImageTk.PhotoImage(self.delete_book_button_image)
        self.delete_book_button = Button(self.root,image=self.delete_book_button_image,borderwidth=0,background='white',command=self.delete_book_window)
        self.delete_book_button.place(x=32,y=370)


        self.lend_book_button_image = Image.open("./images/lend_book_img_green.png")
        self.lend_book_button_image = ImageTk.PhotoImage(self.lend_book_button_image)
        self.lend_book_button = Button(self.root,image=self.lend_book_button_image,borderwidth=0,background='white',command=self.lend_book_window)
        self.lend_book_button.place(x=32,y=470)

        self.update_student_book_button_image = Image.open("./images/update_student_book_img_green.png")
        self.update_student_book_button_image = ImageTk.PhotoImage(self.update_student_book_button_image)
        self.update_student_book_button = Button(self.root,image=self.update_student_book_button_image,borderwidth=0,background='white',command=self.update_student_book_window)
        self.update_student_book_button.place(x=32,y=520)

        self.delete_student_book_button_image = Image.open("./images/delete_student_book_img_green.png")
        self.delete_student_book_button_image = ImageTk.PhotoImage(self.delete_student_book_button_image)
        self.delete_student_book_button = Button(self.root,image=self.delete_student_book_button_image,borderwidth=0,background='white')
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
        else:
            self.status_message_label.config(text="Authentication Failed",fg='red')




    def add_new_student_window(self):
        self.check_and_destroy_frame(self.root)
        self.student_details_frame = Frame(self.root,bg="white",borderwidth=6,width=500,height=400,name='add_student_frame',highlightbackground="black",highlightthickness=2)
        self.student_details_frame.place(x=260,y=140)

        self.student_details_img = tk.PhotoImage(file='./images/student_details_img.png')
        self.student_details_img_label = tk.Label(self.student_details_frame, bd=0,image=self.student_details_img)
        self.student_details_img_label.place(x=20,y=40)
        
        
        self.student_id_text_box = tk.Text(self.student_details_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="blue")
        self.student_id_text_box.place(x=220,y=55)

        self.student_name_text_box = tk.Text(self.student_details_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="blue")
        self.student_name_text_box.place(x=220,y=110)

        self.student_email_text_box = tk.Text(self.student_details_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="blue")
        self.student_email_text_box.place(x=220,y=165)

        self.student_phone_text_box = tk.Text(self.student_details_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="blue")
        self.student_phone_text_box.place(x=220,y=215)
 
        self.add_student_to_db_button = ttk.Button(self.student_details_frame, text="ADD",command=self.add_new_student_to_database)
        self.add_student_to_db_button.place(x=140,y=310)

        self.cancel_button = ttk.Button(self.student_details_frame, text="CANCEL")
        self.cancel_button.place(x=240,y=310)
        pass

    def update_student_details_window(self):
        self.check_and_destroy_frame(self.root)
        self.update_student_details_frame = Frame(self.root,bg="white",borderwidth=6,width=500,height=400,name='update_student_frame',highlightbackground="black",highlightthickness=2)
        self.update_student_details_frame.place(x=260,y=140)


        self.enter_student_id_image = tk.PhotoImage(file='./images/enter_student_id_img.png')
        self.enter_student_id_image_label = tk.Label(self.update_student_details_frame, bd=0,image=self.enter_student_id_image)
        self.enter_student_id_image_label.place(x=10,y=40)

        self.student_id_text_box = tk.Text(self.update_student_details_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.student_id_text_box.place(x=184,y=55)

        self.search_student_img = Image.open("./images/search_img.png")
        self.search_student_img = self.search_student_img.resize((90, 50))
        self.search_student_img = ImageTk.PhotoImage(self.search_student_img)
        self.search_button = Button(self.update_student_details_frame,image=self.search_student_img,borderwidth=0,background='white',command=lambda:self.search_element_in_database(self.student_id_text_box.get("1.0", "end-1c"),self.student_table_name))
        self.search_button.place(x=380,y=35)

        self.update_student_details_bg_image = tk.PhotoImage(file='./images/update_student_details_bg_img.png')
        self.update_student_details_bg_image_label = tk.Label(self.update_student_details_frame, bd=0,image=self.update_student_details_bg_image)
        self.update_student_details_bg_image_label.place(x=5,y=120)

        self.student_name_text_box = tk.Text(self.update_student_details_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.student_name_text_box.place(x=184,y=135)

        self.student_email_text_box = tk.Text(self.update_student_details_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.student_email_text_box.place(x=184,y=195)

        self.student_phone_text_box = tk.Text(self.update_student_details_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.student_phone_text_box.place(x=184,y=250)

        self.update_student_button = ttk.Button(self.update_student_details_frame, text="Update",command=self.update_student_details_in_database)
        self.update_student_button.place(x=140,y=320)

        self.update_cancel_button = ttk.Button(self.update_student_details_frame, text="Cancel")
        self.update_cancel_button.place(x=240,y=320)

        pass


    def delete_student_window(self):
        self.check_and_destroy_frame(self.root)
        self.delete_student_frame = Frame(self.root,bg="white",borderwidth=6,width=500,height=400,name='delete_student_frame',highlightbackground="black",highlightthickness=2)
        self.delete_student_frame.place(x=260,y=140)


        self.enter_student_id_image = tk.PhotoImage(file='./images/enter_student_id_img.png')
        self.enter_student_id_image_label = tk.Label(self.delete_student_frame, bd=0,image=self.enter_student_id_image)
        self.enter_student_id_image_label.place(x=10,y=40)

        self.student_id_text_box = tk.Text(self.delete_student_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.student_id_text_box.place(x=184,y=55)



        self.search_student_img = Image.open("./images/search_img.png")
        self.search_student_img = self.search_student_img.resize((90, 50))
        self.search_student_img = ImageTk.PhotoImage(self.search_student_img)
        self.search_button = Button(self.delete_student_frame,image=self.search_student_img,borderwidth=0,background='white',command=lambda:self.search_element_in_database(self.student_id_text_box.get("1.0", "end-1c"),self.student_table_name))
        self.search_button.place(x=380,y=35)

        self.delete_student_details_bg_image = tk.PhotoImage(file='./images/update_student_details_bg_img.png')
        self.delete_student_details_bg_image_label = tk.Label(self.delete_student_frame, bd=0,image=self.delete_student_details_bg_image)
        self.delete_student_details_bg_image_label.place(x=5,y=120)

        self.student_name_text_box = tk.Text(self.delete_student_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.student_name_text_box.place(x=184,y=135)

        self.student_email_text_box = tk.Text(self.delete_student_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.student_email_text_box.place(x=184,y=195)

        self.student_phone_text_box = tk.Text(self.delete_student_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.student_phone_text_box.place(x=184,y=250)

        self.delete_student_button = ttk.Button(self.delete_student_frame, text="Delete",command=self.delete_student_from_database)
        self.delete_student_button.place(x=140,y=320)

        self.delete_cancel_button = ttk.Button(self.delete_student_frame, text="Cancel")
        self.delete_cancel_button.place(x=240,y=320)

        pass


    def add_new_book_window(self):
        self.check_and_destroy_frame(self.root)
        self.add_new_book_frame = Frame(self.root,bg="white",borderwidth=6,width=500,height=400,name='add_book_frame',highlightbackground="black",highlightthickness=2)
        self.add_new_book_frame.place(x=260,y=140)

        self.new_book_details_img = tk.PhotoImage(file='./images/book_details_img.png')
        self.new_book_details_img_label = tk.Label(self.add_new_book_frame, bd=0,image=self.new_book_details_img)
        self.new_book_details_img_label.place(x=20,y=40)

        self.book_code_text_box = tk.Text(self.add_new_book_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="blue")
        self.book_code_text_box.place(x=220,y=65)

        self.book_title_text_box = tk.Text(self.add_new_book_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="blue")
        self.book_title_text_box.place(x=220,y=120)

        self.book_author_text_box = tk.Text(self.add_new_book_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="blue")
        self.book_author_text_box.place(x=220,y=175)

        self.book_descr_text_box = tk.Text(self.add_new_book_frame,height = 2,width = 25, highlightthickness=1,highlightbackground="blue")
        self.book_descr_text_box.place(x=220,y=225)

        self.add_book_to_db_button = ttk.Button(self.add_new_book_frame, text="ADD",command=self.add_new_book_to_database)
        self.add_book_to_db_button.place(x=140,y=310)

        self.cancel_adding_book_button = ttk.Button(self.add_new_book_frame, text="CANCEL")
        self.cancel_adding_book_button.place(x=240,y=310)

        pass

    def update_book_details_window(self):
        self.check_and_destroy_frame(self.root)
        self.update_book_details_frame = Frame(self.root,bg="white",borderwidth=6,width=500,height=400,name='update_book_frame',highlightbackground="black",highlightthickness=2)
        self.update_book_details_frame.place(x=260,y=140)


        self.enter_book_code_image = tk.PhotoImage(file='./images/enter_book_code_img.png')
        self.enter_book_code_image_label = tk.Label(self.update_book_details_frame, bd=0,image=self.enter_book_code_image)
        self.enter_book_code_image_label.place(x=10,y=40)

        self.book_code_text_box = tk.Text(self.update_book_details_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.book_code_text_box.place(x=184,y=55)

        self.search_book_img = Image.open("./images/search_img.png")
        self.search_book_img = self.search_book_img.resize((90, 50))
        self.search_book_img = ImageTk.PhotoImage(self.search_book_img)
        self.search_button = Button(self.update_book_details_frame,image=self.search_book_img,borderwidth=0,background='white',command=lambda:self.search_element_in_database(self.book_code_text_box.get("1.0", "end-1c"),self.book_table_name))
        self.search_button.place(x=380,y=35)

        self.update_book_details_bg_image = tk.PhotoImage(file='./images/update_book_details_img.png')
        self.update_book_details_bg_image_label = tk.Label(self.update_book_details_frame, bd=0,image=self.update_book_details_bg_image)
        self.update_book_details_bg_image_label.place(x=5,y=120)

        self.book_title_text_box = tk.Text(self.update_book_details_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.book_title_text_box.place(x=184,y=135)

        self.book_author_text_box = tk.Text(self.update_book_details_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.book_author_text_box.place(x=184,y=195)

        self.book_descr_text_box = tk.Text(self.update_book_details_frame,height = 2,width = 22, highlightthickness=1,highlightbackground="blue")
        self.book_descr_text_box.place(x=184,y=250)

        self.update_book_button = ttk.Button(self.update_book_details_frame, text="Update",command=self.update_book_details_in_database)
        self.update_book_button.place(x=140,y=320)

        self.update_book_cancel_button = ttk.Button(self.update_book_details_frame, text="Cancel")
        self.update_book_cancel_button.place(x=240,y=320)

        pass


    def delete_book_window(self):
        self.check_and_destroy_frame(self.root)
        self.delete_book_frame = Frame(self.root,bg="white",borderwidth=6,width=500,height=400,name='delete_book_frame',highlightbackground="black",highlightthickness=2)
        self.delete_book_frame.place(x=260,y=140)


        self.enter_book_code_image = tk.PhotoImage(file='./images/enter_book_code_img.png')
        self.enter_book_code_image_label = tk.Label(self.delete_book_frame, bd=0,image=self.enter_book_code_image)
        self.enter_book_code_image_label.place(x=10,y=40)

        self.book_code_text_box = tk.Text(self.delete_book_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.book_code_text_box.place(x=184,y=55)

        self.search_book_img = Image.open("./images/search_img.png")
        self.search_book_img = self.search_book_img.resize((90, 50))
        self.search_book_img = ImageTk.PhotoImage(self.search_book_img)
        self.search_button = Button(self.delete_book_frame,image=self.search_book_img,borderwidth=0,background='white',command=lambda:self.search_element_in_database(self.book_code_text_box.get("1.0", "end-1c"),self.book_table_name))
        self.search_button.place(x=380,y=35)

        self.delete_book_bg_image = tk.PhotoImage(file='./images/update_book_details_img.png')
        self.delete_book_bg_image_label = tk.Label(self.delete_book_frame, bd=0,image=self.delete_book_bg_image)
        self.delete_book_bg_image_label.place(x=5,y=120)

        self.book_title_text_box = tk.Text(self.delete_book_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.book_title_text_box.place(x=184,y=135)

        self.book_author_text_box = tk.Text(self.delete_book_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.book_author_text_box.place(x=184,y=195)

        self.book_descr_text_box = tk.Text(self.delete_book_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.book_descr_text_box.place(x=184,y=250)

        self.delete_book_button = ttk.Button(self.delete_book_frame, text="Delete",command=self.delete_book_from_database)
        self.delete_book_button.place(x=140,y=320)

        self.delete_book_cancel_button = ttk.Button(self.delete_book_frame, text="Cancel")
        self.delete_book_cancel_button.place(x=240,y=320)

        pass

    def lend_book_window(self):
        if self.load_to_db.flag==False:
            messagebox.showinfo('information', 'User Authentication is Pending')
            return 0
        self.check_and_destroy_frame(self.root)

        self.student_name_lst_in_database =[]
        self.student_id_lst_in_database=[]
        self.dataframe = self.load_to_db.search_in_database(self.student_table_name)
        self.student_name_lst_in_database=list(self.dataframe['student_name'])
        self.student_id_lst_in_database=list(self.dataframe['student_id'])

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
        
        self.search_button_book = Button(self.lend_book_frame,image=self.search_icon_img,borderwidth=0,background='white',command=self.find_book_to_lend)
        self.search_button_book.place(x=420,y=22)

        self.book_code_combobox_var = tk.StringVar()
        self.book_code_combobox = ttk.Combobox(self.lend_book_frame, width = 24,values=['The Great Gatsby','Pride and Prejudice','Discovery of India','Harry Potter'], textvariable=self.book_code_combobox_var)
        self.book_code_combobox.place(x=295,y=75)


        self.from_date_calender=DateEntry(self.lend_book_frame,selectmode='day')
        self.from_date_calender.place(x=10,y=170)
        self.from_date_label = tk.Label(self.lend_book_frame, text="From Date",font=("Arial Bold", 11),fg="#2f5597",bg='white')
        self.from_date_label.place(x=110,y=170)

        self.to_date_calender=DateEntry(self.lend_book_frame,selectmode='day')
        self.to_date_calender.place(x=10,y=210)
        self.to_date_label = tk.Label(self.lend_book_frame, text="To Date",font=("Arial Bold", 11),fg="#2f5597",bg='white')
        self.to_date_label.place(x=110,y=210)


        self.allot_book_button = ttk.Button(self.lend_book_frame, text="Allot Book")
        self.allot_book_button.place(x=140,y=456)

        self.allot_book_cancel_button = ttk.Button(self.lend_book_frame, text="Cancel")
        self.allot_book_cancel_button.place(x=220,y=456)
        pass

    def find_student_to_lend_book(self,frame):
        self.frame = frame
        self.user_input = self.student_id_combobox.get()
        if self.user_input in self.student_name_lst_in_database or int(self.user_input) in self.student_id_lst_in_database:
             if self.user_input in self.student_name_lst_in_database:
                 pass
             elif int(self.user_input) in self.student_id_lst_in_database:
                 self.index_no = self.student_id_lst_in_database.index(int(self.user_input))
                 self.row_data = self.dataframe.loc[self.index_no]
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

        if len(self.selected_student_to_lend_book_lst)==0:
            self.diaplay_student_name_label = tk.Label(self.frame, text=self.user_input,font=("Arial Bold", 11),fg="#2f5597",bg='white',borderwidth=1, relief="solid",width=18)
            self.diaplay_student_name_label.place(x=12,y=120)

            self.close_student_name_label_button = Button(self.frame,image=self.close_icon_img,borderwidth=0,background='white',command=self.remove_selected_student)
            self.close_student_name_label_button.place(x=180,y=120)
            self.selected_student_to_lend_book_lst.append(self.diaplay_student_name_label)
            self.selected_student_to_lend_book_lst.append(self.close_student_name_label_button)

        pass

    def remove_selected_student(self):
        self.diaplay_student_name_label.destroy()
        self.close_student_name_label_button.destroy()
        self.selected_student_to_lend_book_lst=[]

    def find_book_to_lend(self,frame):
            self.frame = frame
            if self.book_code_combobox.get() not in self.selected_book_list:
                self.selected_book_list.append(self.book_code_combobox.get())
                self.diaplay_book_name_label = tk.Label(self.frame, text=self.book_code_combobox.get(),font=("Arial Bold", 11),fg="#2f5597",bg='white',borderwidth=1, relief="solid",width=18)
                self.diaplay_book_name_label.place(x=295,y=self.diaplay_book_name_label_y_pos)

                self.label_var=tk.StringVar()
                self.close_book_name_label_button = tk.Label(self.frame,image=self.close_icon_img,textvariable=self.label_var)
                self.close_book_name_label_button.place(x=465,y=self.diaplay_book_name_label_y_pos)
                self.close_book_name_label_button.bind("<Button-1>", lambda event,book_name_label =self.diaplay_book_name_label,close_book_name_icon=self.close_book_name_label_button,book_name=self.book_code_combobox.get(): self.remove_selected_book(book_name_label,close_book_name_icon,book_name))

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

    def update_student_book_window(self):
        self.check_and_destroy_frame(self.root)
        self.update_student_book_frame = Frame(self.root,bg="white",borderwidth=6,width=500,height=400,name='update_student_book_frame',highlightbackground="black",highlightthickness=2)
        self.update_student_book_frame.place(x=260,y=140)

        self.enter_student_id_image_label = tk.Label(self.update_student_book_frame, bd=0,image=self.enter_student_id_image_lend_win)
        self.enter_student_id_image_label.place(x=10,y=20)

        self.student_id_combobox_var = tk.StringVar()
        self.student_id_combobox = ttk.Combobox(self.update_student_book_frame, width = 24,values=['Vishal Nitavne','Vanshika Deshpande'], textvariable=self.student_id_combobox_var)
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


    def add_new_student_to_database(self):
        self.student_details_list =[]
        self.student_details_list.append(self.student_id_text_box.get("1.0", "end-1c"))
        self.student_details_list.append(self.student_name_text_box.get("1.0", "end-1c"))
        self.student_details_list.append(self.student_email_text_box.get("1.0", "end-1c"))
        self.student_details_list.append(self.student_phone_text_box.get("1.0", "end-1c"))
        print(self.student_details_list)

        for i in self.student_details_list:
            if len(i)==0:
                messagebox.showinfo('information', 'Field is Empty')
                return 0
        if self.load_to_db.flag==False:
                messagebox.showinfo('information', 'User Authentication is Pending')
                return 0
        self.df = self.load_to_db.search_in_database(self.student_table_name)
        self.student_id_list = list(self.df['student_id'])
        self.student_id = int(self.student_id_text_box.get("1.0", "end-1c"))
        if self.student_id in self.student_id_list:
            messagebox.showinfo('information', 'student with this id already exist in database')
            return 0
        else:
            self.load_to_db.load_student_to_database(tuple(self.student_details_list))
            if self.load_to_db.flag:
                self.status_message_label.config(text='Student is Added to Database Successfully StudentID:'+str(self.student_details_list[0]),font=("Arial Bold", 10))

    def add_new_book_to_database(self):
        self.book_details_list =[]
        self.book_details_list.append(self.book_code_text_box.get("1.0", "end-1c"))
        self.book_details_list.append(self.book_title_text_box.get("1.0", "end-1c"))
        self.book_details_list.append(self.book_author_text_box.get("1.0", "end-1c"))
        self.book_details_list.append(self.book_descr_text_box.get("1.0", "end-1c"))

        for i in self.book_details_list:
            if len(i)==0:
                messagebox.showinfo('information', 'Field is Empty')
                return 0
        if self.load_to_db.flag==False:
                messagebox.showinfo('information', 'User Authentication is Pending')
                return 0
        self.dataframe = self.load_to_db.search_in_database(self.book_table_name)
        self.book_code_list = list(self.dataframe['book_code'])
        self.book_code = int(self.book_code_text_box.get("1.0", "end-1c"))
        if self.book_code in self.book_code_list:
            messagebox.showinfo('information', 'book with this id already exist in database')
            return 0
        else:
            self.load_to_db.load_book_to_database(tuple(self.book_details_list))
            if self.load_to_db.flag:
                self.status_message_label.config(text='Book is Added to Database Successfully Book Code:'+str(self.book_details_list[0]),font=("Arial Bold", 10))
    
    def search_element_in_database(self,element_id,table_name):
        if self.load_to_db.flag==False:
            messagebox.showinfo('information', 'User Authentication is Pending')
            return 0
        self.element_id=int(element_id)
        self.table_name = table_name
        self.dataframe = self.load_to_db.search_in_database(self.table_name)
        print(self.dataframe)
        if self.table_name=='student_details':
            self.element_id_list = list(self.dataframe['student_id'])
        elif self.table_name=='books_details':
            self.element_id_list = list(self.dataframe['book_code'])

        if self.element_id in self.element_id_list:
            self.row_index = self.element_id_list.index(self.element_id)
            self.row = self.dataframe.loc[self.row_index]
            if self.table_name=='student_details':
                self.student_id=self.student_id_text_box.get("1.0", "end-1c")
                self.student_name_text_box.delete("1.0","end")
                self.student_email_text_box.delete("1.0","end")
                self.student_phone_text_box.delete("1.0","end")
                self.student_name_text_box.insert(tk.END,self.row['student_name'])
                self.student_email_text_box.insert(tk.END,self.row['student_email'])
                self.student_phone_text_box.insert(tk.END,self.row['student_phone'])
            elif self.table_name=='books_details':
                self.book_code = self.book_code_text_box.get("1.0", "end-1c")
                self.book_title_text_box.delete("1.0","end")
                self.book_author_text_box.delete("1.0","end")
                self.book_descr_text_box.delete("1.0","end")
                self.book_title_text_box.insert(tk.END,self.row['book_title'])
                self.book_author_text_box.insert(tk.END,self.row['book_author'])
                self.book_descr_text_box.insert(tk.END,self.row['book_description'])


        else:
            if self.table_name=='student_details':
                messagebox.showinfo('information', 'Student not found')
            elif self.table_name=='books_details':
                messagebox.showinfo('information', 'Book not found')

    
    def update_student_details_in_database(self):
        self.student_name = self.student_name_text_box.get("1.0", "end-1c")
        self.student_email = self.student_email_text_box.get("1.0", "end-1c")
        self.student_phone = self.student_phone_text_box.get("1.0", "end-1c")
        self.load_to_db.update_student_details_in_database(self.student_id,self.student_name,self.student_email,self.student_phone)
        if self.load_to_db.flag:
            self.status_message_label.config(text='Student details Updated Successfully',fg='green')
        else:
            messagebox.showinfo('information', 'failed to update student data')

    def update_book_details_in_database(self):
        self.book_title = self.book_title_text_box.get("1.0", "end-1c")
        self.book_author = self.book_author_text_box.get("1.0", "end-1c")
        self.book_description = self.book_descr_text_box.get("1.0", "end-1c")
        self.load_to_db.update_book_details_in_database(self.book_code,self.book_title,self.book_author,self.book_description)
        if self.load_to_db.flag:
            self.status_message_label.config(text='book details Updated Successfully',fg='green')
        else:
            messagebox.showinfo('information', 'failed to update books details')

    def delete_student_from_database(self):
        self.load_to_db.delete_student_record_in_database(self.student_id)
        if self.load_to_db.flag:
            self.status_message_label.config(text='Student record deleted StudentID:'+str(self.student_id),fg='green')
        else:
            messagebox.showinfo('information', 'failed to delete student record')

    def delete_book_from_database(self):
        self.load_to_db.delete_book_from_database(self.book_code)
        if self.load_to_db.flag:
            self.status_message_label.config(text='Book is deleted Book Code:'+str(self.book_code),fg='green')
        else:
            messagebox.showinfo('information', 'failed to delete book')
        
    def check_and_destroy_frame(self,root):
        self.status_message_label.config(text='',font=("Arial Bold", 10))
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):
                if child.winfo_name() in ['add_student_frame','update_student_frame','delete_student_frame','add_book_frame','update_book_frame','delete_book_frame','lend_book_frame','update_student_book_frame']:
                    child.destroy()



app_instance = Book_lending_app()
app_instance.mainloop()