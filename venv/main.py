'''
This is a simple App that does basic CRUD operations on Data stored in a file
This is the main python script that invokes functions in other files
Coded By: Arunava Bhattacharya
'''
import createEmployee
allowedoptions = (1,2,3,4)
while True:
    # Getting the options
    print("WELCOME TO EMPLOYEE DATABASE APP\nPlease Select an Option Below")
    print("1. Create a New Employee\n2. Search for an Employee\n3. Update an Employee\n4. Delete Employee Data")
    # Handling exception due to invalid Data type Input
    try:
        option = int(input("\nEnter an Option:"))
    except:
        print("Invalid Number.")
    # Handling exception due to invalid Option Input
    if option == 1:
        # Trigger the Employee Data Creation Function
        # Input the Data for the Fields Employee Name, Age, Grade and Department
        name = input("Enter Employee Name:")
        try:
            age = int(input("Enter Employee Age:"))
        except:
            print("Invalid Age")
            break
        grade = input("Enter Employee Grade:")
        dept = input("Enter Employee Deperatment:")
        createEmployee.CreateEmployee(name,age,grade,dept)
    elif option == 2:
        # Invoking the Search function. Only Search by Name is possible
        name = input("Enter the Name of Employee to Search:")

    elif option == 3:
        print("Inside Option 3")
    elif option == 4:
        print("Inside Option 4")
    else:
        print("Sorry Invalid Option choose again")