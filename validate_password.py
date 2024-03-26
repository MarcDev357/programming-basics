import login

def main():
    password = input("Enter a password: ")
    
    while not login.valid_password(password):
        print("That password is not valid.")
        password = input("Enter a password: ")
        
    print("That is a valid password.")
    
if __name__ == "__main__":
    main()