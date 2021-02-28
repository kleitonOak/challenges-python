#!/usr/bin/env python
rangeList = range(10)

print(rangeList)

for number in rangeList:
    # Check if number is one of the number in the tuple
    if(number in (3,4,7,9)):
        # Break terminates a for without executing the else clause
        break
    else:
        # Continue starts the next iteration of the loop. It's rather useless here,
        # as it's the last statement of the loop
        continue
else:
    # The "Else" clause is optional and is
    # executed only if the loop didn't break.
    pass

if rangeList[1] == 2:
    print("Tghe second item (list are 0-based) is 2")
elif rangeList[1] == 3:
    print("The second item (list are 0-based) is 3")
else:
    print("Dunno")
