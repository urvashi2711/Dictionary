#check dictionary is empty or not
a={}
size=int(input('enter a size'))
for i in range(0,size):
    key=input("enter key")
    value=input("enter value")
    a[key]=value
if(len(a)==0):
    print('The dictionary is empty')
else:
    print('The dictionary is not empty')