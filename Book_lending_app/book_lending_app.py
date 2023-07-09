import tkinter as tk
from tkinter import *
from tkinter import ttk
# from tkinter.ttk import *
from tkinter import Button

from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox


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


    
    def mainloop(self):
        self.root.mainloop()


    def add_baground_images(self):
        self.app_icon_img = tk.PhotoImage(file='./images/app_icon.png')
        self.app_icon_img_label = tk.Label(self.root, bd=0,image=self.app_icon_img)
        self.app_icon_img_label.place(x=0,y=-1)


        self.buttons_bg_image_student = tk.PhotoImage(file='./images/button_white_bg_image.png')
        self.buttons_bg_image_student_label = tk.Label(self.root, bd=0,image=self.buttons_bg_image_student)
        self.buttons_bg_image_student_label.place(x=10,y=48)

        self.buttons_bg_image_book = tk.PhotoImage(file='./images/button_white_bg_image.png')
        self.buttons_bg_image_book_label = tk.Label(self.root, bd=0,image=self.buttons_bg_image_book)
        self.buttons_bg_image_book_label.place(x=10,y=245)

        self.buttons_bg_image_lend_book = tk.PhotoImage(file='./images/button_white_bg_image.png')
        self.buttons_bg_image_lend_book_label = tk.Label(self.root, bd=0,image=self.buttons_bg_image_lend_book)
        self.buttons_bg_image_lend_book_label.place(x=10,y=445)
        pass

    def add_buttons(self):
        self.add_new_student_button_image = Image.open("./images/add_new_student_img.png")
        self.add_new_student_button_image = ImageTk.PhotoImage(self.add_new_student_button_image)
        self.add_new_student_button = Button(self.root,image=self.add_new_student_button_image,borderwidth=0,background='white',command=self.add_new_student_window)
        self.add_new_student_button.place(x=32,y=80)

        self.update_student_details_image = Image.open("./images/update_student_img.png")
        self.update_student_details_image = ImageTk.PhotoImage(self.update_student_details_image)
        self.update_student_details_button = Button(self.root,image=self.update_student_details_image,borderwidth=0,background='white')
        self.update_student_details_button.place(x=32,y=130)

        self.delete_student_image = Image.open("./images/delete_student_img.png")
        self.delete_student_image = ImageTk.PhotoImage(self.delete_student_image)
        self.delete_student_button = Button(self.root,image=self.delete_student_image,borderwidth=0,background='white')
        self.delete_student_button.place(x=32,y=175)

        self.add_new_book_button_image = Image.open("./images/add_new_book_img.png")
        self.add_new_book_button_image = ImageTk.PhotoImage(self.add_new_book_button_image)
        self.add_new_book_button = Button(self.root,image=self.add_new_book_button_image,borderwidth=0,background='white')
        self.add_new_book_button.place(x=32,y=270)

        self.update_book_button_image = Image.open("./images/update_book_img.png")
        self.update_book_button_image = ImageTk.PhotoImage(self.update_book_button_image)
        self.update_book_button = Button(self.root,image=self.update_book_button_image,borderwidth=0,background='white')
        self.update_book_button.place(x=32,y=320)

        self.delete_book_button_image = Image.open("./images/delete_book_img.png")
        self.delete_book_button_image = ImageTk.PhotoImage(self.delete_book_button_image)
        self.delete_book_button = Button(self.root,image=self.delete_book_button_image,borderwidth=0,background='white')
        self.delete_book_button.place(x=32,y=370)


        self.lend_book_button_image = Image.open("./images/lend_book_img.png")
        self.lend_book_button_image = ImageTk.PhotoImage(self.lend_book_button_image)
        self.lend_book_button = Button(self.root,image=self.lend_book_button_image,borderwidth=0,background='white')
        self.lend_book_button.place(x=32,y=470)

        self.update_student_book_button_image = Image.open("./images/update_student_book_img.png")
        self.update_student_book_button_image = ImageTk.PhotoImage(self.update_student_book_button_image)
        self.update_student_book_button = Button(self.root,image=self.update_student_book_button_image,borderwidth=0,background='white')
        self.update_student_book_button.place(x=32,y=520)

        self.delete_student_book_button_image = Image.open("./images/delete_student_book_img.png")
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
        pass


    def check_and_destroy_frame(self,root):
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):
                if child.winfo_name() in ['add_student_frame','update_student_frame']:
                    child.destroy()
app_instance = Book_lending_app()
app_instance.mainloop()