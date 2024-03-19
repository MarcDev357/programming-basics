def main():
    # Open the sales.txt file for reading.
    sales_file = open('sales.txt', 'r')

    # Read the first line from the file.
    for line in sales_file:
        # Convert line to a float
        amount = float(line)
        # Format and display the amount.
        print(f"${amount:.2f}")
        
    # Close the file.
    sales_file.close()
    
# Call the main function.
if __name__ == "__main__":
    main()