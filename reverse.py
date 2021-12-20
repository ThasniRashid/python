n=int(input("Enter the number: "))
s=l=0
while(n>0):
    l=n%10
    s=s*10+l
    n=n//10
print("reverse: ",s)
    
