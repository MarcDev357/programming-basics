def main():
    
    print("Enter the names of three friends. ")
    
    name1 = input("Enter name 1: ")
    name2 = input("Enter name 2: ")
    name3 = input("Enter name 3: ")
    
    myfile = open("friends.txt", "w")
    
    myfile.write(name1 + "\n")
    myfile.write(name2 + "\n")
    myfile.write(name3 + "\n")
    
    myfile.close()
    print("The names were written to friends.txt.")
    
if __name__ == "__main__":
    main()  # call main function