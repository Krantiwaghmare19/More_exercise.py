list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
i=0
l=[]
while i<len(list2):
    list1.append(list2[i])
    j=0
    while j<len(list1):
        if list1[j] not in l:
            l.append(list1[j])
        j=j+1
    i=i+1
print(l)
        