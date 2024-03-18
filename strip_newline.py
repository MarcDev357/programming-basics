def main():
    infile = open("philosophers", "r")
    
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    
    line1 = line1.rstrip("\n")
    line2 = line2.rstrip("\n")
    line3 = line3.rstrip("\n")
    line4 = line4.rstrip("\n")
    
    infile.close()
    
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    
if __name__ == "__main__":
    main()  # call main function