#sort a dictionary
a={}
size=int(input('enter a size'))
for i in range(0,size):
    key=input("enter key")
    value=input("enter value")
    a[key]=value
for key in sorted(a):
    print('%s:%s'%(key,a[key]))
