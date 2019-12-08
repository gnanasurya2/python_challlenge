string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
length = len(string)
new_string = ''
#Since from the picture it's clear that every character is being shifted two characters in the front.
for i in range(0,length,1):
    num = ord(string[i])
    if (num >= 97 and num <= 122):
        num = num + 2
        if num > 122:
            num = num - 26
    char = chr(num)
    new_string = new_string + char
print(new_string)
#the output of new_string suggests us to apply the same to the url.
new_string =''
url_string ="map"
length = len(url_string)
for i in range(0,length,1):
    num = ord(url_string[i])
    if (num >= 97 and num <= 122):
        num = num + 2
        if num > 122:
            num = num - 26
    char = chr(num)
    new_string = new_string + char
print(new_string)