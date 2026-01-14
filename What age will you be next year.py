import time
def greet():
    time.sleep(1)
    print("Wow.")
    print("Thinking...")
    time.sleep(2)
    print(f"Hello {name}, you are going to be {age+1} years old next year!")
if __name__ == "__main__":
    name = input("What is your name?:\n")
    while True:
        while True:
            try:
                age = int(input("What is your age?:\n"))
                break
            except ValueError:
                print("Please type only numbers.")
    
    
    
        greet()
        answer = input("Do you wish to continue using this program? Y/N:\n")
        if answer == "N".lower():
            print("Goodbye!")
            break
        