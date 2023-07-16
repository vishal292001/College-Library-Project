import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox


import urllib
import pandas as pd
import json
import create_schema
import database_loaders




class Book_Details():
    def __init__(self):
        self.root = Tk()
        self.root.title("Book Details App")
        self.root.geometry('1050x650')
        self.root.configure(bg='white')

    # Loaded the background image
        self.image = Image.open("./app/images/bg_img.png")
        self.image = self.image.resize((1050, 650), Image.ANTIALIAS)  
        self.background_image = ImageTk.PhotoImage(self.image)

    # Created a label with the background image and configure it to fill the window
        self.background_label = Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.load_to_db = database_loaders.Load_to_Database()
        self.add_buttons()

       
    def mainloop(self):
        self.root.mainloop()

    # Function for all the buttons(Add/Update/Delete)
    def add_buttons(self):
        self.add_book_button_image = Image.open("./app/images/add_book_btn_img.png")
        self.add_book_button_image = self.add_book_button_image.resize((140, 60))
        self.add_book_button_image = ImageTk.PhotoImage(self.add_book_button_image)
        self.add_book_button = ttk.Button(self.root, text="add book",image=self.add_book_button_image,command=self.add_book_details_window)
        self.add_book_button.place(x=100,y=50)

        self.update_book_button_image = Image.open("./app/images/update_book_btn_image.png")
        self.update_book_button_image = self.update_book_button_image.resize((140, 60))
        self.update_book_button_image = ImageTk.PhotoImage(self.update_book_button_image)
        self.update_book_button = ttk.Button(self.root, text="update book",image=self.update_book_button_image,command=self.update_book_details_window)
        self.update_book_button.place(x=260,y=50)


        self.delete_book_button_image = Image.open("./app/images/delete_book_btn_img.png")
        self.delete_book_button_image = self.delete_book_button_image.resize((140, 60))
        self.delete_book_button_image = ImageTk.PhotoImage(self.delete_book_button_image)
        self.delete_book_button = ttk.Button(self.root, text="delete book",image=self.delete_book_button_image,command=self.delete_book_window)
        self.delete_book_button.place(x=420,y=50)

        
        self.authenticate_button_image = Image.open("./app/images/Authenticate_user_img.png")
        self.authenticate_button_image = self.authenticate_button_image.resize((140, 60))
        self.authenticate_button_image = ImageTk.PhotoImage(self.authenticate_button_image)
        self.authenticate_button = ttk.Button(self.root, text="Authenticate",image=self.authenticate_button_image,command=self.database_details)
        self.authenticate_button.place(x=730,y=50)
   

        pass

     # funtion for Add book details window
    def add_book_details_window(self):
        self.check_and_destroy_frame(self.root)
        self.book_details_frame = Frame(self.root,bg="white",borderwidth=6,width=600,height=400,name='add_book_frame')
        self.book_details_frame.place(x=40,y=140)

        self.book_details_bg_image = tk.PhotoImage(file='./app/images/book_details_bg_img copy.png')
        self.book_details_bg_image_label = tk.Label(self.book_details_frame, bd=0,image=self.book_details_bg_image)
        self.book_details_bg_image_label.place(x=0,y=0)

        self.book_details_image = tk.PhotoImage(file='./app/images/book_details_image.png')
        self.book_details_image_label = tk.Label(self.book_details_frame, bd=0,image=self.book_details_image)
        self.book_details_image_label.place(x=60,y=40)


        self.book_name_text_box = tk.Text(self.book_details_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.book_name_text_box.place(x=260,y=65)

        self.book_author_text_box = tk.Text(self.book_details_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.book_author_text_box.place(x=260,y=120)

        self.book_description_text_box = tk.Text(self.book_details_frame,height = 2,width = 25, highlightthickness=1,highlightbackground="black")
        self.book_description_text_box.place(x=260,y=180)

        self.book_id_text_box = tk.Text(self.book_details_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.book_id_text_box.place(x=260,y=250)

        self.add_book_to_db_button = ttk.Button(self.book_details_frame, text="ADD", command=self.add_to_database)
        self.add_book_to_db_button.place(x=170,y=300)

        self.cancel_button = ttk.Button(self.book_details_frame, text="CANCEL", command=self.cancel)
        self.cancel_button.place(x=260,y=300)


    def check_and_destroy_frame(self,root):
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):
                if child.winfo_name() in ['add_student_frame','update_student_frame']:
                    child.destroy()

    # Function for Update book details window
    def update_book_details_window(self):
        self.check_and_destroy_frame(self.root)
        self.update_book_details_frame = Frame(self.root,bg="white",borderwidth=6,width=600,height=400)
        self.update_book_details_frame.place(x=40,y=140)

        self.update_book_details_bg_image = tk.PhotoImage(file='./app/images/book_details_bg_img copy.png')
        self.update_book_details_bg_image_label = tk.Label(self.update_book_details_frame, bd=0,image=self.update_book_details_bg_image)
        self.update_book_details_bg_image_label.place(x=0,y=0)


        self.enter_book_id_img = tk.PhotoImage(file='./app/images/enter_bookid_img.png')
        self.enter_book_id_img_label = tk.Label(self.update_book_details_frame, bd=0,image=self.enter_book_id_img)
        self.enter_book_id_img_label.place(x=35,y=40)

        self.enter_book_id_text_box = tk.Text(self.update_book_details_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.enter_book_id_text_box.place(x=205,y=65)


        self.search_book_img = Image.open("./app/images/search_img.png")
        self.search_book_img = self.search_book_img.resize((70, 40))
        self.search_book_img = ImageTk.PhotoImage(self.search_book_img)
        self.search_book_button = ttk.Button(self.update_book_details_frame,text="search book",image=self.search_book_img,command=lambda:self.search_book_in_database('update'))
        self.search_book_button.place(x=435,y=50)


        pass


    #Function for delete book window
    def delete_book_window(self):
        self.check_and_destroy_frame(self.root)
        self.delete_book_frame = Frame(self.root,bg="white",borderwidth=6,width=600,height=400)
        self.delete_book_frame.place(x=40,y=140)

        self.delete_book_bg_image = tk.PhotoImage(file='./app/images/book_details_bg_img copy.png')
        self.delete_book_bg_image_label = tk.Label(self.delete_book_frame, bd=0,image=self.delete_book_bg_image)
        self.delete_book_bg_image_label.place(x=0,y=0)

        self.enter_book_id_img = tk.PhotoImage(file='./app/images/enter_bookid_img.png')
        self.enter_book_id_img_label = tk.Label(self.delete_book_frame, bd=0,image=self.enter_book_id_img)
        self.enter_book_id_img_label.place(x=35,y=40)

        self.enter_book_id_text_box = tk.Text(self.delete_book_frame,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.enter_book_id_text_box.place(x=205,y=65)

        self.search_book_img_in_delete_win = Image.open("./app/images/search_img.png")
        self.search_book_img_in_delete_win = self.search_book_img_in_delete_win.resize((70, 40))
        self.search_book_img_in_delete_win = ImageTk.PhotoImage(self.search_book_img_in_delete_win)
        self.search_book_button_in_delete_win = ttk.Button(self.delete_book_frame,text="search student",image=self.search_book_img_in_delete_win,command=lambda:self.search_book_in_database('delete'))
        self.search_book_button_in_delete_win.place(x=435,y=50)


    # Function for Add to database
    def add_to_database(self):
        self.book_details_list =[]
        self.book_details_list.append(self.book_id_text_box.get("1.0", "end-1c"))
        self.book_details_list.append(self.book_name_text_box.get("1.0", "end-1c"))
        self.book_details_list.append(self.book_author_text_box.get("1.0", "end-1c"))
        self.book_details_list.append(self.book_description_text_box.get("1.0", "end-1c"))
        
        print(self.book_details_list)

        for i in self.book_details_list:
            if len(i)==0:
                messagebox.showinfo('information', 'Field is Empty')
                return 0
        
        if self.load_to_db.flag==False:
                messagebox.showinfo('information', 'User Authentication is Pending')
                return 0
        
        self.load_to_db.load_to_postgres(tuple(self.book_details_list))
        if self.load_to_db.flag:
            messagebox.showinfo('information', 'Book added to database successfully!')


            
#function  to add database details
    def database_details(self):

        self.load_to_databse_details_bg_img = tk.PhotoImage(file='./app/images/load_database_details_bg_img.png')
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

# Function that check database from the dropdown menu
    def check_database(self,*args):
        self.detect_child_frames(self.load_to_database_details_frame)

        if self.select_database_dropdown.get()=="POSTGRES":
            self.postgres_database_details_frame = Frame(self.load_to_database_details_frame,bg="white",borderwidth=6,width=240,height=160)
            self.postgres_database_details_frame.place(x=10,y=40)

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
    
    # Function for aunthenticating 
    def authenticate_user(self):
        self.database_tool_name = self.select_database_dropdown.get()
        
        if self.database_tool_name=="POSTGRES":
            self.postgres_username = self.text_box_postgres_username.get(1.0, "end-1c")
            self.postgres_password = self.text_box_postgres_password.get(1.0, "end-1c")
            self.load_to_db.connect_to_postgres('book_db','Library',self.postgres_username,self.postgres_password)


        print(self.load_to_db.flag)
        if self.load_to_db.flag:
            self.authentication_success_image = tk.PhotoImage(file='./app/images/Auth_success.png')
            self.authentication_success_image_label = tk.Label(self.root, bd=0,image=self.authentication_success_image)
            self.authentication_success_image_label.place(x=660,y=460)
            create_schema.create_book_table()
        else:
            self.authentication_failed_image = tk.PhotoImage(file='./app/images/Auth_failed.png')
            self.authentication_failed_image_label = tk.Label(self.root, bd=0,image=self.authentication_failed_image)
            self.authentication_failed_image_label.place(x=660,y=460)

    # Function to search book in database
    def search_book_in_database(self,operation):

        if self.load_to_db.flag==False:
            messagebox.showinfo('information', 'User Authentication is Pending')
            return 0
        self.book_id = self.enter_book_id_text_box.get(1.0, "end-1c")
        self.df = self.load_to_db.search_in_database()
        print(self.df)
        self.book_id_list = list(self.df['book_code'])

        if operation=='update':
            self.frame = self.update_book_details_frame
        if operation=='delete':
            self.frame=self.delete_book_frame
        self.book_details_image_opration = tk.PhotoImage(file='./app/images/book_details_image.png')
        self.book_details_image_opration_label = tk.Label(self.frame, bd=0,image=self.book_details_image_opration)
        self.book_details_image_opration_label.place(x=40,y=95)

        self.book_name_text_box = tk.Text(self.frame,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.book_name_text_box.place(x=220,y=120)

        self.book_author_text_box = tk.Text(self.frame,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.book_author_text_box.place(x=220,y=180)

        self.book_description_text_box = tk.Text(self.frame,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.book_description_text_box.place(x=220,y=240)

        self.book_id_text_box = tk.Text(self.frame,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.book_id_text_box.place(x=220,y=300)

        if self.book_id in self.book_id_list:
            self.row_index = self.book_id_list.index(self.book_id)
            self.row = self.df.loc[self.row_index]

            self.book_name_text_box.insert(tk.END,self.row['book_title'])
            self.book_author_text_box.insert(tk.END,self.row['book_author'])
            self.book_description_text_box.insert(tk.END,self.row['book_description'])
            self.book_id_text_box.insert(tk.END,self.row['book_code'])

            if operation=='update':
                self.book_to_db_button = ttk.Button(self.frame, text="Update",command=self.update_book_details)
                self.book_to_db_button.place(x=210,y=340)

                self.cancel_update_button = ttk.Button(self.frame, text="Cancel",command=self.close_update_book_details_window)
                self.cancel_update_button.place(x=300,y=340)
            if operation=='delete':
                self.book_to_db_button = ttk.Button(self.frame, text="Delete",command=self.delete_book)
                self.book_to_db_button.place(x=210,y=340)

                self.cancel_update_button = ttk.Button(self.frame, text="Cancel",command=self.close_delete_book_details_window)
                self.cancel_update_button.place(x=300,y=340)

        else:
             messagebox.showinfo('information', 'Book not found')
             print("Book not found")

# Function to update book details
    def update_book_details(self):

        self.book_name = self.book_name_text_box.get("1.0", "end-1c")
        self.book_author = self.book_author_text_box.get("1.0", "end-1c")
        self.book_description = self.book_description_text_box.get("1.0", "end-1c")
        self.book_id = self.book_id_text_box.get("1.0", "end-1c")
        self.load_to_db.update_data_in_database(self.book_name,self.book_author,self.book_description,self.book_id)
        if self.load_to_db.flag:
            messagebox.showinfo('information', 'Book Details updated Successfully!')


    def delete_book(self):
        self.load_to_db.delete_record_in_database(self.book_id)
        if self.load_to_db.flag:
            messagebox.showinfo('information', 'Book deleted Successfully!')



    def cancel(self):
        self.book_details_frame.destroy()

    def close_update_book_details_window(self):
        self.update_book_details_frame.destroy()

    def close_delete_book_details_window(self):
        self.delete_book_frame.destroy()
    
app_instance = Book_Details()
app_instance.mainloop()









        
