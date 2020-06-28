#Defining functions for the string at both the ends
def stringEnds(str):
    if len(str) < 2:
        return "Empty String"

    return str[0:2] + str[-2:]


print(stringEnds('Python'))
# print(stringEnds('Py'))
print(stringEnds('s'))
