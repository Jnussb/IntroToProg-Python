# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# JNussb,05.10.2022,Added code for assignment 5
# JNussb,05.16.2022,Completed code
# JNussb,05.17.2022,Completed final run
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dictRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
try:      # if file exists
    strFile = open(objFile, "r")
    for row in strFile:
        task, priority = row.split(",") # Returns a list!
        dictRow = {"Task": task.strip(), "Priority": priority.strip()}
        lstTable.append(dictRow)
        print(dictRow["Task"] + ',' + dictRow["Priority"])
    strFile.close()
except:     # if file not found
    print("File not found. You can create a new file when you save.")

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
        # TODO: Add Code Here
        print("Task" + " | " + "Priority")
        for row in lstTable:
            print(row["Task"] + '|' + row["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        print("Type in another 'Task' and its 'Priority'")
        strTask = input("Enter a new task:")
        strPriority = input("Enter priority (High, Medium, or Low): ")
        dictRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dictRow)
        print("Your task was added to the list.")
        print("Task" + '|' + "Priority")
        for row in lstTable:
            print(row["Task"] + '|' + row["Priority"])
        continue
    # Step 5 - Remove an item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        strTaskRemove = input("Which task do you wish to remove? ")
        for row in lstTable:
            if row["Task"].lower() == strTaskRemove.lower():
                lstTable.remove(row)
                print("Task removed")
                print(lstTable)
            else:
                print("Task not found")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        strFile = open(objFile, "w")
        for row in lstTable:
            strFile.write(row["Task"] + ',' + row["Priority"] + '\n')
        strFile.close()
        print("Successfully saved!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print("You have exited the program. Adios!")
        break  # and Exit the program

    else:
        print("Input is not recognized. Please pick a number from 1 to 5.")