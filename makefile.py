# Info:
# --- Project name : Todo list (shamsi date)
# --- Autor        : Reza Tanakizadeh
# --- Date         : 2 Jun. 2022 

# All Tasks of this file (makefile.py)
# --- 1. based on input dataframe make a file for user that can
#        see their Tasks

# --- import libs
import pandas as pd

# --- Make Makefile class
class makefile():
    def __init__(self, date, text_list, id):
        # initilize variables
        self.date = date
        self.text_list = text_list
        self.id = id
        self.date_dict = {"fa":"Farvardin",
                          "or":"Ordibehesht",
                          "kh":"Khordad",
                          "ti":"Tir",
                          "mo":"Mordad",
                          "sh":"Shahrivar",
                          "me":"Mehr",
                          "ab":"Aban",
                          "az":"Azar",
                          "de":"Dey",
                          "ba":"Bahman",
                          "es":"Esfand"}
        # write to file based on write_to_file() function
        self.write_to_file()

    # write to file function
    def write_to_file(self):
        #  Make header string
        path = "./todo/"+self.date+".txt"
        header = "-"*15 + " " + self.date[0:-2] + " " + self.date_dict[date[-2::]] + " " +"-"*15

        #  Make and open file
        f = open(path, "w")

        #  Write header to file
        f.write('-'*len(header))
        f.write("\n")
        f.write(header)
        f.write("\n")
        f.write("\n")
        f.write("\n")    
           
        #  write all Todo Tasks
        for idx, text in enumerate(self.text_list):
            f.write("{}. ({}) {}".format(str(idx+1), "0"*(4-len(self.id[idx]))+self.id[idx], text))
            f.write("\n")
        f.close()




        

# --- input data
date = "30ba"
text_list = ["Call to mr.ebrahimi at 8PM","Read PM book","Face Recognition Project"]
id = ["1", "5", "105"]

temp = makefile(date, text_list, id)
temp.write_to_file()



