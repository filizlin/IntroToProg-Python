# ------------------------------------------------------------------------ #
# Title: Assignment 05_ToDoList
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <YLin>,<11.17.2020>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:
    objFile=open("ToDoList.txt", "r")
    for row in lstTable:
        strData = row.split(",")
        dicRow = {"Task":strData[0].strip,"Priority":strData[1].strip()}
        lstTable.append(dicRow)

except:
    print("There is no data in this file yet.  Please proceed with the menu to input data.")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        if len(lstTable) == 0:
            print("Currently, there is no Data in the ToDoList.txt File")
        else:
            for row in lstTable:
                print (row["Task"] + '\t' + row["Priority"])

        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Type in a Task: ")
        strPriority = input("Indicate its Priority (High/Medium/Low): ")
        print("Adding", strTask, strPriority, "to Table", sep=" ")
        dicRow = {"Task": strTask.strip(), "Priority" : strPriority.strip()}
        lstTable.append(dicRow)

        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strDelete = input("Which task would you like to delete from the To-Do list? ")
        for row in lstTable:
            if  strDelete.strip().lower() in row["Task"].strip().lower():
                strConfirmDelete = input("Are you sure you would like to delete the task " + strDelete + " from the file?  [Y/N] ")
                if strConfirmDelete.lower() == 'y':
                    lstTable.remove(row)
                    print("The task" + strDelete + "has been removed from the file.")
                else:
                    print("The task" + strDelete + "was not removed from the file.")
            else:
                print("The task entered does not exist in this row.")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        strResponse = input("Would you like to save your Data? [Y/N] ")
        if strResponse.lower().strip() == 'y':
            objFile = open("ToDoList.txt", "w")
            for row in lstTable:
                objFile.write(row["Task"] + "," + row["Priority"] + "\n")
            objFile.close()
        else:
            print("The data entered was not saved.")
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        strConfirmExit = input("Are you sure you want to exit the program? [Y/N] ")
        if strConfirmExit.lower().strip() == 'y':
            break
        else:
            continue
            # and Exit the program
