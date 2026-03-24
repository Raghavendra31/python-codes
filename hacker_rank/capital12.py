def capitalize(s) -> str:

    words = s.split(" ")
    result = []

    for word in words:
        if word and word[0].isalpha():   # check if first char is a letter
            word = word[0].upper() + word[1:]
        result.append(word)

    return " ".join(result)

s = "ragu ruler"
print(capitalize("12 212 casx"))



# str(s)
#     if isinstance(s, int):
#         return s
#     s = s.split(" ")
#     for i in range (0 , len(s)):
#         s[i] = s[i][0].upper() + s[i][1:]
    
    
#     result = ' '.join(s)
#     return result


