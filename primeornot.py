n=int(input("Enter the number"))
counter=0
for i in range(1,n+1):
    if n%i==0:
        counter=counter+1
if counter==2:
    print(n," is a prime number")
else:
    print(n," is not a prime number")
    
