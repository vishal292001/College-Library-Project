
import tkinter as tk
from tkinter import *
from tkinter import ttk
# from tkinter.ttk import *
from tkinter import Button
from tkinter import messagebox
from tkinter import ttk
from PIL import Image
from PIL import ImageTk



class add_new_student_in_database():
    def __init__(self,root,load_to_db,status_message_label):
        self.root=root
        self.load_to_db=load_to_db
        self.status_message_label=status_message_label
        self.student_table_name='student_details'

        
        pass


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
        self.student_id = self.student_id_text_box.get("1.0", "end-1c")
        if self.student_id in self.student_id_list:
            messagebox.showinfo('information', 'student with this id already exist in database')
            return 0
        else:
            self.load_to_db.load_student_to_database(tuple(self.student_details_list))
            if self.load_to_db.flag:
                self.status_message_label.config(text='Student is Added to Database Successfully StudentID:'+str(self.student_details_list[0]),font=("Arial Bold", 9))


    def check_and_destroy_frame(self,root):
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):
                if child.winfo_name() in ['add_student_frame','update_student_frame','delete_student_frame','add_book_frame','update_book_frame','delete_book_frame','lend_book_frame','update_student_book_frame','delete_lended_book_frame']:
                    child.destroy()