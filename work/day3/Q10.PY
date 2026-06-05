keys = ["name","age","city"]
values = ["ali",20,"calicut"]

def create_dictionary(keys,values):
    return dict(zip(keys,values))
result = create_dictionary(keys,values)
print(result)
    