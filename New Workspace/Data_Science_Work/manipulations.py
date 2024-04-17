# create variable storing user input  
str_manip = input("Please enter a sentence: ")

# display no. characters from user input using len() function 
print("your sentence has " + str(len(str_manip)) + " characters, including spaces")

# replace the last letter with an @ using the .replace() function and backwards index [-1], displaying the altered user input 
print(str_manip.replace(str_manip[-1], "@"))

# display last 3 characters of the user's input backwards 
print(str_manip[-1:-4:-1])

# create new string variable that is the addition of the first 3 characters and last 2 characters of user's input
new_str = str_manip[:3] + str_manip[-2:]
print(new_str)