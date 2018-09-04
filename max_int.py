# Design an algorithm that finds the maximum positive integer input by a user.  The user repeatedly inputs numbers until a negative value is entered.
# 1. Ask user to Input a number
# 2. Check if the number is negative
# 2.1 If number is negative then print the number
# 2.2 If the number is positive, assign it to max_int
# 3. Keep asking user to input a number
# 3.1 If the number is higher than max_int then it should be assigned to max_int
# 3.2 If the number is negative - Print max_int
num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = num_int

while num_int > 0:
    num_int = int(input("Input a number: "))    # Do not change this line
    max_int = num_int if num_int > max_int else max_int
else:    
    print("The maximum is", max_int)    # Do not change this line
