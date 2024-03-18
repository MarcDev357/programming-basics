def main():
    
    infile = open("philosophers", "r")
    
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    
    infile.close()
    
    
    print(line1)
    print(line2)    
    print(line3)    
    print(line4)
    
if __name__ == "__main__":
    main()