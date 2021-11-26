def mysplit(string = ""):
    ''' own function, which
behaves almost exactly like the original split()
Argument: exactly one argument -> string
Returns: list of words created from the string,
divided by whitespaces (returns empty list if string is empty)  '''

    string = string.strip() # delete leading and trailing spases 
    # init empty list
    my_list = []
    # init word by empty
    word = ""
    # loop by character in input string
    for ch in string:
        if ch != ' ':
            word += ch  # add character to word if it is not space
        elif word != "":
            my_list.append(word)    # add word into end of list
            word = ""               # init word by empty
    
    if word != "":
        my_list.append(word)

    return my_list  # return list of words or empty list