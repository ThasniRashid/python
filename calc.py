a=int(input("Enter the value of A: "))
b=int(input("Enter the value of B: "))
def calc(x,y):
    s=x+y
    d=x-y
    p=x*y
    div=x/y
    return(s,d,p,div)
l=calc(a,b)
print("Sum= ",l[0])
print("Difference= ",l[1])
print("Product= ",l[2])
print("division= ",l[3])


