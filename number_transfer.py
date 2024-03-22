# Assume the list number1 has 100 elements, 
# and number2 is empty. Write code that copies 
# the values in number1 to number2.

numbers1 = [i for i in range(100)]  # Assuming numbers1 has 100 elements
numbers2 = []

numbers2 = numbers1.copy()  # This will copy all the elements from numbers1 to numbers2 