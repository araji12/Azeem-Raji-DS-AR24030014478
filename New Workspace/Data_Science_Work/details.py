# create variables which will store user's name, age, house no. and streer name 
name = input("Please enter your name: ")
age = int(input("Please provide your age: "))
house_num = input("What is your house number?: ")
street_name = input("Which street do you live on?: ")

# display stored all data in a single sentence 
print("This is " + name + ", who is " +  str(age) + " years old." + " They live at house number " + house_num + " on " + street_name)
   