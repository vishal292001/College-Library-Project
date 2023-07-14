import tkinter as tk
from tkinter import *
from tkinter import ttk
# from tkinter.ttk import *
from tkinter import Button
from tkinter import messagebox
from tkinter import ttk
from PIL import Image
from PIL import ImageTk



class add_new_book_window():
    def __init__(self,root,load_to_db,status_message_label):
        self.root=root
        self.load_to_db=load_to_db
        self.status_message_label=status_message_label
        self.book_table_name='books_details'



    def add_new_book_in_database(self):
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
        self.book_code = self.book_code_text_box.get("1.0", "end-1c")
        if self.book_code in self.book_code_list:
            messagebox.showinfo('information', 'book with this id already exist in database')
            return 0
        else:
            self.load_to_db.load_book_to_database(tuple(self.book_details_list))
            if self.load_to_db.flag:
                self.status_message_label.config(text='Book is Added to Database Successfully Book Code:'+str(self.book_details_list[0]),font=("Arial Bold", 10))


    def check_and_destroy_frame(self,root):
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):
                if child.winfo_name() in ['add_student_frame','update_student_frame','delete_student_frame','add_book_frame','update_book_frame','delete_book_frame','lend_book_frame','update_student_book_frame']:
                    child.destroy()