l1=[5,2,3,1]
l2=[1,6,3,12]
print(l1)
print(l2)
c=0
if(len(l1)==len(l2)):
    print("lists are equal length")
else:
    print("sets are not equal")
if sum(l1)==sum(l2):
        print("sum of both lists are equal")
else:
        print("sum of both lists are not equal")
    
for i in l1:
    for j in l2:
        if i==j:
            c=c+1
            print(i)
if c==0:
    print("common elements does not exist")
else:
    print("common elements exist")
    
