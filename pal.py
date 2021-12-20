n=int(input("Enter the number: "))
a=n
s=l=0
while(n>0):
    l=n%10
    s=s*10+l
    n=n//10
if a==s:
    print("The number is palindrome")
else:
    print("The number is not palindrome")
    
    
