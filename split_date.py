def main():
    
    date_string = "11/26/2023"
    
    date_list = date_string.split("/")
    
    print("Month:", date_list[0])
    
    print("Day:", date_list[1])

    print("Year:", date_list[2])
    
if __name__ == "__main__":
    main()