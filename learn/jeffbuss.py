#3* jeff
#5* buss
#3,5 jeffbuss
#else i

for i in range(1,31):
    if(i%3==0 and i%5==0):
        print(f"jeffbuss - {i}")
    elif(i%3==0):
        print(f"jeff - {i}")
    elif(i%5==0):
        print(f"buss - {i}")
    else:
        print(i)
