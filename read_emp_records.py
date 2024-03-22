# This program displays the records that are in the employee.txt file.

def main():
    # Open the employee.txt file.
    with open("employee.txt", "r") as emp_file:
        # Read the first record's name field.
        name = emp_file.readline()
        
        # If a field was read, continue reading the rest of the record.
        while name != "":
            # Read the ID number and department fields.
            id_num = emp_file.readline()
            dept = emp_file.readline()
            
            # Strip the newlines from the fields.
            name = name.rstrip("\n")
            id_num = id_num.rstrip("\n")
            dept = dept.rstrip("\n")
            
            # Display the record.
            print("Name:", name)
            print("ID:", id_num)
            print("Dept:", dept)
            print()
            
            # Read the next name field.
            name = emp_file.readline()
            
# Call the main function.
if __name__ == "__main__":
    main()