# This program copies the sequence.txt file.
def main():
    with open("sequence.txt", "r") as infile, open("sequence_copy.txt", "w") as outfile:
        line = infile.readline()
        while line != "":
            outfile.write(line)
            line = infile.readline()
    print("File has been copied.")
    
# Call the main function.
if __name__ == "__main__":
    main()