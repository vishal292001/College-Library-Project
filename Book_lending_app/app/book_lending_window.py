import tkinter as tk
from tkinter import *
from tkinter import ttk
# from tkinter.ttk import *
from tkinter import Button
from tkinter import messagebox
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from tkcalendar import Calendar
from tkcalendar import DateEntry
import pandas as pd


class book_lending_window():
    def __init__(self,root,load_to_db,status_message_label):
        self.root=root
        self.load_to_db=load_to_db
        self.status_message_label=status_message_label
        self.book_lending_table_name='book_lending_details'
        self.student_table_name='student_details'
        self.book_table_name='books_details'
 
        self.enter_student_id_image_lend_win = Image.open("./app/images/enter_student_id_img.png")
        self.enter_student_id_image_lend_win = self.enter_student_id_image_lend_win.resize((120, 50))
        self.enter_student_id_image_lend_win = ImageTk.PhotoImage(self.enter_student_id_image_lend_win)

        self.search_icon_img = Image.open("./app/images/search_icon.png")
        self.search_icon_img = self.search_icon_img.resize((40, 40))
        self.search_icon_img = ImageTk.PhotoImage(self.search_icon_img)

        
        self.close_icon_img = Image.open("./app/images/close_icon.png")
        self.close_icon_img = self.close_icon_img.resize((20, 20))
        self.close_icon_img = ImageTk.PhotoImage(self.close_icon_img)


        self.enter_book_code_image_lend_win = Image.open("./app/images/enter_book_code_img.png")
        self.enter_book_code_image_lend_win = self.enter_book_code_image_lend_win.resize((120, 50))
        self.enter_book_code_image_lend_win = ImageTk.PhotoImage(self.enter_book_code_image_lend_win)

    def lend_book_from_library(self):
        if self.load_to_db.flag==False:
            messagebox.showinfo('information', 'User Authentication is Pending')
            return 0
        self.check_and_destroy_frame(self.root)
        self.diaplay_book_name_label_y_pos = 120
        self.selected_book_list = []
        self.diaplay_book_name_label_lst=[]
        self.close_book_name_label_button_lst =[]
        self.selected_student_to_lend_book_lst = []

        self.dataframe = self.load_to_db.search_in_database(self.student_table_name)
        self.student_name_lst_in_database=list(self.dataframe['student_name'])
        self.student_id_lst_in_database=list(self.dataframe['student_id'])

        self.book_data_dataframe = self.load_to_db.search_in_database(self.book_table_name)
        self.book_title_lst_in_database = list(self.book_data_dataframe['book_title'])
        self.book_code_lst_in_database = list(self.book_data_dataframe['book_code'])

        self.lend_book_frame = Frame(self.root,bg="white",borderwidth=6,width=500,height=500,name='lend_book_frame',highlightbackground="black",highlightthickness=2)
        self.lend_book_frame.place(x=260,y=140)

        self.sub_frame = Frame(self.lend_book_frame,bg="white",borderwidth=6,width=500,height=50,highlightbackground="black",highlightthickness=2)
        self.sub_frame.place(x=-8,y=442)

        self.enter_student_id_image_label = tk.Label(self.lend_book_frame, bd=0,image=self.enter_student_id_image_lend_win)
        self.enter_student_id_image_label.place(x=10,y=20)

        self.student_id_combobox_var = tk.StringVar()
        self.student_id_combobox = ttk.Combobox(self.lend_book_frame, width = 24,values=self.student_name_lst_in_database, textvariable=self.student_id_combobox_var)
        self.student_id_combobox.place(x=12,y=75)

        self.search_button_student = Button(self.lend_book_frame,image=self.search_icon_img,borderwidth=0,background='white',command=lambda:self.find_student_to_lend_book(self.lend_book_frame))
        self.search_button_student.place(x=140,y=22)

                
        self.enter_book_code_image_label = tk.Label(self.lend_book_frame, bd=0,image=self.enter_book_code_image_lend_win)
        self.enter_book_code_image_label.place(x=295,y=20)
        
        self.search_button_book = Button(self.lend_book_frame,image=self.search_icon_img,borderwidth=0,background='white',command=lambda:self.find_book_to_lend(self.lend_book_frame))
        self.search_button_book.place(x=420,y=22)

        self.book_code_combobox_var = tk.StringVar()
        self.book_code_combobox = ttk.Combobox(self.lend_book_frame, width = 24,values=self.book_title_lst_in_database, textvariable=self.book_code_combobox_var)
        self.book_code_combobox.place(x=295,y=75)


        self.from_date_calender=DateEntry(self.lend_book_frame,selectmode='day')
        self.from_date_calender.place(x=10,y=190)
        self.from_date_label = tk.Label(self.lend_book_frame, text="From Date",font=("Arial Bold", 11),fg="#2f5597",bg='white')
        self.from_date_label.place(x=110,y=190)

        self.to_date_calender=DateEntry(self.lend_book_frame,selectmode='day')
        self.to_date_calender.place(x=10,y=216)
        self.to_date_label = tk.Label(self.lend_book_frame, text="Return Date",font=("Arial Bold", 11),fg="#2f5597",bg='white')
        self.to_date_label.place(x=110,y=216)


        self.allot_book_button = ttk.Button(self.lend_book_frame, text="Allot Book",command=self.allot_book_to_student)
        self.allot_book_button.place(x=140,y=456)

        self.allot_book_cancel_button = ttk.Button(self.lend_book_frame, text="Cancel")
        self.allot_book_cancel_button.place(x=220,y=456)
        pass




    def find_student_to_lend_book(self,frame):
        self.frame = frame
        self.user_input = self.student_id_combobox.get()
        if self.user_input in self.student_name_lst_in_database or self.user_input in self.student_id_lst_in_database:
             if self.user_input in self.student_name_lst_in_database:
                 self.index_no = self.student_name_lst_in_database.index(self.user_input)
                 self.row_data = self.dataframe.loc[self.index_no]
                 self.user_input_id = self.row_data['student_id']
                 self.user_input=self.user_input
                 pass
             elif self.user_input in self.student_id_lst_in_database:
                 self.index_no = self.student_id_lst_in_database.index(self.user_input)
                 self.row_data = self.dataframe.loc[self.index_no]
                 self.user_input_id = self.user_input
                 self.user_input=self.row_data['student_name']

             pass
        else:
             messagebox.showinfo('information', 'Student not found')
             return 0


        if len(self.selected_student_to_lend_book_lst)>0:
            for i in self.selected_student_to_lend_book_lst:
                i.destroy()
            for j in self.selected_student_to_lend_book_lst:
                self.selected_student_to_lend_book_lst.pop()
                self.selected_student_to_lend_book_lst.pop()
                self.selected_student_to_lend_book_lst.pop()
                self.selected_student_to_lend_book_lst.pop()

        if len(self.selected_student_to_lend_book_lst)==0:
            self.diaplay_id_label = tk.Label(self.frame, text="Student ID:"+self.user_input_id,font=("Arial Bold", 11),fg="#2f5597",bg='white',borderwidth=1, relief="solid",width=18)
            self.diaplay_id_label.place(x=12,y=110)
    
            self.close_student_id_label_button = Button(self.frame,image=self.close_icon_img,borderwidth=0,background='white',command=self.remove_selected_student)
            self.close_student_id_label_button.place(x=180,y=110)

            self.diaplay_student_name_label = tk.Label(self.frame, text=self.user_input,font=("Arial Bold", 11),fg="#2f5597",bg='white',borderwidth=1, relief="solid",width=18)
            self.diaplay_student_name_label.place(x=12,y=140)

            self.close_student_name_label_button = Button(self.frame,image=self.close_icon_img,borderwidth=0,background='white',command=self.remove_selected_student)
            self.close_student_name_label_button.place(x=180,y=140)

            self.selected_student_to_lend_book_lst.append(self.diaplay_student_name_label)
            self.selected_student_to_lend_book_lst.append(self.close_student_name_label_button)
            self.selected_student_to_lend_book_lst.append(self.diaplay_id_label)
            self.selected_student_to_lend_book_lst.append(self.close_student_id_label_button)

    def remove_selected_student(self):
        self.diaplay_student_name_label.destroy()
        self.close_student_name_label_button.destroy()
        self.diaplay_id_label.destroy()
        self.close_student_id_label_button.destroy()
        self.selected_student_to_lend_book_lst=[]




    def find_book_to_lend(self,frame):
        self.frame = frame

        self.book_user_input = self.book_code_combobox.get()
    
        if self.book_user_input in self.book_title_lst_in_database or self.book_user_input in self.book_code_lst_in_database:
             if self.book_user_input in self.book_title_lst_in_database:
                 pass
             elif self.book_user_input in self.book_code_lst_in_database:
                 self.index_no = self.book_code_lst_in_database.index(self.book_user_input)
                 self.row_data = self.book_data_dataframe.loc[self.index_no]
                 self.book_user_input=self.row_data['book_title']

             pass
        else:
             messagebox.showinfo('information', 'Book not found')
             return 0

        if len(self.selected_book_list)==4:
            messagebox.showinfo('information', 'maximum four book can be assigne to student')
            return 0

        if self.book_user_input not in self.selected_book_list:
            self.selected_book_list.append(self.book_user_input)
            self.diaplay_book_name_label = tk.Label(self.frame, text=self.book_user_input,font=("Arial Bold", 11),fg="#2f5597",bg='white',borderwidth=1, relief="solid",width=18)
            self.diaplay_book_name_label.place(x=295,y=self.diaplay_book_name_label_y_pos)

            self.label_var=tk.StringVar()
            self.close_book_name_label_button = tk.Label(self.frame,image=self.close_icon_img,textvariable=self.label_var)
            self.close_book_name_label_button.place(x=465,y=self.diaplay_book_name_label_y_pos)
            self.close_book_name_label_button.bind("<Button-1>", lambda event,book_name_label =self.diaplay_book_name_label,close_book_name_icon=self.close_book_name_label_button,book_name=self.book_user_input: self.remove_selected_book(book_name_label,close_book_name_icon,book_name))

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


    def allot_book_to_student(self):
        self.selected_student_id=str(self.diaplay_id_label.cget("text")).split(':')
        self.selected_student_id_list=[]
        self.selected_student_name_list =[]
        self.selected_book_code_list=[]
        self.selected_book_author_list=[]
        self.selected_book_description_list=[]
        self.from_date_list=[]
        self.to_date_list=[]
        self.selected_data_dataframe= self.load_to_db.search_in_database(self.book_table_name)
        self.book_data_book_title_list = list(self.selected_data_dataframe['book_title'])
        for i in self.selected_book_list:
            self.index = self.book_data_book_title_list.index(i)
            self.record = self.selected_data_dataframe.loc[self.index]
            self.selected_book_code_list.append(self.record['book_code'])
            self.selected_book_author_list.append(self.record['book_author'])
            self.selected_book_description_list.append(self.record['book_description'])
            self.selected_student_id_list.append(self.selected_student_id[1])
            self.selected_student_name_list.append(self.diaplay_student_name_label.cget("text"))
            self.from_date_list.append(self.from_date_calender.get_date())
            self.to_date_list.append(self.to_date_calender.get_date())

        self.book_lending_data_to_be_load={'student_id':self.selected_student_id_list,
                                           'student_name':self.selected_student_name_list,
                                           'book_code':self.selected_book_code_list,
                                           'book_title':self.selected_book_list,
                                           'book_author':self.selected_book_author_list,
                                           'book_description':self.selected_book_description_list,   
                                           'assigne_date':self.from_date_list,
                                           'return_date':self.to_date_list
                                           }
        
        
        self.book_lending_data_to_be_load_dataframe = pd.DataFrame(self.book_lending_data_to_be_load)
        print(self.book_lending_data_to_be_load_dataframe)
        self.load_to_db.load_book_lending_details(self.book_lending_data_to_be_load_dataframe)
        if self.load_to_db.flag:
            self.status_message_label.config(text='books alloted to student successfully',fg='green')
        else:
            messagebox.showinfo('information', 'failed to update books details')

        for i in self.selected_book_code_list:
            self.load_to_db.delete_book_from_database(i)


    def check_and_destroy_frame(self,root):
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):
                if child.winfo_name() in ['add_student_frame','update_student_frame','delete_student_frame','add_book_frame','update_book_frame','delete_book_frame','lend_book_frame','update_student_book_frame','delete_lended_book_frame']:
                    child.destroy()