company = {
    "department1":{
        "name" : "sales",
        "emplyees":{
            "e1":{"name" : "John", "age":30,"position":"manager"},
            "e2":{"name": "Alice", "age":25,"position":"sales associate"}
        },
        "budjet":100000
    },
    "department2" : {
        "name" : "Engineering",
        "emplyees":{
            "e3":{"name" : "Bob", "age":35,"position":"team lead"},
            "e4":{"name": "Charlie", "age":28,"position":"software Engineer"}
        },
        "budjet":200000
    },
    "department3": {
        "name" : "Marketing",
        "emplyees":{
            "e5":{"name" : "Devid", "age":32,"position":"marketing manager"},
            "e6":{"name": "Eve", "age":27,"position":"SEO specialist"}
        },
        "budjet":50000
    }
}

#Print all keys from above dict

list1 = company.keys()#dict_keys(['department1', 'department2', 'department3'])
print(list1)

#Print "department1"
for k,v in company.items():
    print(k)#department1
    break

#To get the total budget of the cumpany[summing all department budgets]

tot_bud = 0
for k,v in company.items():#k is department,v is {name,employees,budget}
    for k1,v1 in v.items():#k1 is {name,employees,budget},v1 is values of name,employees,budget(100000,200000,50000)
        if k1 == "budjet":
            tot_bud += v[k1]#tot_bud = 0+100000, then 100000+200000, then 300000+50000

print(tot_bud)#350000

#########################
#To get age of "John"

step1 = company["department1"]["emplyees"]["e1"]["name"]#John
print("John")
########################################
#To get the position of Devid

step2 = company["department3"]["emplyees"]["e5"]["name"]#Devid
print(step2)

###########################
#which department has lowest budget
#None is used as a safe initial placeholder when finding min/max values dynamically.
#No department budget is less than 0; Condition dept["budjet"] < min_budget is never true; Result stays wrong

min_bud = None
min_dep = ""

for dep in company.values():
    if min_bud is None or dep["budjet"] < min_bud:
        min_bud = dep["budjet"]
        min_dep = dep["name"]

print(min_bud)#50000
print(min_dep)#Marketing

#########################################
#Method 2

first_key = list(company.keys())[0]
min_budget = company[first_key]["budjet"]
min_department = company[first_key]["name"]

for dept in company.values():
    if dept["budjet"] < min_budget:
        min_budget = dept["budjet"]
        min_department = dept["name"]

print(min_budget)
print(min_department)

###############################################

