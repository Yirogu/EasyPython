import csv

def find_user(name, surname) :
    i = 0
    a = 0
    with open("users.csv") as f :
        data = csv.DictReader(f)
        for user in data :
            a+=1
            if user["First Name"] == name and user["Last Name"] == surname :
                return a
        return f"{name} {surname} not found."
