def main():
    
    with open("test_scores.csv", "r") as csv_file:
        lines = csv_file.readlines()
        
    for line in lines:
        
        tokens = line.split(",")
        
        total = 0.0
        for score in tokens:
            total += float(score)
            
        average = total / len(tokens)
        print("Average:", average)
        
if __name__ == "__main__":
    main()