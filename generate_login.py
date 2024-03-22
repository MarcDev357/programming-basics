import generate_login as login

def main():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    idnumber = input("Enter your ID number: ")
    
    print("Your system login name is: ", login.generate_login(first, last, idnumber))
if __name__ == "__main__":
    main()