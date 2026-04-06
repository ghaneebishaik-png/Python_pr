##Shallow copy:: Shallow copy creates a new object, but doesn't copy nested inner objects.
# Both original and copy share references to inner object. ***Changing nested data effects the original data.***
##Deepcopy:: A deep copy creates completely independednt copy, including all nested objects.
# ***Original data unchamged when changing nested data.***


import sys
import copy

##We are using input as nested list, if we update the shallow copy nested [list] the original list updated as well.
# But if we update the deepcopy the original nested list remains same.
original=[[1,2],[3,4]]
shallow=copy.copy(original)

shallow[0][1]=66

print(original)#[[1, 66], [3, 4]]
print(shallow)#[[1, 66], [3, 4]]
#shallow[1][1]=88

#print(shallow)
#print(original)

deepcopy=copy.deepcopy(original)
deepcopy[0][1]=77
print(deepcopy)#[[1, 77], [3, 4]]
print(original)#[[1, 66], [3, 4]]

print(sys.getsizeof(original))
print(sys.getsizeof(shallow))
print(sys.getsizeof(deepcopy))
print(sys.getsizeof(original))

"""
##If we usig input as a list shallow copy and deepcopy both are updated.
#  but the original input remains same if you update shallow and deep copy.
ori=[1,2,3,4]

shallow=copy.copy(ori)#[1, 2, 3, 4]
shallow[0]=55

print(shallow)#[55, 2, 3, 4]
print(ori)#[1, 2, 3, 4]

deep=copy.deepcopy(ori)#[1, 2, 3, 4]
deep[0]=66

print(deep)#[66, 2, 3, 4]
print(ori)#[1, 2, 3, 4]

"""