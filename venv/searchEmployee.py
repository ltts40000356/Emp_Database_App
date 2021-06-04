import csv
def searchEmployee(name):
    flag = False
    # Read csv file that is seperated by a comma seperator
    csv_file = csv.reader(open('database.csv', "r"), delimiter=",")
    # loop through the csv list
    for row in csv_file:
        # If the name exists. Comparing in same cases so that Search works on any case combination
        if (name.upper() == row[1].upper()):
            print(row)
            flag = True
    # If instead the search is Empty
    if flag == False:
        print("Searched Name Does NOT Exist")