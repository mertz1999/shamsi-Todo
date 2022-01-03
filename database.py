
# Info:
# --- Project name : Todo list (shamsi date)
# --- Autor        : Reza Tanakizadeh
# --- Date         : 2 Jun. 2022 

# All Tasks of this file (database.py)
# --- 1. Make CSV file for saving data
# --- 2. Get and save data to .csv file
# --- 3. Read Data based on time or period time


# --- import libs
import pandas as pd
import os


# --- Define a Class That we use it for Database managment in this project
class database():
    # initialize function
    def __init__(self, database_path="./inc/database.csv"):
        self.database_path = database_path
        self.last_id = int(0)
        # check if csv file exist
        if os.path.isfile(database_path):
            self.df = pd.read_csv(self.database_path)
        else:
            self.df = pd.DataFrame({'id':[], 'date':[], 'text':[]})
    
    # Insert Data to database
    def insert(self, date, text):
        self.last_id = self.last_func()
        self.df.loc[len(self.df)] = [str(self.last_id+1), date, text]
        self.last_func(self.last_id+1, False)
        self.saving()

    # Save and Read Last id number
    def last_func(self, prv_id=0, read=True):
        if read:
            f = open("./inc/last_id.txt", "r")
            return int(f.read())
        else:
            f = open("./inc/last_id.txt", "w")
            f.write(str(prv_id))
            f.close()
    
    # save .csv file
    def saving(self):
        self.df.to_csv(self.database_path, index=False)
    
    # Read Data
    def read(self, date):
        result = self.df.loc[self.df['date'] == date]
        return result
        
    
    


# temp = database()
# temp.insert("12ba", "Call to mum!")


# insert('dddd', 'reere')
# insert('dddd', 'reere')
# insert('dddd', 'reere')
# insert('88888', 'reere')
# print(temp.read("88888"))
# saving(df)



