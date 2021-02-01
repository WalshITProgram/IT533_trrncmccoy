import os 
import sys 
import shutil 
# argc = number of arguments 
# argv = elements of list 

if "-m" not in sys.argv:
    privilege_level = sys.argv[sys.argv.index("-m") + 1]
else:
    privilege_level = sys.argv[sys.argv.index("-m") + 1]
    if privilege_level != "basic" and privilege_level != "elevated" and privilege_level != "admin":
        print("Invalid privilege level. Please specify basic, elevated, or admin")
        sys.exit()

if "-d" in sys.argv: 
    starting_directory = sys.argv[sys.argv.index("-d") + 1]
    if ".." in starting_directory:
        print("Cannot move up the filesystem using ..")
        exit()
    try:
        os.chdir(starting_directory)
    except:
        print("Please specify a directory to move to.")
else:
    starting_directory = os.getcwd()

if privilege_level == "basic":

except:
    ("Please enter mode")


'''
determine if -m is given
if given, determine privilege level

if -d is given
determine the starting directory
attempt to chdir into that directory
else, use getcwd

if basic mode
user can choose to change directory or exit the program
add a custom change directory function here

if evelvated mode
user can choose to cd, cp, or exit
make custom cd and cp functions

if admin mode
user can choose to cd, cp, mv, rm, or exit

mv = move_directory()

Exmaple cp:
print out the current directory for the user
ask for the source file and the destination file
try to copy the source file to the destination
ask if the user wants to exit, otherwise ask for more files to copy (infinite loop) 

Example rm:
print out the current directory
ask for the file to delete
make a backup of the file (shutil.move)
rename the deleted file?
make a log entry (just make up this part)
determine if the user wants to delete something else
'''

        if ".." in starting_directory:
            print("Cannot move up the filesystem using ..")
            sys.exit()
        try:
            os.chdir(starting_directory)
        except:
            print("Please specify a directory to move to.")
    else:
        starting_directory = os.getcwd()

 if "-m" not in sys.argv:
        privilege_level = sys.argv[sys.argv.index("-m") + 1]

    elif "-d" not in sys.argv:
        starting_directory = sys.argv[sys.argv.index("-d") + 1]
    else:
        privilege_level = sys.argv[sys.argv.index("-m") + 1]
        starting_directory = sys.argv[sys.argv.index("-d") + 1]
        if privilege_level != "basic" and privilege_level != "elevated" and privilege_level != "admin":
            print("Invalid privilege level. Please specify basic, elevated, or admin")
        if starting_directory != "basic" and starting_directory != "elevated" and starting_directory != "admin": 
            print("Invalid starter directory level. Please specify basic, elevated, or admin")
            sys.exit()

