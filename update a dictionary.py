#update a dictionary
a={}
size=int(input('enter a size'))
for i in range(0,size):
    key=input("enter key")
    value=input("enter value")
    a[key]=value
a.update({9:0})
print(a)