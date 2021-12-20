a=int(input("Enter the 1st limit :"))
b=int(input("Enter the 2nd limit :"))
if a%2!=0:
    a=a+1
if a>=b:
    print("invalid operation")
for i in range (a,b+1,2):
    print(i)
