import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import psycopg2

from tkinter import messagebox


from sqlalchemy import create_engine,text
import urllib
import pandas as pd
import sqlalchemy
import json
import pyodbc
import database_loaders



class Books_Details():
    def __init__(self):
        self.root = Tk()
        self.root.title("Books Details App")
        self.root.geometry('1000x650')

        # Load the background image
        self.image = Image.open("./images/bg_img.PNG")
        self.image = self.image.resize((1000, 650), Image.ANTIALIAS)  # Resize the image to fit the window size
        self.background_image = ImageTk.PhotoImage(self.image)

        # Create a label with the background image and configure it to fill the window
        self.background_label = Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.add_buttons()  # Add buttons to the window

    def add_buttons(self):
        self.add_book_button_image = Image.open("./images/add_book_btn_img.png")
        self.add_book_button_image = self.add_book_button_image.resize((140, 60))
        self.add_book_button_image = ImageTk.PhotoImage(self.add_book_button_image)
        self.add_book_button = ttk.Button(
            self.root,
            text="Add Book",
            image=self.add_book_button_image,
            command=self.add_new_book_frame
        )
        self.add_book_button.place(x=355, y=92)

        self.update_book_button_image = Image.open("./images/update_book_btn_image.png")
        self.update_book_button_image = self.update_book_button_image.resize((140, 60))
        self.update_book_button_image = ImageTk.PhotoImage(self.update_book_button_image)
        self.update_book_button = ttk.Button(
            self.root,
            text="Update Book",
            image=self.update_book_button_image,
            command=self.update_book_frame
        )
        self.update_book_button.place(x=515, y=92)

        self.delete_book_button_image = Image.open("./images/delete_book_btn_img.png")
        self.delete_book_button_image = self.delete_book_button_image.resize((140, 60))
        self.delete_book_button_image = ImageTk.PhotoImage(self.delete_book_button_image)
        self.delete_book_button = ttk.Button(
            self.root,
            text="Delete Book",
            image=self.delete_book_button_image,
            command=self.delete_book_frame
        )
        self.delete_book_button.place(x=675, y=92)
        self.authenticate_button_image = Image.open("./images/Authenticate_user_img.png")
        self.authenticate_button_image = self.authenticate_button_image.resize((140, 60))
        self.authenticate_button_image = ImageTk.PhotoImage(self.authenticate_button_image)
        self.authenticate_button = ttk.Button(self.root, text="Aithenticate",image=self.authenticate_button_image)
        self.authenticate_button.place(x=28,y=92)

    def check_and_destroy_frame(self,root):
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):
                if child.winfo_name() in ['add_new_book_frame','update_book_frame']:
                    child.destroy()

    def add_new_book_frame(self):
        self.check_and_destroy_frame(self.root)
        self.book_details_frame = Frame(self.root, bg="white", borderwidth=6, width=650, height=420)
        self.book_details_frame.place(x=280, y=180)

        self.book_details_bg_image = tk.PhotoImage(file='./images/book_details_bg_img copy.png')
        self.book_details_bg_image_label = tk.Label(self.book_details_frame, bd=0, image=self.book_details_bg_image)
        self.book_details_bg_image_label.place(x=10, y=10)

        self.book_details_image = tk.PhotoImage(file='./images/book_details_image.png')
        self.book_details_image_label = tk.Label(self.book_details_frame, bd=0, image=self.book_details_image)
        self.book_details_image_label.place(x=56, y=55)

        self.book_name_text_box = tk.Text(
            self.book_details_frame, height=1, width=25, highlightthickness=1, highlightbackground="black"
        )
        self.book_name_text_box.place(x=265, y=80)

        self.book_author_text_box = tk.Text(
            self.book_details_frame, height=1, width=25, highlightthickness=1, highlightbackground="black"
        )
        self.book_author_text_box.place(x=265, y=135)

        self.book_description_text_box = tk.Text(
            self.book_details_frame, height=2, width=25, highlightthickness=1, highlightbackground="black"
        )
        self.book_description_text_box.place(x=265, y=190)

        self.book_code_text_box = tk.Text(
            self.book_details_frame, height=1, width=25, highlightthickness=1, highlightbackground="black"
        )
        self.book_code_text_box.place(x=265, y=265)

        self.ok_button_image = Image.open("./images/ok_button_image.png")
        self.ok_button_image = self.ok_button_image.resize((60, 30))
        self.ok_button_image = ImageTk.PhotoImage(self.ok_button_image)
        self.ok_button = ttk.Button(
            self.book_details_frame, text="OK", image=self.ok_button_image, command=self.insert_book_details
        )
        self.ok_button.place(x=200, y=315)

        self.cancel_button_image = Image.open("./images/cancel_button_img.png")
        self.cancel_button_image = self.cancel_button_image.resize((60, 30))
        self.cancel_button_image = ImageTk.PhotoImage(self.cancel_button_image)
        self.cancel_button = ttk.Button(
            self.book_details_frame, text="Cancel", image=self.cancel_button_image, command=self.destroy_frame
        )
        self.cancel_button.place(x=290, y=315)



    def update_book_frame(self):
        self.book_details_frame = Frame(self.root, bg="white", borderwidth=6, width=650, height=420)
        self.book_details_frame.place(x=280, y=180)

        self.book_details_bg_image = tk.PhotoImage(file='./images/book_details_bg_img copy.png')
        self.book_details_bg_image_label = tk.Label(self.book_details_frame, bd=0, image=self.book_details_bg_image)
        self.book_details_bg_image_label.place(x=10, y=10)

        self.book_details_image = tk.PhotoImage(file='./images/book_details_image.png')
        self.book_details_image_label = tk.Label(self.book_details_frame, bd=0, image=self.book_details_image)
        self.book_details_image_label.place(x=56, y=55)

        self.book_name_text_box = tk.Text(
            self.book_details_frame, height=1, width=25, highlightthickness=1, highlightbackground="black"
        )
        self.book_name_text_box.place(x=265, y=80)

        self.book_author_text_box = tk.Text(
            self.book_details_frame, height=1, width=25, highlightthickness=1, highlightbackground="black"
        )
        self.book_author_text_box.place(x=265, y=135)

        self.book_description_text_box = tk.Text(
            self.book_details_frame, height=2, width=25, highlightthickness=1, highlightbackground="black"
        )
        self.book_description_text_box.place(x=265, y=190)

        self.book_code_text_box = tk.Text(
            self.book_details_frame, height=1, width=25, highlightthickness=1, highlightbackground="black"
        )
        self.book_code_text_box.place(x=265, y=265)

        self.ok_button_image = Image.open("./images/ok_button_image.png")
        self.ok_button_image = self.ok_button_image.resize((60, 30))
        self.ok_button_image = ImageTk.PhotoImage(self.ok_button_image)
        self.ok_button = ttk.Button(
            self.book_details_frame, text="OK", image=self.ok_button_image, command=self.update_book_details
        )
        self.ok_button.place(x=200, y=315)

        self.cancel_button_image = Image.open("./images/cancel_button_img.png")
        self.cancel_button_image = self.cancel_button_image.resize((60, 30))
        self.cancel_button_image = ImageTk.PhotoImage(self.cancel_button_image)
        self.cancel_button = ttk.Button(
            self.book_details_frame, text="Cancel", image=self.cancel_button_image, command=self.destroy_frame
        )
        self.cancel_button.place(x=290, y=315)

    
    def delete_book_frame(self):
        self.book_details_frame = Frame(self.root, bg="white", borderwidth=6, width=650, height=420)
        self.book_details_frame.place(x=280, y=180)

        self.book_details_bg_image = tk.PhotoImage(file='./images/book_details_bg_img copy.png')
        self.book_details_bg_image_label = tk.Label(self.book_details_frame, bd=0, image=self.book_details_bg_image)
        self.book_details_bg_image_label.place(x=10, y=10)

        self.book_details_image = tk.PhotoImage(file='./images/book_details_image.png')
        self.book_details_image_label = tk.Label(self.book_details_frame, bd=0, image=self.book_details_image)
        self.book_details_image_label.place(x=56, y=55)

        self.book_name_text_box = tk.Text(
            self.book_details_frame, height=1, width=25, highlightthickness=1, highlightbackground="black"
        )
        self.book_name_text_box.place(x=265, y=80)

        self.book_author_text_box = tk.Text(
            self.book_details_frame, height=1, width=25, highlightthickness=1, highlightbackground="black"
        )
        self.book_author_text_box.place(x=265, y=135)

        self.book_description_text_box = tk.Text(
            self.book_details_frame, height=2, width=25, highlightthickness=1, highlightbackground="black"
        )
        self.book_description_text_box.place(x=265, y=190)

        self.book_code_text_box = tk.Text(
            self.book_details_frame, height=1, width=25, highlightthickness=1, highlightbackground="black"
        )
        self.book_code_text_box.place(x=265, y=265)

        self.ok_button_image = Image.open("./images/ok_button_image.png")
        self.ok_button_image = self.ok_button_image.resize((60, 30))
        self.ok_button_image = ImageTk.PhotoImage(self.ok_button_image)
        self.ok_button = ttk.Button(
            self.book_details_frame, text="OK", image=self.ok_button_image, command=self.delete_book_details
        )
        self.ok_button.place(x=200, y=315)

        self.cancel_button_image = Image.open("./images/cancel_button_img.png")
        self.cancel_button_image = self.cancel_button_image.resize((60, 30))
        self.cancel_button_image = ImageTk.PhotoImage(self.cancel_button_image)
        self.cancel_button = ttk.Button(
            self.book_details_frame, text="Cancel", image=self.cancel_button_image, command=self.destroy_frame
        )
        self.cancel_button.place(x=290, y=315)

    def insert_book_details(self):
        book_name = self.book_name_text_box.get("1.0", "end-1c")
        book_author = self.book_author_text_box.get("1.0", "end-1c")
        book_description = self.book_description_text_box.get("1.0", "end-1c")
        book_code = self.book_code_text_box.get("1.0", "end-1c")

        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host="localhost",
            database="Library",
            user="postgres",
            password="Vansh12345@"
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Prepare the INSERT query
        query = "INSERT INTO public.books (name, author, description, code) VALUES (%s, %s, %s, %s)"
        values = (book_name, book_author, book_description, book_code)

        # Execute the INSERT query
        cursor.execute(query, values)

        # Commit the transaction
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        self.destroy_frame()

    def update_book_details(self):
        book_name = self.book_name_text_box.get("1.0", "end-1c")
        book_author = self.book_author_text_box.get("1.0", "end-1c")
        book_description = self.book_description_text_box.get("1.0", "end-1c")
        book_code = self.book_code_text_box.get("1.0", "end-1c")

        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host="localhost",
            database="Library",
            user="postgres",
            password="Vansh12345@"
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Prepare the UPDATE query
        query = "UPDATE public.books SET author = %s, description = %s, code = %s WHERE name = %s"
        values = (book_author, book_description, book_code, book_name)

        # Execute the UPDATE query
        cursor.execute(query, values)

        # Commit the transaction
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        self.destroy_frame()

    def delete_book_details(self):
        book_name = self.book_name_text_box.get("1.0", "end-1c")

        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host="localhost",
            database="Library",
            user="postgres",
            password="Vansh12345@"
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Prepare the DELETE query
        query = "DELETE FROM public.books WHERE name = %s"
        values = (book_name,)

        # Execute the DELETE query
        cursor.execute(query, values)

        # Commit the transaction
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        self.destroy_frame()

    def destroy_frame(self):
        self.book_details_frame.destroy()

    def mainloop(self):
        self.root.mainloop()


app_instance = Books_Details()
app_instance.mainloop()
