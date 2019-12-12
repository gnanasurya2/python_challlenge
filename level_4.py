# importing regular expression module
import re
# copying the text from page source and storing it in level_4.txt
text = open('level_4.txt')
text = text.read()
# using pattern searching to find all the small letters
print(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", text))
