given_number = int(input("Enter a number: \n")) # Triggers user input for an integer
stars = "*****" # creates pattern templatee  variable 
for i in range(0, 10): # initiates loop with 9 iterations 
        if i <= 5:
            print(stars[:i]) # creates increasing number of stars 
        elif i > 5:
            index = 5 - i
            print(stars[:index]) # creates decreasing number of stars