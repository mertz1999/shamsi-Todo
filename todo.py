import argparse
from database import database
from makefile import makefile
from utils import *

# --- Handle argparse
parser = argparse.ArgumentParser(description='------ Todo list ------')

group = parser.add_mutually_exclusive_group()
group.add_argument("-w","--write", action="store_true", help='Write Todo list of input date to .txt file')
group.add_argument("-i","--insert", action="store_true", help='Insert a Todo item')
group.add_argument("-t","--today", action="store_true", help='Write Todo list of Today list')

parser.add_argument('-d','--date', type=str, help="Date of Todo item that you want to set or you want to see")

args = parser.parse_args()

# --- instance of database class
databace_obj = database()
print("------ Dataset is working ------")

# --- select method based on -w or -i or -t
if args.insert:
    i=0
    while(1):
        text_list = input("insert your ("+ str(i+1) +") Text(For set insert 'end') : ")
        if text_list != 'end':
            databace_obj.insert(args.date, text_list)
        else:
            break
    print("Your data has been set to database.")

elif args.today:
    # Get today date
    [date, short_date] = today()
    print("Today : ", date)

    # Read data from database
    data_values = databace_obj.read(short_date)
    print("Your Todo list (Also saved in ./todo/{}) : ".format(short_date+'.txt'))
    print(data_values)

    # call Makefile class
    makefile_obj = makefile(short_date, list(data_values['text']), list(data_values['id']))

elif args.write:
    # Read data from database
    data_values = databace_obj.read(args.date)
    print("Your Todo list (Also saved in ./todo/{}) : ".format(args.date+'.txt'))
    print(data_values)

    # call Makefile class
    makefile_obj = makefile(args.date, list(data_values['text']), list(data_values['id']))


