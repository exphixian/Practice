"""Python 3 script to print names in a list in a first m. last format"""

#replace with the file path to the document you are going to use
file = open("/home/user/Documents/document.txt", "r")

#To check if the file is being read properly
#print(file.read())
x = 0
name = []
for i in file:
    x += 1
    print(x)
    name = str.split(i)

#To check if the list is being created properly
#    print(name)
    if name[1] != name[-1]:
        name[1] = " " + name[1][0] + ". "
    if name [2] != name [-1]:
        name[2] = name[2][0] + ". "

#If users have more than one middle name
#    if name[3] != name[-1]:
#        name[3] = name[3][0] + ". "
    name =''.join(name)
    print(name)
    print ()
