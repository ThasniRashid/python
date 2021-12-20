s=input("Enter the string: ")
ls=list(s)
for i in ls:
    c=0
    if i!=" ":
        for j in range(0,len(ls)):
            if i==ls[j]:
                c=c+1
                ls[j]=" "
        print(i,"=",c)
