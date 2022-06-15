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