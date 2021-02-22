import sys
import os 
import shutil
sys.path 
'''
Import:
* sys
* os
* shutil

Create Python Naming Convention:
If the -m and -d are not in sys.argv
Create Three Privilege Levels:
* Basic
* Elevated
* Admin 

Create a if statement for basic:
* Find Current Working Directory
* Print Current Directory
* Confirm you want to change the directory 
* Enter new directory 
* Run makedir function 
* Print(listdir)
* Print Items inside the directory

Create a if statement for elevated:
* Find Current Working Directory
* Print Current Directory
* Confirm you want to change the directory 
* Enter new directory 
* Run makedir function 
* Print(listdir)
* Print Items inside the directory
* Ask if they would like to copy a file or directory 
* Enter name of file 
* Copy to new file = 'Users/terrancemccoy/Python_Log/system_log.txt'
* Create exceptions for creating a new directory 

Create a if statement for admin:
* Find Current Working Directory
* Print Current Directory
* Confirm you want to change the directory 
* Enter new directory 
* Run makedir function 
* Print(listdir)
* Print Items inside the directory
* Ask if they would like to copy a file or directory 
* Enter name of file 
* Copy to new file = 'Users/terrancemccoy/Python_Log/system_log.txt'
* Create exceptions for creating a new directory 

Issues:
1. Each Conditional Statement runs consecutively
2. Assign all commands to Users/terrancemccoy/Python_Log/system_log.txt
3. -d command 

'''
if __name__ == "__main__":
    privilege_level = sys.argv[sys.argv.index("-m") + 1]
    if "-m" not in sys.argv:
        privilege_level = sys.argv[sys.argv.index("-m") + 1]
    if ".." in privilege_level:
        print("Cannot move up the filesystem using ..")
        exit()

    else:
        if privilege_level != "basic" and privilege_level != "elevated" and privilege_level != "admin":
            print("Invalid privilege level. Please specify basic, elevated, or admin")
    
   
    if "-m" in sys.argv and privilege_level == "basic":
        cwd = os.getcwd()
        print("Current Working Directory %s" % cwd)
        change_dic = input("Would you like to change the directory?")
        if change_dic == "yes":
            try:
                direct = input("Enter Directory:")
                mode1 = 456
                os.makedirs(direct, mode1)
                print(os.listdir())
                print(os.system("ls -l"))
                x = os.stat(direct)
                print(x)
            except FileExistsError:
                print("Please enter a different file")
            if not os.path.exists('/Users/terrancemccoy/Python_Log/system_log.txt'):
                os.makedirs('/Users/terrancemccoy/Python_Log/system_log.txt')

    if "-m" in sys.argv and privilege_level == "elevated":
        cwd = os.getcwd()
        print("Current Working Directory %s" % cwd)
        change_dic = input("Would you like to change the directory?")
        if change_dic == "yes":
            try:
                direct = input("Enter Directory:")
                mode1 = 456
                os.makedirs(direct, mode1)
                print(os.listdir())
                print(os.system("ls -l"))
                x = os.stat(direct)
                print(x)
            except FileExistsError:
                print("Please enter a different file")
    
        copy = input("Would you like to copy a file or directory? yes or no:")
        if copy == "yes":
            try:
                file1 = input("Enter File's name:")
                new_file = '/Users/terrancemccoy/Python_Log/system_log.txt'
                shutil.copy2(file1, new_file)
                if not os.path.exists('/Users/terrancemccoy/Python_Log/system_log.txt'):
                    os.makedirs('/Users/terrancemccoy/Python_Log/system_log.txt')

            except shutil.SameFileError:
                print("Source and destination represents the same file.")
            except IsADirectoryError:
                print("Destination is a directory.")
            except PermissionError:
                print("Permission denied")
                
            for directoryName, subDir, fileNames in os.walk("/Users/terrancemccoy/Python_Log/system_log.txt"):
                print("The current directory is" + directoryName)  

    if "-m" in sys.argv and privilege_level == "admin":
        cwd = os.getcwd()
        print("Current Working Directory %s" % cwd)
        change_dic = input("Would you like to change the directory?")
        if change_dic == "yes":
            try:
                direct = input("Enter Directory:")
                mode1 = 456
                os.makedirs(direct, mode1)
                print(os.listdir())
                print(os.system("ls -l"))
                x = os.stat(direct)
                print(x)
            except FileExistsError:
                print("Please enter a different file")
    copy = input("Would you like to copy a file or directory? yes or no:")
    if copy == "yes":
        try:
            file1 = input("Enter File's name:")
            new_file = '/Users/terrancemccoy/Python_Log/system_log.txt'
            backup = './backups'
            shutil.copy2(file1, "./backup/" + file1 + "_saved")
            os.remove(file1)
            if not os.path.exists('/Users/terrancemccoy/Python_Log/system_log.txt'):
                os.makedirs('/Users/terrancemccoy/Python_Log/system_log.txt')
        except shutil.SameFileError:
            print("Source and destination represents the same file.")
        except IsADirectoryError:
            print("Destination is a directory.")
        except PermissionError:
            print("Permission denied")
        for directoryName, subDir, fileNames in os.walk("/Users/terrancemccoy/Python_Log/system_log.txt"):
            print("The current directory is" + directoryName)  





    



