import login

def main():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    idnumber = input("Enter your ID number: ")
    
    print("Your system login name is: ", login.get_login_name(first, last, idnumber))
if __name__ == "__main__":
    main()