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



class update_lended_book_window():
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







    def update_lended_book(self):
        if self.load_to_db.flag==False:
            messagebox.showinfo('information', 'User Authentication is Pending')
            return 0
        self.check_and_destroy_frame(self.root)
        self.diaplay_add_new_book_name_label_y_pos=120
        self.selected_student_to_lend_book_lst = []
        self.diaplay_new_book_name_label_lst=[]
        self.close_new_book_name_label_button_lst=[]
        self.selected_book_list=[]

        self.dataframe = self.load_to_db.search_in_database(self.book_lending_table_name)
        self.student_name_lst_in_database=list(self.dataframe['student_name'])
        self.student_id_lst_in_database=list(self.dataframe['student_id'])

        
        self.book_data_dataframe = self.load_to_db.search_in_database(self.book_table_name)
        self.book_title_lst_in_database = list(self.book_data_dataframe['book_title'])
        self.book_code_lst_in_database = list(self.book_data_dataframe['book_code'])

        self.filter_student_name_list = []
        [self.filter_student_name_list.append(x) for x in self.student_name_lst_in_database if x not in self.filter_student_name_list]

        self.update_student_book_frame = Frame(self.root,bg="white",borderwidth=6,width=560,height=500,name='update_student_book_frame',highlightbackground="black",highlightthickness=2)
        self.update_student_book_frame.place(x=260,y=140)

        self.enter_student_id_image_label = tk.Label(self.update_student_book_frame, bd=0,image=self.enter_student_id_image_lend_win)
        self.enter_student_id_image_label.place(x=10,y=20)

        self.student_id_combobox_var = tk.StringVar()
        self.student_id_combobox = ttk.Combobox(self.update_student_book_frame, width = 24,values=self.filter_student_name_list, textvariable=self.student_id_combobox_var)
        self.student_id_combobox.place(x=12,y=75)

        self.search_button_student = Button(self.update_student_book_frame,image=self.search_icon_img,borderwidth=0,background='white',command=lambda:self.find_student_to_lend_book(self.update_student_book_frame))
        self.search_button_student.place(x=140,y=22)

        self.enter_book_code_image_label = tk.Label(self.update_student_book_frame, bd=0,image=self.enter_book_code_image_lend_win)
        self.enter_book_code_image_label.place(x=295,y=20)
        
        self.search_button_book = Button(self.update_student_book_frame,image=self.search_icon_img,borderwidth=0,background='white',command=lambda:self.find_book_to_lend(self.update_student_book_frame))
        self.search_button_book.place(x=420,y=22)

        self.book_code_combobox_var = tk.StringVar()
        self.book_code_combobox = ttk.Combobox(self.update_student_book_frame, width = 24,values=self.book_title_lst_in_database, textvariable=self.book_code_combobox_var)
        self.book_code_combobox.place(x=295,y=75)


        self.from_date_calender=DateEntry(self.update_student_book_frame,selectmode='day')
        self.from_date_calender.place(x=295,y=240)
        self.from_date_label = tk.Label(self.update_student_book_frame, text="From Date",font=("Arial Bold", 11),fg="#2f5597",bg='white')
        self.from_date_label.place(x=390,y=240)

        self.to_date_calender=DateEntry(self.update_student_book_frame,selectmode='day')
        self.to_date_calender.place(x=295,y=264)
        self.to_date_label = tk.Label(self.update_student_book_frame, text="Return Date",font=("Arial Bold", 11),fg="#2f5597",bg='white')
        self.to_date_label.place(x=390,y=264)

        self.update_student_book_button = ttk.Button(self.update_student_book_frame, text="update",command=self.update_book_lending_details)
        self.update_student_book_button.place(x=160,y=440)

        self.cancel_Update_student_book_button = ttk.Button(self.update_student_book_frame, text="Cancel")
        self.cancel_Update_student_book_button.place(x=240,y=440)
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

        if self.frame.winfo_name()=='update_student_book_frame':
                self.diplay_currently_alloted_book(self.frame)



    def remove_selected_student(self):
        self.diaplay_student_name_label.destroy()
        self.close_student_name_label_button.destroy()
        self.diaplay_id_label.destroy()
        self.close_student_id_label_button.destroy()
        self.selected_student_to_lend_book_lst=[]

    def diplay_currently_alloted_book(self,frame):
        self.frame = frame

        self.currently_alloted_book_frame = Frame(self.frame,bg="white",borderwidth=6,width=210,height=180,name='currently_alloted_book_frame',highlightbackground="black",highlightthickness=2)
        self.currently_alloted_book_frame.place(x=10,y=190)

        self.current_alloted_book_icon = tk.Label(self.currently_alloted_book_frame, text='Current Alloted Books',font=("Arial Bold", 11),fg="#2f5597",bg='white',borderwidth=1, relief="solid",width=18)
        self.current_alloted_book_icon.place(x=6,y=2)

        book_lending_details_dataframe=self.load_to_db.search_in_database(self.book_lending_table_name)
        selected_student_id=self.user_input_id
        self.previously_alloted_book_df = duckdb.query("select * from book_lending_details_dataframe where student_id='%s'"%selected_student_id).df()
        self.previously_alloted_book_list = list(self.previously_alloted_book_df['book_title'])
        print(self.previously_alloted_book_df)
        self.diaplay_book_name_label_lst=[]
        self.close_book_name_label_button_lst=[]
        self.diaplay_book_name_label_y_pos=50
        for book_name in self.previously_alloted_book_list:
            self.diaplay_book_name_label = tk.Label(self.currently_alloted_book_frame, text=book_name,font=("Arial Bold", 11),fg="#2f5597",bg='white',borderwidth=1, relief="solid",width=18)
            self.diaplay_book_name_label.place(x=0,y=self.diaplay_book_name_label_y_pos)

            self.label_var=tk.StringVar()
            self.close_book_name_label_button = tk.Label(self.currently_alloted_book_frame,image=self.close_icon_img,textvariable=self.label_var)
            self.close_book_name_label_button.place(x=170,y=self.diaplay_book_name_label_y_pos)
            self.close_book_name_label_button.bind("<Button-1>", lambda event,book_name_label =self.diaplay_book_name_label,close_book_name_icon=self.close_book_name_label_button,book_name=book_name: self.remove_selected_book(book_name_label,close_book_name_icon,book_name))

            self.diaplay_book_name_label_lst.append(self.diaplay_book_name_label)
            self.close_book_name_label_button_lst.append(self.close_book_name_label_button)
            self.diaplay_book_name_label_y_pos+=30
        pass

    def remove_selected_book(self,book_name_label,close_book_name_icon,book_name):
        
        book_name_label.destroy()
        close_book_name_icon.destroy()
        self.previously_alloted_book_list.remove(book_name)
        self.diaplay_book_name_label_lst.remove(book_name_label)
        self.close_book_name_label_button_lst.remove(close_book_name_icon)
        self.diaplay_book_name_label_y_pos-=30
        self.diaplay_book_name_label_y_pos=50
        if len(self.previously_alloted_book_list)>0:
            self.diaplay_book_name_label_y_pos=50
            for i in self.diaplay_book_name_label_lst:
                i.place(x=0,y=self.diaplay_book_name_label_y_pos)
                self.diaplay_book_name_label_y_pos+=30
            self.diaplay_book_name_label_y_pos=50
            for j in self.close_book_name_label_button_lst:
                j.place(x=170,y=self.diaplay_book_name_label_y_pos)
                self.diaplay_book_name_label_y_pos+=30


    def remove_new_selected_book(self,book_name_label,close_book_name_icon,book_name):
        
        book_name_label.destroy()
        close_book_name_icon.destroy()
 
        self.selected_book_list.remove(book_name)
        self.diaplay_new_book_name_label_lst.remove(book_name_label)
        self.close_new_book_name_label_button_lst.remove(close_book_name_icon)
        self.diaplay_add_new_book_name_label_y_pos-=30
        self.diaplay_add_new_book_name_label_y_pos=120
        if len(self.selected_book_list)>0:
            self.diaplay_add_new_book_name_label_y_pos=120
            for i in self.diaplay_new_book_name_label_lst:
                i.place(x=295,y=self.diaplay_add_new_book_name_label_y_pos)
                self.diaplay_add_new_book_name_label_y_pos+=30
            self.diaplay_add_new_book_name_label_y_pos=120
            for j in self.close_new_book_name_label_button_lst:
                j.place(x=465,y=self.diaplay_add_new_book_name_label_y_pos)
                self.diaplay_add_new_book_name_label_y_pos+=30





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

        print(self.previously_alloted_book_list)
        print(self.selected_book_list)
        if self.book_user_input in self.previously_alloted_book_list:
            messagebox.showinfo('information', 'this book is already assigned to this student')
            return 0
        if len(self.selected_book_list)+len(self.previously_alloted_book_list)==4:
            messagebox.showinfo('information', 'maximum four book can be assigne to student')
            return 0

        if self.book_user_input not in self.selected_book_list:
            self.selected_book_list.append(self.book_user_input)
            self.diaplay_new_book_name_label = tk.Label(self.frame, text=self.book_user_input,font=("Arial Bold", 11),fg="#2f5597",bg='white',borderwidth=1, relief="solid",width=18)
            self.diaplay_new_book_name_label.place(x=295,y=self.diaplay_add_new_book_name_label_y_pos)

            self.label_var=tk.StringVar()
            self.close_new_book_name_label_button = tk.Label(self.frame,image=self.close_icon_img,textvariable=self.label_var)
            self.close_new_book_name_label_button.place(x=465,y=self.diaplay_add_new_book_name_label_y_pos)
            self.close_new_book_name_label_button.bind("<Button-1>", lambda event,book_name_label =self.diaplay_new_book_name_label,close_book_name_icon=self.close_new_book_name_label_button,book_name=self.book_user_input: self.remove_new_selected_book(book_name_label,close_book_name_icon,book_name))

            self.diaplay_new_book_name_label_lst.append(self.diaplay_new_book_name_label)
            self.close_new_book_name_label_button_lst.append(self.close_new_book_name_label_button)
            self.diaplay_add_new_book_name_label_y_pos+=30



    def update_book_lending_details(self):
        print(self.selected_book_list)
        print(self.previously_alloted_book_list)
        self.previously_alloted_book_list_constant = list(self.previously_alloted_book_df['book_title'])
        print(self.previously_alloted_book_list_constant)
        self.records_to_be_removed = []
        self.records_to_be_insert = []
        self.books_to_return =[]
        self.records_to_be_insert.extend(self.selected_book_list)
        for i in self.previously_alloted_book_list_constant:
            if i not in self.previously_alloted_book_list:
                self.records_to_be_removed.append(i)
        
        self.books_to_return.extend(self.records_to_be_removed)

        for book_name in self.records_to_be_removed:
            self.load_to_db.remove_book_lending_record(self.user_input_id,book_name)

        self.data_to_be_inserted = {}
        self.student_id=[]
        self.student_name=[]
        self.book_code=[]
        self.book_title=[]
        self.book_author=[]
        self.book_description=[]
        self.assigne_date=[]
        self.return_date=[]
        self.book_data_dataframe
        self.book_title_lst_in_database
        for i in self.records_to_be_insert:
            self.index = self.book_title_lst_in_database.index(i)
            self.record= self.book_data_dataframe.loc[self.index]
            self.student_id.append(self.user_input_id)
            self.student_name.append(self.user_input)
            self.book_code.append(self.record['book_code'])
            self.book_title.append(i)
            self.book_author.append(self.record['book_author'])
            self.book_description.append(self.record['book_description'])
            self.assigne_date.append(self.from_date_calender.get_date())
            self.return_date.append(self.to_date_calender.get_date())

        self.book_lending_data_to_be_load={'student_id':self.student_id,
                                           'student_name':self.student_name,
                                           'book_code':self.book_code,
                                           'book_title':self.book_title,
                                           'book_author':self.book_author,
                                           'book_description':self.book_description,   
                                           'assigne_date':self.assigne_date,
                                           'return_date':self.return_date
                                           }            

        self.book_lending_data_to_be_load_dataframe = pd.DataFrame(self.book_lending_data_to_be_load)
        print(self.book_lending_data_to_be_load_dataframe)
        self.load_to_db.load_book_lending_details(self.book_lending_data_to_be_load_dataframe)
        if self.load_to_db.flag:
            self.status_message_label.config(text='book lending data updated successfully',fg='green')
        else:
            messagebox.showinfo('information', 'failed to update lending books details')
        conn = duckdb.connect(database=':memory:')
        conn.register('previously_alloted_book_df', self.previously_alloted_book_df)

        self.query = f"select book_code, book_title,book_author,book_description from previously_alloted_book_df where book_title IN {tuple(self.books_to_return)}"
        self.books_to_return_df = conn.query(self.query).fetchdf()
        self.load_to_db.books_to_be_return(self.books_to_return_df)


    def check_and_destroy_frame(self,root):
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):
                if child.winfo_name() in ['add_student_frame','update_student_frame','delete_student_frame','add_book_frame','update_book_frame','delete_book_frame','lend_book_frame','update_student_book_frame','delete_lended_book_frame']:
                    child.destroy()