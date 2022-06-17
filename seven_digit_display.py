# Set up the dictionary of digits.  each is a list of 5 strings
one = ["  #"] * 5
two = ["###", "  #", "###", "#  ", "###"]
three = ["###", "  #", "###", "  #", "###"]
four = ["# #"] * 2 + ["###"] + ["  #"] * 2
five = ["###", "#  ", "###", "  #", "###"]
six = ["###", "#  ", "###", "# #", "###"]
seven = ["###"] + ["  #"] * 4
eight = ["###","# #","###","# #","###"]
nine = ["###","# #","###","  #","###"]
zero = ["###"] + ["# #"] * 3 + ["###"]
number_dict = {"1": one, "2": two, "3": three, "4": four, "5": five, "6": six, "7":seven, "8":eight, "9":nine, "0":zero}

num_string = input("Enter number to display...")

# build a list of digit strings to print
numbers_to_print = []
for ch in num_string:
    if not ch.isdigit(): # ignore any non-digits
        continue
    numbers_to_print.append(number_dict[ch])

for row in range(5):
    for number in numbers_to_print:
        print(number[row], end=" ")
    print()