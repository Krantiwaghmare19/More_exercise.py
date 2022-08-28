words=input("enter the words")
list=[]
string=" "
for i in  words:
    if i in words:
        if i==" ":
            list.append(string)
            string=" "
        else:
            string=string+i
if string:
    list.append(string)
    print(list)