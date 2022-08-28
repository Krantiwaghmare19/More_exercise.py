# x = 42
# x_digits = list(str(x))


a=int(input("enter the number"))
i=a
sum=0
while i>0:
    sum=sum+(i%10)
    i=i//10
if a%sum==0:
    print("harshad number")
else:
    print("not harshad number")