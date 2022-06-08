# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter a word...").upper()
vowels = "AEIOU"

for letter in user_word:  # iterate over each letter in a string
    if letter in vowels:
        continue
    print(letter)

#==================================================================

word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter a word...").upper()


for letter in user_word:
    if letter in vowels:
        continue
    word_without_vowels += letter

# Print the word assigned to word_without_vowels.
print(word_without_vowels)