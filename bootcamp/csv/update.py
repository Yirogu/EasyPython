# import csv
#
# def update_users(name, surname,new_name,new_surname) :
#     with open("users.csv", "r+") as f :
#         data = csv.DictReader(f)
#         for user in data :
#             if user["First Name"] == name and user["Last Name"] == surname :
#                 new_data = str(data)
#                 new_data = new_data.replace(name, new_name)
#                 new_data = new_data.replace(surname,new_surname)
#                 # break
#             # else :
#             #     return f"{name} {surname} not found."
#     with open("users.csv", "w") as f :
#         csv_write = csv.writer(new_data)
#         csv_write.truncate()
#         return csv_write
#
# update_users("Michal","Stachowski","Janusz","Wasacz")
# print(update_users("Michal","Stachowski","Janusz","Wasacz"))
import csv

def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)

    return "Users updated: {}.".format(count)
update_users("Michal","Stachowski","Janusz","Wasacz")
