#!/usr/bin/env python

def mintrip(maxweigth, listpackage):
	trips = 0;
	sortedArrayPackage = sorted(listpackage,reverse=True)
	begin = 0
	end = len(sortedArrayPackage) - 1

	while(begin <= end):
		onePackage = sortedArrayPackage[begin]
		otherPackage = sortedArrayPackage[end]
		if(onePackage + otherPackage <= maxweigth):
			begin += 1
			end -= 1
		else:
			end -= 1
		trips += 1
	return trips

arrayPackage = [70,20,80,20]
print mintrip(100,arrayPackage)
