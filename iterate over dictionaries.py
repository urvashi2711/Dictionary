#iterate over dictionaries
a={}
size=int(input('enter a size'))
for i in range(0,size):
    key=input("enter key")
    value=input("enter value")
    a[key]=value
for key,value in a.items():
    print(key,'corresponds to',a[key])