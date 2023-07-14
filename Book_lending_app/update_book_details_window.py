import tkinter as tk
from tkinter import *
from tkinter import ttk
# from tkinter.ttk import *
from tkinter import Button
from tkinter import messagebox
from tkinter import ttk
from PIL import Image
from PIL import ImageTk


class update_book_details_window():
    def __init__(self,root,load_to_db,status_message_label):
        self.root=root
        self.load_to_db=load_to_db
        self.status_message_label=status_message_label
        self.book_table_name='books_details'


    def update_book_details(self):
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

    def search_element_in_database(self,element_id,table_name):
        if self.load_to_db.flag==False:
            messagebox.showinfo('information', 'User Authentication is Pending')
            return 0
        self.element_id=element_id
        self.table_name = table_name
        self.dataframe = self.load_to_db.search_in_database(self.table_name)

        self.element_id_list = list(self.dataframe['book_code'])

        if self.element_id in self.element_id_list:
            self.row_index = self.element_id_list.index(self.element_id)
            self.row = self.dataframe.loc[self.row_index]
            self.book_code = self.book_code_text_box.get("1.0", "end-1c")
            self.book_title_text_box.delete("1.0","end")
            self.book_author_text_box.delete("1.0","end")
            self.book_descr_text_box.delete("1.0","end")
            self.book_title_text_box.insert(tk.END,self.row['book_title'])
            self.book_author_text_box.insert(tk.END,self.row['book_author'])
            self.book_descr_text_box.insert(tk.END,self.row['book_description'])

        else:
            messagebox.showinfo('information', 'Book not found')

    def update_book_details_in_database(self):
        self.book_title = self.book_title_text_box.get("1.0", "end-1c")
        self.book_author = self.book_author_text_box.get("1.0", "end-1c")
        self.book_description = self.book_descr_text_box.get("1.0", "end-1c")
        self.load_to_db.update_book_details_in_database(self.book_code,self.book_title,self.book_author,self.book_description)
        if self.load_to_db.flag:
            self.status_message_label.config(text='book details Updated Successfully',fg='green')
        else:
            messagebox.showinfo('information', 'failed to update books details')

    def check_and_destroy_frame(self,root):
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):
                if child.winfo_name() in ['add_student_frame','update_student_frame','delete_student_frame','add_book_frame','update_book_frame','delete_book_frame','lend_book_frame','update_student_book_frame']:
                    child.destroy()