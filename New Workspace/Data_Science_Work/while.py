# Create control variable and user input variable

number_total = 0 
nums = []
 # Makes the while loop run infinitely
while True:  
# Triggers a user input of an integer
    user_num = int(input("Please enter a number: "))  # 
    if user_num == -1:  
        break  # If the user enters -1 it breaks out of the while loop
    else:
        nums.append(user_num)   # If the number is not -1 add it to the list of numbers
        number_total += user_num  # Adds to the total value to use later for calculating average


if number_total > 0:
    average = number_total / len(nums)   # len(nums) finds the length of the list excluding
    print("The average of the numbers entered is:", average)
else:
    print("No valid numbers entered. Exiting program.")