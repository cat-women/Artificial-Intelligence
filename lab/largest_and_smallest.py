import numpy as np
arr = np.random.randint(1, 101, 5)
largest = arr[0]
lowest = arr[0]
largest2 = None
lowest2 = None
for item in arr[1:]:
    if item > largest:
        largest2 = largest
        largest = item
    elif largest2 is None or largest2 < item:
        largest2 = item
    if item < lowest:
        lowest2 = lowest
        lowest = item
    elif lowest2 is None or lowest2 > item:
        lowest2 = item

print(arr)
print("largest number is ",largest,"smallest number is ",lowest)
