# Write a program to sort an array of integers.
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
 
 
arr = np.random.randint(1, 101, 5)
print(arr) 
bubbleSort(arr)
 
print("Sorted array is:")
print(arr)

