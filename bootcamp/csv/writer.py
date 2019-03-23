from csv import writer, DictWriter,reader
import os
def add_user(first,last,fpath):

    with open(fpath,"a") as f :
        headers = ["First Name","Last Name"]
        csv_writer = DictWriter(f,fieldnames = headers)
        if not (os.path.isfile(fpath) and os.path.getsize(fpath) > 0):
            csv_writer.writeheader()
            # do zrobienia :
            # jezeli w pelnym pliku nie ma headers to ma je wstawiac na poczatku
        csv_writer.writerow({
        "First Name" : first,
        "Last Name" : last})
add_user("Michal","Stachowski","users.csv")
