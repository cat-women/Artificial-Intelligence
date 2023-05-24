
import numpy as np

def bubbleSort(arr):
    n = len(arr)
    
    swapped = False   
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return
 


arr1 = np.random.randint(1, 101, 5)
arr2 = np.random.randint(1, 101, 5)

print(arr1)
print(arr2)

arr3 = []

for i in range(len(arr1)):
    arr3.append(arr1[i])


for j in range(len(arr2)):
    arr3.append(arr2[j])

print(arr3)
bubbleSort(arr3)
print(arr3)


