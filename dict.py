"""Dict methods
1.Adding key and value at the end of the existing dict
2.listing keys and values
3.accessing the value with the help of key
4. deleting an item
5.update
6.pop(key) and popitem()


dict1={"a":"Australia", "b":"Ball","c":"collage"}
dict2={"1":"Number","2":"calender"}

dict2["3"]="India"
print(dict2)

print(dict1.keys())
print(dict2.values())
print(dict1.items())

print(dict2["2"])

del dict1["c"]
print(dict1)

dict2.pop("1")
print(dict2)

dict1.update({"d":"dance","e":"Eme"})
print(dict1)

"""

data={10:20,30:11,40:50}

if 10 in data:
    print("It is exested")
else:
    print("It is not exested")

data.pop(30)
print(data)