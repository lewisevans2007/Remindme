import os
import sys
import shutil
from sys import exit
VERSION = "0.1.3"

def newreminder(name,due,notes):
    os.chdir("reminders")
    name_hex = str(name.encode().hex().upper())
    try:
        os.mkdir(name_hex)
        os.chdir(name_hex)
        name_file = open("name.data","w")
        name_file.write(name)
        name_file.close()
        del name
        due_file = open("due.data","w")
        due_file.write(due)
        due_file.close()
        del due
        notes_file = open("notes.data","w")
        notes_file.write(notes)
        notes_file.close()
        del notes
        os.chdir("..")
        os.chdir("..")
        print("Created reminder!")
    except FileExistsError:
        print("Reminder already exists")

def deletereminder(name):
    name_hex = str(name.encode().hex().upper())
    os.chdir("reminders")
    try:
        shutil.rmtree(name_hex)
    except FileNotFoundError:
        print("Reminder dose not exist!")
        exit()
    os.chdir("..")
    print("Deleted reminder!")
def getreminders():
    reminders = os.listdir("reminders")
    reminders.remove("gitkeep")
    return reminders
def getdue(name):
    os.chdir("reminders")
    os.chdir(name)
    date_due_file = open("due.data","r")
    date_due = date_due_file.read()
    date_due_file.close()
    del date_due_file
    os.chdir("..")
    os.chdir("..")
    return date_due
def getnotes(name):
    os.chdir("reminders")
    os.chdir(name)
    notes_file = open("notes.data","r")
    notes = notes_file.read()
    notes_file.close()
    del notes_file
    os.chdir("..")
    os.chdir("..")
    return notes
if __name__ == "__main__":
    print("RemindMe v"+VERSION,"by Awesomelewis2007")
    print("")

    for i in sys.argv: #goes though the arguments
        if i.upper() == "-NEW":
            #Reminder creation wizard
            print("Creating a new reminder")
            reminder_name = input("Name of reminder>")
            reminder_due = input("Date due>")
            writing_notes = True
            reminder_notes = ""
            while writing_notes == True:
                note_input = input("Notes>")
                if note_input == "":
                    break
                reminder_notes = reminder_notes +"\n"+ note_input
            if reminder_due == "":
                reminder_due = "--" 
            newreminder(reminder_name,reminder_due,reminder_notes)
            exit()
        if i.upper() == "-DEL":
            #Reminder deletion wizard
            print("Deleting a reminder")
            print("WARNING: This will PERMANENTLY delete your reminder and all of its data!")
            print("Use crtl+C to cancel")
            try:
                reminder_name = input("Name of reminder>")
            except KeyboardInterrupt:
                print("Exiting, no changes were made")
                exit()
            deletereminder(reminder_name)
            exit()
    if getreminders() == []: #Message if there is no reminders
        print("You have no reminders you can make one by adding the '-new' argument")
        exit()

    if len(getreminders()) >= 30:
        print("you have over 30 reminders do you want to display them all? Y or N")
        consent = input(">")
        if consent.upper() == "Y" or "YES":
            pass
            del consent
        else:
            exit()

    print("Reminders:")
    for i in getreminders():
        i_object = bytes.fromhex(i)
        decoded_string = i_object.decode("UTF-8")
        print("==========["+decoded_string+"]==========")
        print("Due:"+getdue(i))
        print("===[Notes]==="+getnotes(i))
