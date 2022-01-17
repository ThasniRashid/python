
l1=[1,2,4,5]
l2=[6,7,8,3]
print(l1)
print(l2)
def list(l1,l2):
    for i in l1:
        for j in l2:
            if i==j:
                return(True)
            
if(list(l1,l2)):
    print("common elements")
else:
    print("not common elements")
                
            

