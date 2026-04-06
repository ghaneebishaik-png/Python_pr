import json
with open("D:\Python practice/file2.json","r") as json_data:
    data = json.load(json_data)
print(data)
print(type(data))

#json.load():to load json data as dictionary data
#json.loads(): to load dictionary data from string
#json_string = '{"a":10,"b":20,"c":30}'
with open("D:\Python practice/file3.txt","r") as json_string:

    data1 = json.loads(json_string)
print(data1)

