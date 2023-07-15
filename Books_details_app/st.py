import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk






class Student_Details():
    def __init__(self):
        self.root = Tk()
        self.root.title("Student Details App")
        self.root.geometry('1000x650')
        self.root.configure(bg='white')
        self.add_buttons()

    def add_buttons(self):
        self.add_student_button_image = Image.open("./images/add_student_button_img.png")
        self.add_student_button_image = self.add_student_button_image.resize((140, 60))
        self.add_student_button_image = ImageTk.PhotoImage(self.add_student_button_image)
        self.add_student_button = ttk.Button(self.root, text="add student",image=self.add_student_button_image,command=self.add_new_student_frame)
        self.add_student_button.place(x=100,y=50)

        self.update_student_button_image = Image.open("./images/update_student_button_img.png")
        self.update_student_button_image = self.update_student_button_image.resize((140, 60))
        self.update_student_button_image = ImageTk.PhotoImage(self.update_student_button_image)
        self.update_student_button = ttk.Button(self.root, text="update student",image=self.update_student_button_image)
        self.update_student_button.place(x=260,y=50)


        self.delete_student_button_image = Image.open("./images/delete_student_button_img.png")
        self.delete_student_button_image = self.delete_student_button_image.resize((140, 60))
        self.delete_student_button_image = ImageTk.PhotoImage(self.delete_student_button_image)
        self.delete_student_button = ttk.Button(self.root, text="delete student",image=self.delete_student_button_image)
        self.delete_student_button.place(x=420,y=50)

        pass

    def add_new_student_frame(self):
        self.student_details_bg_image = tk.PhotoImage(file='./images/student_details_bg_img.png')
        self.student_details_bg_image_label = tk.Label(self.root, bd=0,image=self.student_details_bg_image)
        self.student_details_bg_image_label.place(x=40,y=140)

        self.student_details_image = tk.PhotoImage(file='./images/student_details_img.png')
        self.student_details_image_label = tk.Label(self.root, bd=0,image=self.student_details_image)
        self.student_details_image_label.place(x=100,y=200)


        self.studen_id_text_box = tk.Text(self.root,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.studen_id_text_box.place(x=280,y=215)

        self.studen_name_text_box = tk.Text(self.root,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.studen_name_text_box.place(x=280,y=265)

        self.studen_email_text_box = tk.Text(self.root,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.studen_email_text_box.place(x=280,y=310)

        self.studen_phone_text_box = tk.Text(self.root,height = 1,width = 25, highlightthickness=1,highlightbackground="black")
        self.studen_phone_text_box.place(x=280,y=360)




        pass

    def mainloop(self):
        self.root.mainloop()


    

app_instance = Student_Details()
app_instance.mainloop()
