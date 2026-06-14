import random
list = ['rim','abd','imran','fathima','lana']



try:
    index1= int(input("enter an index: "))
    if 0<= index1<= len(list):
        print(list[index1])
except ValueError:
    print("valueError found")

index2= int(input("enter an index: "))


    
try:
    if 0 <= index2<= len(list):
        print(list[index2])
except IndexError:
    print("IndexError Found")


rand = random.choice(list)
print(f"random choice = {rand}")



