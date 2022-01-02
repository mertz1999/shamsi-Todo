# Info:
# --- Project name : Todo list (shamsi date)
# --- Autor        : Reza Tanakizadeh
# --- Date         : 2 Jun. 2022 

# All Tasks of this file (makefile.py)
# --- 1. based on input dataframe make a file for user that can
#        see their Tasks

# --- import libs
import pandas as pd

# --- input data
date = "8az"
text = ["Call to mr.ebrahimi at 8PM","Read PM book"]

# --- Dictionary of month
date_dict = {"fa":"Farvardin",
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


path = "./todo/"+date+".txt"
header = "-"*15 + " " + date[0:-2] + " " + date_dict[date[-2::]] + " " +"-"*15

f = open(path, "w")

f.write('-'*len(header))
f.write("\n")
f.write(header)
f.close()

