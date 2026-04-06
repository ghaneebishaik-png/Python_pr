"""STRING METHODS
1.Concatenation and Repetation
2.split and join
3.position and indexing
4.sclicing
5.replace
6.isdigit
7.lower and upper
8.startswith and endswith
9.count
10.strip
"""

data1="Ajay kumar"
data2="Kums"
print('2'+'2')

out=data1.split('a')
print(out)
data="Ajay kumar"
data=['100','200','300']
out="9".join(data)
print(out)
print(data1.index('y'))
print(data1[3])
print(data1[3:6])
print(data1.replace("a","b"))

data3="23"
print(data3.isdigit())
print(data1.lower())
print(data1.upper())
print(data1.count("A"))

data4="    /n/t  khadar  /n/t   "
print(data4.strip())

data5="accounts.xls"
print(data5.endswith(".xlsx"))
print(data5.startswith("acc"))
data6=["a","b","c"]
print("kk".join(data6))
print(data5.split("."))