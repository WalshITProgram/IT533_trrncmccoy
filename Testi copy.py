import sys
import os 
import shutil
sys.path 
if __name__ == "__main__":
    if "-m" not in sys.argv or "-d" not in sys.argv:
        privilege_level = sys.argv[sys.argv.index("-m") + 1]
        starting_directory = sys.argv[sys.argv.index("-d") + 0]    

    else:
        if privilege_level != "basic" and privilege_level != "elevated" and privilege_level != "admin":
            print("Invalid privilege level. Please specify basic, elevated, or admin")


    if ".." in starting_directory:
        print("Cannot move up the filesystem using ..")
        exit()
    if "-d" in starting_directory:
        try:
            os.chdir(starting_directory)
        except:
            print("Please specify a directory to move to.")
    else:
        starting_directory = os.getcwd()


    if "-m" in sys.argv and privilege_level == "basic":
        cwd = os.getcwd()
        print("Current Working Directory %s" % cwd)
        change_dic = input("Would you like to change the directory?")
        if change_dic == "yes":
            direct = input("Enter Diectory:")
            mode1 = 456
            os.makedirs(direct, mode1)
            print(os.listdir())
            print(os.system("ls -l"))
            if not os.path.exists('Users/terrancemccoy/Python_Log/system_log.txt'):
                os.makedirs('Users/terrancemccoy/Python_Log/system_log.txt')

    if "-m" in sys.argv and privilege_level == "elevated":
       cwd = os.getcwd()
       print("Current Working Directory %s" % cwd)
       change_dic = input("Would you like to change the directory?")
       if change_dic == "yes":
            direct = input("Enter Directory:")
            mode1 = 456
            os.makedirs(direct, mode1)
            print(os.listdir())
            print(os.system("ls -l"))
            x = os.stat(direct)
            print(x)
       chanf = input("Would you like to copy a file or directory? yes or no:")
       if chanf == "yes":
           file1 = input("Enter File's name:")
           new_file = input("Enter path you would like to store the copied file:")
           shutil.copy2(file1, new_file)

    if "-m" in sys.argv and privilege_level == "admin":
        cwd = os.getcwd()
        print("Current Working Directory %s" % cwd)
        change_dic = input("Would you like to change the directory?")
        if change_dic == "yes":
            direct = input("Enter Directory:")
            mode1 = 456
            os.makedirs(direct, mode1)
            print(os.listdir())
            print(os.system("ls -l"))
            x = os.stat(direct)
            print(x)
            chanf = input("Would you like to copy a file or directory? yes or no:")
            if chanf == "yes":
                file1 = input("Enter File's name:")
                new_file = input("Enter path you would like to store the copied file:")
                shutil.copytree(file1, new_file)
                shutil.move(file1)
                shutil.rmtree(file1)



        