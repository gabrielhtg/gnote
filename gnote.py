import sys
import os
import pyperclip

# buat dulu fungsi fungsi yang memungkinkan
# ! Nama program ini adalah Gnotes --> jadi nanti dipanggil dengan command gnotes
# sub argumen yang dibuat adalah
# todo - list
# todo - add
# todo - remove
home = os.path.expanduser('~')

def list() :
    if len(os.listdir(home + "/gnote/list/")) != 0 : 
        for i in range(len(os.listdir(home + "/gnote/list/"))) :
            print("    -", os.listdir(home + "/gnote/list/")[i])
    else:
        print("Your note is empty.")
        
def add() :
    try : 
        nama_file = sys.argv[2]
        os.system("nano ~/gnote/list/" + nama_file)
    except IndexError :
        print("Make sure your command is correct.")
        
def remove() :
    try :
        nama_file = sys.argv[2]
        os.system("rm ~/gnote/list/" + nama_file)
        
    except IndexError :
        print("Make sure your command is correct.")
        
def view() :
    
    try :
        nama_file = sys.argv[2]
        os.system("cat ~/gnote/list/" + nama_file)
    except IndexError:
        print("Make sure your command is correct.")

    
def copy() :
    try :
        nama_file = sys.argv[2]
        with open(home + "/gnote/list/" + nama_file, "r") as file :
            salin = file.read()
        pyperclip.copy(salin)
        print("Copied") 
        
    # except UnboundLocalError :
    #     print("Make sure your command is correct.")
        
    except IndexError :
        print("Make sure your command is correct.")
        
    except FileNotFoundError :
        print("Note " + nama_file + " not found")
    
def help() :
    print("USAGE")
    print("    note add [note_name]")
    print("    note view [note_name]")
    print("    note remove [note_name]")
    print("    note list") 
    print("    note copy [note_name]")
    print("    note version")
    print("OPTIONS")
    print("    add          Add new note or edit a note")
    print("    view         See the contents of the note")
    print("    remove       Removing note")
    print("    list         Show all notes")
    print("    help         Prints help information")
    print("    copy         Copy a note content")
    print("    version      Show gnote version")
        
if (len(sys.argv) >= 2)  :
    perintah = sys.argv[1]
    
    if sys.argv[1] == 'list' :
        list()
                
    elif sys.argv[1] == 'add' :
        add()
    
    elif sys.argv[1] == 'remove' :
        remove()
        if len(os.listdir(home + "/gnote/list/")) != 0 :
            print("List your notes now")
            list()
        else :
            print("Your note is now empty.")
        
    elif sys.argv[1] == 'view' :
        view()
        
    elif sys.argv[1] == 'copy' :
        copy()
        
    elif sys.argv[1] == 'version' :
        print("GNOTE v.1.2")
        
    else :
        help()
        
else :
    help()
    
