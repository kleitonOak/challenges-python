#!/usr/bin/env python
list1 = [1,2,3]
list2 = [3,4,5]

print([ x for x in list1 if(4 < x > 1)])

# Check if a condition is true for any itenms
# any returns true if any item in the list is true
# This returns true because 4 % 3 = 1, and 1 is true
any([i % 3 for i in [3,3,4,4,3]])

# This returns the value 2, because the are just two itens igual 4
sum(1 for i in [3,3,4,4,3] if i == 4)

print("List 1 before delete %s" % list1)
del list1[0]
print list1
del list2

# This is a error, because o delete the variable
print("List 2 after deleted - %s " % list2)
