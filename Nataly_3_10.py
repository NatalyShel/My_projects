""" program performs a vowel eater (redisinged to create a final word)
"""

# read a user word
word = input("Enter a word --> ")

# convert the word to uppercase
word = word.upper()

# init a final word
final_word = ""

# check the letters of the word in a loop
for i in word:
    if i in ['A','E','I','O','U']:  # if the letter is vowel
        continue                    # continue looping without printing
    else:
        final_word += i     # otherwise concatenate the letter to the final word

# print the final word
print(final_word)