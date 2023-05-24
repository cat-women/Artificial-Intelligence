# 6. Write a function that combines two lists/arrays by alternatingly taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].

import numpy as np
arr1 = np.random.randint(1, 101, 5)
arr2 = np.random.randint(1, 101, 5)

print("array one",arr1)
print(arr2)
arr3 = []
for i in range(len(arr1)):
    for j in range(len(arr2)):
        arr3.append(arr1[j])
        arr3.append(arr2[j])
    break

print(arr3)



