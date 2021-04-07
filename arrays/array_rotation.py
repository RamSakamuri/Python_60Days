"""
Array rotation
"""


def arrayRotation(arr, pos, n):
    arr[:] = arr[pos:n] + arr[0:pos]


def reverseArray(arr, start, end):
    while(start < end):
        temp = arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start = start + 1
        end = end - 1




array1 = [10, 5, 6, 3, 5, 12, 1, 5]
# arrayRotation(array1, 5, len(array1))
print(array1)
reverseArray(array1, 0, len(array1)-1)
print(array1)
