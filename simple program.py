import os
import time
discontinue = "q"
GUI = f"""\033[32mMy current working directory\033[0m \"{os.getcwd()}\"
1. Make Folders
2. Remove Folders
3. View my directories
4. Quit('q')"""
while True:
    print(GUI)
    user_input = input("Please select your choice ('1', '2', '3', 'q'):\n")
    if user_input == "1":
        while True:


            user_input = input("What folders do you want to make:\n")
            if user_input.lower() == discontinue:
                break
            else:
                try:
                    os.mkdir(user_input)
                except FileExistsError:
                    print("File already exists")
        
    
    elif user_input == "2":
        while True:
            user_input = input("What folders do you want to remove:\n")
            
            if user_input.lower() == discontinue:
                break
            else:
                try:
                    os.rmdir(user_input)
                except FileNotFoundError:
                    print("The file does not exists")
    elif user_input == "3":
        while True:
            print(os.listdir())
            input("Press enter to continue.")
            break
    elif user_input.lower() == "q":
        break
    elif user_input == "":
        print("This program doesn't receive empty command.")
        time.sleep(1)
