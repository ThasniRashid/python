a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=int(input("Enter the 3rd number: "))
if a<b:
    if a<c:
        print(a," is smallest ")
    else:
        print(c," is smallest ")
else:
    if b<c:
        print(b," is smallest")
    else:
        print(c," is smallest")
    
