import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk




class Books_Details():
    def __init__(self):
        self.root = Tk()
        self.root.title("Books Details App")
        self.root.geometry('1000x650')
        self.root.configure(bg='white')
        self.add_buttons()

    def add_buttons(self):
        self.add_book_button_image = Image.open("Book_details_app/images/add_book_btn_img.png")
        self.add_book_button_image = self.add_book_button_image.resize((140, 60))
        self.add_book_button_image = ImageTk.PhotoImage(self.add_book_button_image)
        self.add_book_button = ttk.Button(self.root, text="add student",image=self.add_book_button_image,command=self.add_new_book_frame)
        self.add_book_button.place(x=100,y=50)

        self.update_book_button_image = Image.open("Book_details_app/images/update_book_btn_image.png")
        self.update_book_button_image = self.update_book_button_image.resize((140, 60))
        self.update_book_button_image = ImageTk.PhotoImage(self.update_book_button_image)
        self.update_book_button = ttk.Button(self.root, text="update student",image=self.update_book_button_image)
        self.update_book_button.place(x=260,y=50)


        self.delete_book_button_image = Image.open("Book_details_app/images/delete_book_btn_img.png")
        self.delete_book_button_image = self.delete_book_button_image.resize((140, 60))
        self.delete_book_button_image = ImageTk.PhotoImage(self.delete_book_button_image)
        self.delete_book_button = ttk.Button(self.root, text="delete student",image=self.delete_book_button_image)
        self.delete_book_button.place(x=420,y=50)

        pass

    def add_new_book_frame(self):
        self.book_details_bg_image = tk.PhotoImage(file='Book_details_app/images/book_details_bg_img copy.png')
        self.book_details_bg_image_label = tk.Label(self.root, bd=0,image=self.book_details_bg_image)
        self.book_details_bg_image_label.place(x=40,y=140)

        self.book_details_image = tk.PhotoImage(file='Book_details_app/images/book_details_image.png')
        self.book_details_image_label = tk.Label(self.root, bd=0,image=self.book_details_image)
        self.book_details_image_label.place(x=100,y=200)


        self.book_name_text_box = tk.Text(self.root,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.book_name_text_box.place(x=290,y=215)

        self.book_author_text_box = tk.Text(self.root,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.book_author_text_box.place(x=290,y=275)

        self.book_description_text_box = tk.Text(self.root,height = 2,width = 25, highlightthickness=1,highlightbackground="black")
        self.book_description_text_box.place(x=290,y=330)

        self.book_code_text_box = tk.Text(self.root,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.book_code_text_box.place(x=290,y=405)




        pass

    def mainloop(self):
        self.root.mainloop()


    

app_instance = Books_Details()
app_instance.mainloop()
