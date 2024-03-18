def main():
    
    infile = open("philosophers", "r")
    
    file_contents = infile.read()
    
    infile.close()
    
    print(file_contents)
    
if __name__ == "__main__":
    main()