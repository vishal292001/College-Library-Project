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
import duckdb




class delete_lended_book_window():
    def __init__(self,root,load_to_db,status_message_label):
        self.root=root
        self.load_to_db=load_to_db
        self.status_message_label=status_message_label
        self.book_lending_table_name='book_lending_details'
        self.student_table_name='student_details'
        self.book_table_name='books_details'
        self.selected_student_to_lend_book_lst=[]

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

    def delete_lended_book(self):
        if self.load_to_db.flag==False:
            messagebox.showinfo('information', 'User Authentication is Pending')
            return 0
        self.check_and_destroy_frame(self.root)

        self.dataframe = self.load_to_db.search_in_database(self.book_lending_table_name)
        self.student_name_lst_in_database=list(self.dataframe['student_name'])
        self.student_id_lst_in_database=list(self.dataframe['student_id'])

        
        self.book_data_dataframe = self.load_to_db.search_in_database(self.book_table_name)
        self.book_title_lst_in_database = list(self.book_data_dataframe['book_title'])
        self.book_code_lst_in_database = list(self.book_data_dataframe['book_code'])

        self.filter_student_name_list = []
        [self.filter_student_name_list.append(x) for x in self.student_name_lst_in_database if x not in self.filter_student_name_list]

        self.delete_lended_book_frame = Frame(self.root,bg="white",borderwidth=6,width=500,height=500,name='delete_lended_book_frame',highlightbackground="black",highlightthickness=2)
        self.delete_lended_book_frame.place(x=260,y=140)

        self.enter_student_id_image_label = tk.Label(self.delete_lended_book_frame, bd=0,image=self.enter_student_id_image_lend_win)
        self.enter_student_id_image_label.place(x=10,y=20)

        self.student_id_combobox_var = tk.StringVar()
        self.student_id_combobox = ttk.Combobox(self.delete_lended_book_frame, width = 24,values=self.filter_student_name_list, textvariable=self.student_id_combobox_var)
        self.student_id_combobox.place(x=12,y=75)

        self.search_button_student = Button(self.delete_lended_book_frame,image=self.search_icon_img,borderwidth=0,background='white',command=lambda:self.find_student_to_delete_lended_book(self.delete_lended_book_frame))
        self.search_button_student.place(x=140,y=22)


        self.delete_student_book_button = ttk.Button(self.delete_lended_book_frame, text="Return",command=self.return_lended_book)
        self.delete_student_book_button.place(x=160,y=440)

        self.cancel_delete_student_book_button = ttk.Button(self.delete_lended_book_frame, text="Cancel")
        self.cancel_delete_student_book_button.place(x=240,y=440)
        pass





    def find_student_to_delete_lended_book(self,frame):
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

        self.diplay_currently_alloted_book(self.frame)

    def remove_selected_student(self):
        self.diaplay_student_name_label.destroy()
        self.close_student_name_label_button.destroy()
        self.diaplay_id_label.destroy()
        self.close_student_id_label_button.destroy()
        self.selected_student_to_lend_book_lst=[]

    def diplay_currently_alloted_book(self,frame):
        self.frame = frame

        self.currently_alloted_book_frame = Frame(self.frame,bg="white",borderwidth=6,width=210,height=210,name='currently_alloted_book_frame',highlightbackground="black",highlightthickness=2)
        self.currently_alloted_book_frame.place(x=260,y=22)

        self.current_alloted_book_icon = tk.Label(self.currently_alloted_book_frame, text='Select Books to Returned',font=("Arial Bold", 10),fg="#2f5597",bg='white',borderwidth=1, relief="solid",width=20)
        self.current_alloted_book_icon.place(x=6,y=2)

        book_lending_details_dataframe=self.load_to_db.search_in_database(self.book_lending_table_name)
        selected_student_id=self.user_input_id
        self.previously_alloted_book_df = duckdb.query("select * from book_lending_details_dataframe where student_id='%s'"%selected_student_id).df()
        self.previously_alloted_book_list = list(self.previously_alloted_book_df['book_title'])
        self.diaplay_book_name_label_lst=[]
        self.check_box_selected_book_name=[]
        self.check_box_list=[]
        self.diaplay_book_name_label_y_pos=50
        for book_name in self.previously_alloted_book_list:
            self.diaplay_book_name_label = tk.Label(self.currently_alloted_book_frame, text=book_name,font=("Arial Bold", 11),fg="#2f5597",bg='white',borderwidth=1, relief="solid",width=18)
            self.diaplay_book_name_label.place(x=0,y=self.diaplay_book_name_label_y_pos)

            self.check_box_status = tk.IntVar()
            self.select_book_check_box = tk.Checkbutton(self.currently_alloted_book_frame,variable=self.check_box_status,bg='alice blue')
            self.select_book_check_box.place(x=170,y=self.diaplay_book_name_label_y_pos)

            self.diaplay_book_name_label_lst.append(self.diaplay_book_name_label)
            self.check_box_selected_book_name.append(self.check_box_status)
            self.check_box_list.append(self.select_book_check_box)
            self.diaplay_book_name_label_y_pos+=30
        pass


    def return_lended_book(self):
        self.book_to_return =[]
        for i in self.check_box_selected_book_name:
            if i.get()==1:
                self.index = self.check_box_selected_book_name.index(i)
                self.book_title = self.previously_alloted_book_list[self.index]
                self.book_to_return.append(self.book_title)
                self.load_to_db.remove_book_lending_record(self.user_input_id, self.book_title)
                self.diaplay_book_name_label_lst[self.index].destroy()
                self.check_box_list[self.index].destroy()
                self.diaplay_book_name_label_lst.pop(self.index)

        conn = duckdb.connect(database=':memory:')
        conn.register('previously_alloted_book_df', self.previously_alloted_book_df)

        self.query = f"select book_code, book_title,book_author,book_description from previously_alloted_book_df where book_title IN {tuple(self.book_to_return)}"
        self.books_to_return_df = conn.query(self.query).fetchdf()
        self.load_to_db.books_to_be_return(self.books_to_return_df)
        if self.load_to_db.flag:
            self.status_message_label.config(text='Book Returned Succsessfully',font=("Arial Bold", 9))



    def check_and_destroy_frame(self,root):
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):
                if child.winfo_name() in ['add_student_frame','update_student_frame','delete_student_frame','add_book_frame','update_book_frame','delete_book_frame','lend_book_frame','update_student_book_frame','delete_lended_book_frame']:
                    child.destroy()