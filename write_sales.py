def main():
    # Prompt for number of sales days
    num_days = int(input("For how many days do you have sales? "))
    
    # Open the file in write mode
    with open("sales.txt", "w") as sales_file:
        # Loop for input per days of sales
        for count in range(1, num_days + 1):
            sales = float(input(f"Enter the sales for day #{count}: "))
            sales_file.write(f"{sales}\n")
    # Close file and identfy when input is done. 
    sales_file.close()
    print("Data written to sales.txt")
    

if __name__ == "__main__":
    main()
