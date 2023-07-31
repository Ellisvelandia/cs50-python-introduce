#Ask user for their name
name = input("whats your name? ").strip().title()

#remove whitespace from str
# name = name.strip().title()

#Capitalize user's name 

# name = name.capitalize()
# name = name.title()

#split users name into first name and last name
  
first , last = name.split(" ")

print("welcome " + first + " your awesome and very smart")

age = input("what is your age? ")
print(int(age) , str("your age is great"))