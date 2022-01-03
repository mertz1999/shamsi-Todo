import argparse
from database import database

# --- Handle argparse
parser = argparse.ArgumentParser(description='------ Todo list ------')

group = parser.add_mutually_exclusive_group()
group.add_argument("-w","--write", action="store_true", help='Write Todo list of input date to .txt file')
group.add_argument("-i","--insert", action="store_true", help='Insert a Todo item')
group.add_argument("-t","--today", action="store_true", help='Write Todo list of  Today list')

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

elif args.insert:


# elif argparse.today:

