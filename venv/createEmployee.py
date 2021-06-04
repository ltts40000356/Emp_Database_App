import pandas as pd
import csv as csv
from csv import writer
def CreateEmployee(name,age,grade,dept):
    # Input the Data for the Fields Employee Name, Age, Grade and Department
    # Checking the csv file if the file already has a data
    database = pd.read_csv("database.csv")
    # Assigning the first ID in case of an Empty file or incrementing the last ID by 1 if it is not Empty
    if database.shape[0] == 0:
        id  = 100001
    else:
        last_row = database.iloc[-1]
        id = int(last_row[0]) + 1
    # Creating tuple made of the different fields.
    data = [id, name, age, grade, dept]
    # Opening the csv file to write the Data into the csv
    with open('database.csv', 'a', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(data)
    print("Employee has been added successfully")