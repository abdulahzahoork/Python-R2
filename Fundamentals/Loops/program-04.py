# Find the largest number: Given the list [12, 45, 7, 89, 23], find the largest number without using max().

arr = [12, 45, 7, 89, 23]
arr_max = 0
for i in range(1, len(arr)):
    if (arr[i] > arr[arr_max]):
        arr_max = i

print(f"Largest number: {arr[arr_max]}")