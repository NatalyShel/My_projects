""" program performs a vowel eater
"""
# read a user word
word = input("Enter a word --> ")

# convert the word to uppercase
word = word.upper()

# check the letters of the word in a loop
for i in word:
    if i in ['A','E','I','O','U']:  # if the letter is vowel
        continue                    # continue looping without printing
    else:
        print(i)                    # otherwise print the letter