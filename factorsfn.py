n=int(input("Enter a number: "))
def fact(s):
    for i in range(1,s+1):
        if s%i==0:
            print(i)
fact(n)
        
