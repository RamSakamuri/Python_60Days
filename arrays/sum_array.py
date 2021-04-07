"""
Python Program to find sum of array
"""

def findSumArray(arr):
    sum:int = 0
    for element in arr:
        sum += element
    return sum


print(findSumArray([10,  11, 12]))


