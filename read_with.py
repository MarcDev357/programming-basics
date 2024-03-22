# This program reads the contenets of sequence.txt and displays them.
def main():
    with open("sequence.txt", "r") as infile:
        line = infile.readline()
        while line != "":
            print(line.rstrip("\n"))
            line = infile.readline()
            
# Call the main function.
if __name__ == "__main__":
    main()