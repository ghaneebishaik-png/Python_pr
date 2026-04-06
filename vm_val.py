import re

vm_details = '''VM1 :: Centos
VM2 :: Ubuntu
VM3 :: RHEL9
VM4 :: Windows8'''

#Expected output = {"VM1" : "Centos", "VM2" : "Ubuntu", "VM3":"RHEL9", "VM4" = "Windows8"}

line = vm_details.split("\n")
print(line)#['VM1 :: Centos', 'VM2 :: Ubuntu', 'VM3 :: RHEL9', 'VM4 :: Windows8']
dict1={}
for i in line:    
    obj = re.search("(VM[0-9])\s::\s(\w+)",i)
    if obj:
        name=obj.group(1)
        obj_type=obj.group(2)
        dict1[name]=obj_type

print(dict1)