import re

"""
str1="Linux kernel is RHEL and version is 91.2"
pattern="Linux kernel is (\w+) and version is (\d+.\d+)"

out = re.search(pattern,str1)
kernel = out.group(1)
version = out.group(2)
print(kernel,version)

#final=out.group(1)
#print(final)

"""

#gmail validation
gmail_id = "ghaneebishaik@gmail.com"

pattern = "\w+\W\w+\.\w+"

res = re.match(pattern, gmail_id)
print(res)

#ip address validation

ip = "160.120.3.44"
pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

out = re.match(pattern,ip)
print(out)

#Validating mac address

mac_ip = "92-E8-68-13-83-3D"

pattern = "\w{1,2}\W\w{1,2}\W\w{1,2}\W\w{1,2}\W\w{1,2}\W\w{1,2}"
out1 = re.match(pattern,mac_ip)
print(out1)

#Validating mobile number

mob_no = "9387710758"
pattern = "^[6-9]{1}\d{9}$"
#pattern = "\d+" , \d{9},\d{10},\d{11}
# ^ should starts with particular char
#$ should end with a particular char
result = re.match(pattern,mob_no)
print(result)