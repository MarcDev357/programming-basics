def main():
    myfile = open("friends.txt", "a")
    
    myfile.write("Tia\n")
    myfile.write("William\n")
    myfile.write("Travon\n")
    myfile.write("Wini\n")
    
    myfile.close()
    
if __name__ == "__main__":
    main()