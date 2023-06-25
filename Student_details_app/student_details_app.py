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
        self.add_student_button.place(x=50,y=50)

        self.update_student_button_image = Image.open("./images/update_student_button_img.png")
        self.update_student_button_image = self.update_student_button_image.resize((140, 60))
        self.update_student_button_image = ImageTk.PhotoImage(self.update_student_button_image)
        self.update_student_button = ttk.Button(self.root, text="update student",image=self.update_student_button_image)
        self.update_student_button.place(x=220,y=50)


        self.delete_student_button_image = Image.open("./images/delete_student_button_img.png")
        self.delete_student_button_image = self.delete_student_button_image.resize((140, 60))
        self.delete_student_button_image = ImageTk.PhotoImage(self.delete_student_button_image)
        self.delete_student_button = ttk.Button(self.root, text="delete student",image=self.delete_student_button_image)
        self.delete_student_button.place(x=390,y=50)

        pass

    def add_new_student_frame(self):
        self.student_details_bg_image = tk.PhotoImage(file='./images/student_details_bg_img.png')
        self.student_details_bg_image_label = tk.Label(self.root, bd=0,image=self.student_details_bg_image)
        self.student_details_bg_image_label.place(x=40,y=140)

        self.student_details_image = tk.PhotoImage(file='./images/student_details_img.png')
        self.student_details_image_label = tk.Label(self.root, bd=0,image=self.student_details_image)
        self.student_details_image_label.place(x=90,y=180)

        # self.student_id_image = tk.PhotoImage(file='./images/student_id_img.png')
        # self.student_id_image_label = tk.Label(self.root, bd=0,image=self.student_id_image)
        # self.student_id_image_label.place(x=70,y=200)

        # self.student_name_image = tk.PhotoImage(file='./images/student_name_img.png')
        # self.student_name_image_label = tk.Label(self.root, bd=0,image=self.student_name_image)
        # self.student_name_image_label.place(x=70,y=260)

        # self.student_email_image = tk.PhotoImage(file='./images/student_email_img.png')
        # self.student_email_image_label = tk.Label(self.root, bd=0,image=self.student_email_image)
        # self.student_email_image_label.place(x=70,y=320)

        # self.student_phone_number_image = tk.PhotoImage(file='./images/student_phone_img.png')
        # self.student_phone_number_image_label = tk.Label(self.root, bd=0,image=self.student_phone_number_image)
        # self.student_phone_number_image_label.place(x=70,y=380)


        pass

    def mainloop(self):
        self.root.mainloop()


    

app_instance = Student_Details()
app_instance.mainloop()
