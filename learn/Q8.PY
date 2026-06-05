#USER INPUT
def larger(a,b,c):
    lrg=a
    if(b>a):
        lrg=b
    if(c>a):
        lrg=c
    return lrg


a = int(input("enter a : "))
b = int(input("enter b : "))
c = int(input("enter c : "))

z = larger(a,b,c)
print(z)