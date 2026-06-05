word = "apple"

store = {}

for char in word:
    if char  in store:
        store[char]+=1
    else:
        store[char]=1
print(store)
    