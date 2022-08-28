print("create a strong password" )
ch=input("enter the uppercase letter")
if ch>="A" and ch<="Z":
    print(ch)
    ch2=input("enter the lowercase letter")
    if ch2>="a" and ch2<="z":
        print(ch2)
        num=int(input("enter the number"))
        if num>=1 and num<=9:
            print(num)
            sc=input("enter the sc")
            if sc=="@" or sc=="#":
                print(sc)
                print("This is strong password")
            else:
                print("incorrect sc")
        else:
            print("incorrect number")
    else:
        print("incorrect ch2")
else:
    print("incorrect ch")



print("create a strong password")
ch=str(input("enter the alpha"))
if ch>="A" or "a" and ch<="Z" or "z":
    digit=(input("enter the number"))
    sc=input("enter  the special character")
    if sc=="#" or sc=="@" or sc=="$" or sc=="&":
        print("your password")
        a=(ch+digit+sc)
        if len(a)>=6 or len(a)<=16:
            print("strong password")
            print(a)
        else:
            print("pilase enter password length 6 and 16")
    else:
        print("this is not strong password")
        print("please create strong password")
else:
    print("something wrong")    
