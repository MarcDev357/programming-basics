# This program gets employee data from the user and saves it as a record in the employee.txt file.

def main():
    # Get the number of employee records to create.
    num_emps = int(input("How many employee records do you want to create? "))
    
    # Open a file for writing.
    with open("employee.txt", "w") as emp_file:
        # Get each employee's data and write it to the file.
        for count in range(1, num_emps + 1):
            print("Enter data for employee #", count, sep="")
            name = input("Name: ")
            id_num = input("ID number: ")
            dept = input("Department: ")
            
            # Write the data as a record to the file.
            emp_file.write(name + "\n")
            emp_file.write(id_num + "\n")
            emp_file.write(dept + "\n")
            
            # Display a blank line.
            print()
            
    # Let the user know the records were written to the file.
    print("The records were written to employee.txt.")
    
# Call the main function.
if __name__ == "__main__":
    main()