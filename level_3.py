# the text from the the page source to copied to the filed named 'level_3.txt
text = open("level_3.txt")
char = []
for line in text:
    for c in line:
        if c not in char:
            char.append(c)
print(char)
# the aplhabet in the char are "equality" changes it in the url
