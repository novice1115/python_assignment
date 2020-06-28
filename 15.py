#insertion of a string in the middle of the other string
def insertString(str1, str2):
	return str1[:2] + str2 + str1[2:]

print(insertString('[[]]', 'Python'))
print(insertString('{{}}', 'PHP'))
