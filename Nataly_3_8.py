""" program that uses the break statement to
    exit/terminate a loop (in case of secret word "chupacabra")
"""
# continue asking in a loop until entered word is equal to "chupacabra"
while True:
    # read word
    word = input("Enter a word --> ")
    if word == "chupacabra":
        break

# show the final message
print("You've left the loop successfully.")