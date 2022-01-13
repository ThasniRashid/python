a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=int(input("Enter the 3rd number: "))
def sum(x,y,z):
    s=x+y+z
    if x==y==z:
        return(3*s)
    else:
        return(s)
print("sum=",sum(a,b,c))
