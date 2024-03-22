# This program writes the number 0-9 to sequence.txt
def main():
    with open('sequence.txt', 'w') as seq_file:
        for number in range(10):
            seq_file.write(f"{number}\n")
    print("Data has been written to sequence.txt.")
    
# Call the main function.
if __name__ == "__main__":
    main()