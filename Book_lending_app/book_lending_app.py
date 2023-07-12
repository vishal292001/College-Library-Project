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




class Book_lending_app():
    def __init__(self):
        self.root = Tk()
        self.root.title("Book Lending App")
        self.root.geometry('1050x700')
        self.root.configure(bg='white')
        self.add_baground_images()
        self.add_buttons()

        self.diaplay_book_name_label_y_pos = 120
        self.selected_book_list = []
        self.diaplay_book_name_label_lst=[]
        self.close_book_name_label_button_lst =[]
        self.selected_student_to_lend_book_lst = []

    
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

    def add_new_student_window(self):
        self.check_and_destroy_frame(self.root)
        self.student_details_frame = Frame(self.root,bg="white",borderwidth=6,width=500,height=400,name='add_student_frame',highlightbackground="black",highlightthickness=2)
        self.student_details_frame.place(x=260,y=140)

        self.student_details_img = tk.PhotoImage(file='./images/student_details_img.png')
        self.student_details_img_label = tk.Label(self.student_details_frame, bd=0,image=self.student_details_img)
        self.student_details_img_label.place(x=20,y=40)
        
        
        self.studen_id_text_box = tk.Text(self.student_details_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="blue")
        self.studen_id_text_box.place(x=220,y=55)

        self.studen_name_text_box = tk.Text(self.student_details_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="blue")
        self.studen_name_text_box.place(x=220,y=110)

        self.studen_email_text_box = tk.Text(self.student_details_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="blue")
        self.studen_email_text_box.place(x=220,y=165)

        self.studen_phone_text_box = tk.Text(self.student_details_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="blue")
        self.studen_phone_text_box.place(x=220,y=215)
 
        self.add_student_to_db_button = ttk.Button(self.student_details_frame, text="ADD")
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

        self.studen_id_text_box = tk.Text(self.update_student_details_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.studen_id_text_box.place(x=184,y=55)

        self.search_student_img = Image.open("./images/search_img.png")
        self.search_student_img = self.search_student_img.resize((90, 50))
        self.search_student_img = ImageTk.PhotoImage(self.search_student_img)
        self.search_button = Button(self.update_student_details_frame,image=self.search_student_img,borderwidth=0,background='white',command=self.add_new_student_window)
        self.search_button.place(x=380,y=35)

        self.update_student_details_bg_image = tk.PhotoImage(file='./images/update_student_details_bg_img.png')
        self.update_student_details_bg_image_label = tk.Label(self.update_student_details_frame, bd=0,image=self.update_student_details_bg_image)
        self.update_student_details_bg_image_label.place(x=5,y=120)

        self.studen_name_text_box = tk.Text(self.update_student_details_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.studen_name_text_box.place(x=184,y=135)

        self.studen_email_text_box = tk.Text(self.update_student_details_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.studen_email_text_box.place(x=184,y=195)

        self.studen_phone_text_box = tk.Text(self.update_student_details_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.studen_phone_text_box.place(x=184,y=250)

        self.update_student_button = ttk.Button(self.update_student_details_frame, text="Update")
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

        self.studen_id_text_box = tk.Text(self.delete_student_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.studen_id_text_box.place(x=184,y=55)



        self.search_student_img = Image.open("./images/search_img.png")
        self.search_student_img = self.search_student_img.resize((90, 50))
        self.search_student_img = ImageTk.PhotoImage(self.search_student_img)
        self.search_button = Button(self.delete_student_frame,image=self.search_student_img,borderwidth=0,background='white',command=self.add_new_student_window)
        self.search_button.place(x=380,y=35)

        self.update_student_details_bg_image = tk.PhotoImage(file='./images/update_student_details_bg_img.png')
        self.update_student_details_bg_image_label = tk.Label(self.delete_student_frame, bd=0,image=self.update_student_details_bg_image)
        self.update_student_details_bg_image_label.place(x=5,y=120)

        self.studen_name_text_box = tk.Text(self.delete_student_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.studen_name_text_box.place(x=184,y=135)

        self.studen_email_text_box = tk.Text(self.delete_student_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.studen_email_text_box.place(x=184,y=195)

        self.studen_phone_text_box = tk.Text(self.delete_student_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.studen_phone_text_box.place(x=184,y=250)

        self.update_student_button = ttk.Button(self.delete_student_frame, text="Delete")
        self.update_student_button.place(x=140,y=320)

        self.update_cancel_button = ttk.Button(self.delete_student_frame, text="Cancel")
        self.update_cancel_button.place(x=240,y=320)

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

        self.add_book_to_db_button = ttk.Button(self.add_new_book_frame, text="ADD")
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
        self.search_button = Button(self.update_book_details_frame,image=self.search_book_img,borderwidth=0,background='white')
        self.search_button.place(x=380,y=35)

        self.update_book_details_bg_image = tk.PhotoImage(file='./images/update_book_details_img.png')
        self.update_book_details_bg_image_label = tk.Label(self.update_book_details_frame, bd=0,image=self.update_book_details_bg_image)
        self.update_book_details_bg_image_label.place(x=5,y=120)

        self.book_title_text_box = tk.Text(self.update_book_details_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.book_title_text_box.place(x=184,y=135)

        self.book_author_text_box = tk.Text(self.update_book_details_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.book_author_text_box.place(x=184,y=195)

        self.book_descr_text_box = tk.Text(self.update_book_details_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.book_descr_text_box.place(x=184,y=250)

        self.update_book_button = ttk.Button(self.update_book_details_frame, text="Update")
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
        self.search_button = Button(self.delete_book_frame,image=self.search_book_img,borderwidth=0,background='white')
        self.search_button.place(x=380,y=35)

        self.delete_book_bg_image = tk.PhotoImage(file='./images/update_book_details_img.png')
        self.delete_book_bg_image_label = tk.Label(self.delete_book_frame, bd=0,image=self.update_book_details_bg_image)
        self.delete_book_bg_image_label.place(x=5,y=120)

        self.book_title_text_box = tk.Text(self.delete_book_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.book_title_text_box.place(x=184,y=135)

        self.book_author_text_box = tk.Text(self.delete_book_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.book_author_text_box.place(x=184,y=195)

        self.book_descr_text_box = tk.Text(self.delete_book_frame,height = 1,width = 22, highlightthickness=1,highlightbackground="blue")
        self.book_descr_text_box.place(x=184,y=250)

        self.delete_book_button = ttk.Button(self.delete_book_frame, text="Delete")
        self.delete_book_button.place(x=140,y=320)

        self.delete_book_cancel_button = ttk.Button(self.delete_book_frame, text="Cancel")
        self.delete_book_cancel_button.place(x=240,y=320)

        pass

    def lend_book_window(self):
        self.check_and_destroy_frame(self.root)
        self.lend_book_frame = Frame(self.root,bg="white",borderwidth=6,width=500,height=500,name='lend_book_frame',highlightbackground="black",highlightthickness=2)
        self.lend_book_frame.place(x=260,y=140)

        self.sub_frame = Frame(self.lend_book_frame,bg="white",borderwidth=6,width=500,height=50,highlightbackground="black",highlightthickness=2)
        self.sub_frame.place(x=-8,y=442)

        self.enter_student_id_image_label = tk.Label(self.lend_book_frame, bd=0,image=self.enter_student_id_image_lend_win)
        self.enter_student_id_image_label.place(x=10,y=20)

        self.student_id_combobox_var = tk.StringVar()
        self.student_id_combobox = ttk.Combobox(self.lend_book_frame, width = 24,values=['Vishal Nitavne','Vanshika Deshpande'], textvariable=self.student_id_combobox_var)
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
        if len(self.selected_student_to_lend_book_lst)>0:
            for i in self.selected_student_to_lend_book_lst:
                i.destroy()
            for j in self.selected_student_to_lend_book_lst:
                self.selected_student_to_lend_book_lst.pop()
                self.selected_student_to_lend_book_lst.pop()

        if len(self.selected_student_to_lend_book_lst)==0:
            self.diaplay_student_name_label = tk.Label(self.frame, text=self.student_id_combobox.get(),font=("Arial Bold", 11),fg="#2f5597",bg='white',borderwidth=1, relief="solid",width=18)
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

        
    def check_and_destroy_frame(self,root):
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):
                if child.winfo_name() in ['add_student_frame','update_student_frame','delete_student_frame','add_book_frame','update_book_frame','delete_book_frame','lend_book_frame','update_student_book_frame']:
                    child.destroy()



app_instance = Book_lending_app()
app_instance.mainloop()