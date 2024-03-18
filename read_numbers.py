def main():
    
    infile = open('number.txt', 'r')
    
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())
    
    infile.close()
    
    total = num1 + num2 + num3
    
    print(f'The numbers are:, {num1}, {num2}, {num3}')
    print(f'Their total is:, {total}')
    
if __name__ == '__main__':
    main()