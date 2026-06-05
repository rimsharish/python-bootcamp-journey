list=[3,4,5,6,7,8]

for i in list:
    print(i)

def filterEven(list):
    even = []
    for num in list:
        if(num%2==0):
            even.append(num)
    return even
        
print(filterEven(list)) #or
...
l1 = filterEven(list)
print(l1)
...
