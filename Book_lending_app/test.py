import duckdb
import database_loaders



class test_code():
    def __init__(self):
        self.load_to_db = database_loaders.Load_to_Database()
        self.book_lending_table_name='book_lending_details'
        self.load_to_db.connect_to_postgres('localhost','Library','postgres','1234')

        pass

    def diplay_previously_alloted_book(self):
        
            book_lending_details_dataframe=self.load_to_db.search_in_database(self.book_lending_table_name)
            # duckdb.query("select count(*) as billable_cnt from df where dm_name = 'sanket' and Exection_hub='iDEAS-DIGITAL-EXECUTION HUB-EUROPE' and billable_cat='%s'" %i).df()
            print(book_lending_details_dataframe)
            self.previously_alloted_book_df = duckdb.query("select * from book_lending_details_dataframe where student_id='1001'").df()
            print(self.previously_alloted_book_df)
            pass


inst = test_code()
inst.diplay_previously_alloted_book()
