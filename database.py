
# Info:
# --- Reza Tanaki 
# --- 2 Jun. 2022 

# All Tasks of this file (database.py)
# --- 1. Make CSV file for saving data
# --- 2. Get and save data to .csv file
# --- 3. Read Data based on time or period time

# Todo


# --- import libs
import pandas as pd
import os

# --- check if csv file exist
if os.path.isfile("./inc/database.csv"):
    df = pd.read_csv("./inc/database.csv")
else:
    df = pd.DataFrame({'id':[], 'date':[], 'text':[]})


# --- Save and Read last id
def last_func(prv_id=0, read=True):
    # check reading mode or writing mode
    if read:
        f = open("./inc/last_id.txt", "r")
        return int(f.read())

    else:
        f = open("./inc/last_id.txt", "w")
        f.write(str(prv_id))
        f.close()

# --- Data to insert
def insert(date, text):
    last_id = last_func()
    df.loc[len(df)] = [str(last_id+1), date, text]
    last_func(last_id+1, False)

# --- Save to Databane
def saveing(df, path="./inc/database.csv"):
    df.to_csv(path, index=False)

# --- Read data based on certiain day




# insert('dddd', 'reere')
# insert('dddd', 'reere')
# insert('dddd', 'reere')
insert('88888', 'reere')
print(df)
# saveing(df)



