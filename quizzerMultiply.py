# Import random
import random
# Created a main function 
def main():
    success = Quizzer()

# Generate random number for problem, ask user question and see if correct. 
def Quizzer():
    # Create 2 randint variables to use in problem
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    # Display random multiplication problem
    print(f"What is {x} x {y}?")
    #Calculate for the product
    product = x * y
<<<<<<< HEAD
    #Store user answer
    try:
        result = int(input("Answer is: "))
    except ValueError:
        print("Please enter numbers.")
=======
    # Store user answer
    result = int(input("Answer is: "))
>>>>>>> cb84b37bd0b4d20d945aa91cf76e48d2b7b287c0
    # if/else to see if results are true/false.
    if result == product:
        print("Good Job!")
        return True
    else:
        print("Better luck next time!")
        return False
# Call function to run    
main()
