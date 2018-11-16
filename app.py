# Hello World
print("Hello World")

# Drawing Shape
print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")

# Variables and data types
character_name = "John"
character_age = 50
is_male = True
print("There once was a named " + character_name + ", ")
print("he was " + str(character_age) + " years old. ")

character_name = "Mike"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + str(character_age) + ".")

# Working with strings
print("Opennbox\nAcademy")
print("Opennbox\Academy")
phrase = "Opennbox Academy"
print(phrase + " is cool")
print(phrase.lower())
print(phrase.upper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("box"))
print(phrase.replace("Academy", "Datacenter"))

# Working with numbers
print(-2.4546)
print(3.45 + 4.54)
print(3.45 / 4.54)
print(3 * (4 + 5))
print(10 % 3)
my_num = 5
print(str(my_num) + " my favourite number")
print(abs(-5))
print(pow(4, 6))
print(max(4, 6))
print(min(4, 6))
print(round(45.6543))

from math import *
print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))
