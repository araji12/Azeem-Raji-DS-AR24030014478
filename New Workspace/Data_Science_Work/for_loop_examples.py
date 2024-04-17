# Looping through a list (Example 1)
pokemon_list = [ 'Pikachu', 'Charizard', 'Infernape']
for i in pokemon_list: 
      print("Current Pokemon: ", i)

# 'i' would represent each of these values within each iteraton within the loop 
# For Loops allow for manipulation of each individual item
    

# # Looping through a string (Example 2)
random_sent = "Hello there General Kenobi!"

for letter in random_sent: 
        print(letter)

# Prints each indivual letter in each line 



# Isolating words using the split function (Example 3)
random_sent2 = "Gotta catch them all"
random_sent2_split = random_sent2.split(" ")

for letter in random_sent2_split: # stores each word as an singulat item in a list 
      print(letter)




# Looping using range () (Example 4)
# range (1, 6) = [1, 2, 3, 4, 5] i.e range is equal to a list       
for number in range(1, 6):
       print(number)

# Prints 1, 2, 3, 4, 5
# Last number (i.e. 6 in example) is not included in the list
       


# Using the step function in For Loops (Example 5)
for number in range(0, 10, 2): 
       print(number)   

# Prints 0, 2, 4, 6, 8 
# this the step acts as an increment starting from 0 and ending at 8
# essentially returns all the even numbers within the list
       

# Nested Loops (Grids) (Example 6)
for i in range(1, 4): # represents the rows
    print("i: ", i) # prints out i at a particular point 
    for j in range(1, 4): # represnts the columns 
        print("j: ", j) # prints out j at a particular point 
        print(i * j, end=" ") # end=" ", embeds a space between the outputs
        print("i * j:", i * j)
    print( )

