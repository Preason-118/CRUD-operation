## File handling basic project that include CRUD operation
from pathlib import Path
import os


def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items) :
        print(f"{i+1}  : {items}")

def checkfile():
    try:
        readfileandfolder()
        name = input("Please tell your file name:- ")
        p = Path(name)
        if not p.exists() :
            with open(p, 'w') as fs:
                data = input("What you want to write in this file:- ")
                fs.write(data)
            print(f"File created successfully")  
        else:
            print(f"This file already exists")      
    except Exception as error:
        print(f"An error occurred as {error}")


def readfile():
    try:
        readfileandfolder()
        name = input("Tell which file you want to read:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("File read successfully")    

        else:
            print("file doesnot exist")

    except Exception as error:
        print(f"Exception occurred as {error}")


def updatefile():
    try:
        readfileandfolder()
        name = input("Tell which file you want to update:-")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing   the name of your file")
            print("Press 2 for overriding the data of your file")
            print("Press 3 for appending some data in your file")

            res = int(input("Tell your response(1-3):- "))
            if res == 1:
                name2 = input("Tell your new file name :- ")
                p2 = Path(name2)
                p.rename(p2)

            if res == 2:
                with open(p, 'w') as fs:
                    data =  input("Tell what data you want to override:- ")
                    fs.write(data)

            if res == 3:
                with open(p,'a') as fs:
                    data = input("Tell what data you want to append:- ")  
                    fs.write(" "+data)      

    except Exception as error:
        print("Exception occurred as {error}")
    print("File updated successfully")

def deletefile():
    try:
        readfileandfolder()
        name = input("Which file you want to delete:- ")
        p = Path(name)
        if p.exists() and p.is_file:
            os.remove(name)
            print("File removed successfully")
        else:
            print("NO such file exists")
    except Exception as error:
        print(f"An error occurred as {error}")




print("Press 1 for creating the file")
print("Press 2 for reading  the file")
print("Press 3 for updating the file")
print("Press 4 for deleting the file")


check = int(input("Please tell your response:- "))

if check == 1 :
    checkfile()


if check == 2:
    readfile()

if check == 3:
    updatefile()    

if check == 4:
    deletefile()


























