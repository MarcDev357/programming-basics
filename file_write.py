def main():
    
    outfile = open("philosophers", "w")
    
    outfile.write("John Locke\n")
    outfile.write("David Hume\n")
    outfile.write("Edmund Burke\n")
    outfile.write("Marcus Wiggs\n")
    
    outfile.close()
    
if __name__ == "__main__":
    main()