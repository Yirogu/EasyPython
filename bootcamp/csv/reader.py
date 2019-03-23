# print_users() # None
# prints to the console:
# Colt Steele
# '''
from csv import reader


def print_users():
    with open("users.csv") as f :
        users = list(reader(f))
        for user in users :
            print(f"{user[0]} {user[1]}")
print_users()
