#QA-Pthoyn
#Most Important Interview Question
"""
Q: Why Python data types are important in QA automation?

Strong Answer:

“Correct data types ensure reliable validations, prevent runtime errors, improve performance,
 and make automation frameworks stable.”

"""
#Validate test input data(Empty or list)

lst=[]#Before running a test ensure test data is not empty
if not lst:
    print("lst is empty-skip execution")
else:
    print("Proceed with test data execution")

#Remove duplicate testcases from execution list

#Test cases duplicated due to multiple test plans
#1
Test_cases=["tc01","tc02","tc01","tc03"]
Exe_lst=[]

for i in Test_cases:
    if i not in Exe_lst:
        Exe_lst.append(i)
print(Exe_lst)#['tc01', 'tc02', 'tc03']

#2
print(list(set(Test_cases)))#avoid re-running same test. Save execution time.

#Verify required keys in API response(dict)
#Check wheathe API response contains mandatory fields.

response={"status":200,"device":"SSD","capacity":"1TB"}
req_keys={"status","device","capacity"}
#1
if req_keys.issubset(response):
    print("API response validation passed")
else:
    print("API validation failed")

2#
req_keys=["status1","device","capacity"]

is_valid=True
for i in req_keys:
    if i not in response:
        is_valid = False
        break
if is_valid:
    print("API response validation passed")
else:
    print("API validation failed")


###Compare Expected Vs Actual output(Storage Validation)
#Validate FW version after upgrade

exp_fw="2.1.0"
act_fw="2.1.0"

assert exp_fw == act_fw, "FW mismatch"
print("Passed the FW upgrade")


###Log test result status using boolean
#Boolean improoves readability in automation framework

test_passed = True

if test_passed:
    print("Test Case: PASS")
else:
    print("Test Case: FAIL")


####Count failed test cases from result(list+dict)

results=[
    {"tc":"tc01","status":"passed"},
    {"tc":"tc02","status":"Fail"},
    {"tc":"tc03","status":"Fail"}
]

failed_count=0

for i in results:
    if i["status"] == "Fail":
        failed_count += 1
print("The failed tc count is", failed_count)

###Validate disc capacity
#capacity returned as string(string to int)

capacity="1024"

if int(capacity)>=1024:
    print("capacity validation passed")
else:
    print("Validation Failed")

###Detect configuration change(Tuple immutability)
#Prevent conf modification during test run

config=("Nvme","PCIe4","Enabled")#Tuple ensures config remains unchanged
print("config locked",config)

###Find common failed tests accross multiple runs(Set)

run1_failed={"tc01","tc02","tc03","tc05"}
run2_failed={"tc02","tc03","tc04"}

common_failures = run1_failed & run2_failed
print(common_failures)#Used in regression analysis


###Dynamic test case execution(For Loop)

test_cases=["tc01","tc02","tc03"]
for tc in test_cases:
    print(f"Execuiting {tc}")