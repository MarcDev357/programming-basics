import random

def main():
    
    myfile = open("numbers.txt", "w")
    
    for count in range (100):
        number = random.randint(1,100)
        myfile.write(str(number) + "\n")
        
    myfile.close()
    print("Done")
    
if __name__ == '__main__':
    main()