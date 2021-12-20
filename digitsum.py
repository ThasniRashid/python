n=int(input("Enter the number: "))
s=l=0
while(n>0):
    l=n%10
    s=s+l
    n=n//10
print("sum: ",s)
    
    
