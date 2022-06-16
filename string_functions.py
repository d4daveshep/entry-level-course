# Demonstrating the ord() function.

char_1 = 'a'
char_2 = ' '  # space

# print the code point number from the char
print(ord(char_1))
print(ord(char_2))

print()
# Demonstrating the chr() function.
# print the char from the code piont number
print(chr(97))
print(chr(945))

x = 'a'
print(chr(ord(x)) == x)

y = 97
print(ord(chr(y)) == y)

# Example 1: Demonstrating the islower() method:
print()
print("Moooo".islower()) # false
print('moooo'.islower()) # true

# Example 2: Demonstrating the isspace() method:
print(' \n '.isspace()) # true
print(" ".isspace()) # true
print("mooo mooo mooo".isspace()) # false

# Example 3: Demonstrating the isupper() method:
print("Moooo".isupper()) # false
print('moooo'.isupper()) # false
print('MOOOO'.isupper()) # true
print()

# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))  # join these 3 strings together with the string the method is called on

# Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]")

print("www.cisco.com".lstrip("w."))  # strip all the characters in the argument string form the string

print("pythoninstitute.org".lstrip(".org"))  # does nothing since .org is not leading

# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

# rfind searches the substring from the right for the string specified
txt = "Hello, welcome to my world."
x = txt.rfind("e", 9, 15)  # search between chars 9 to 14 "lcome to" for "e" gives index 13 in original string
print(x)

# Demonstrating the split() method:  split the string on whitespace returning a list of substrings
print("phi       chi\npsi".split())

