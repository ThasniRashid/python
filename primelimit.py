x=int(input("Enter the 1st limit :"))
y=int(input("Enter the 2nd limit :"))
while(x<=y):
    counter=0
    for i in range(1,x+1):
        if x%i==0:
            counter=counter+1
    if counter==2:
        print(x)
    x=x+1
    
   
    
    
