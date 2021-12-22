# Split string method
names_string = input("Give everybody's names separated by a comma and space")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
random_choice = random.randint(0, len(names)-1)
whos_paying = names[random_choice]
print(whos_paying)
