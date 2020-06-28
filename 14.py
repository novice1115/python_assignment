def addTags(tag, string):
	return "<%s>%s</%s>" % (tag, string, tag)
print(addTags('i', 'Python'))
print(addTags('b', 'Python Tutorial'))
print(addTags('h1', 'Python Tutorial'))