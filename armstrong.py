n=int(input("Enter a number:"))
def digit(s):
    sum=l=0
    temp=s
    while(s>0):
        l=s%10
        sum=sum+(l**3)
        s=s//10
    if temp==sum:
        print(temp,"armstrong")
    else:
        print( temp,"not armstrong")
        
digit(n)
