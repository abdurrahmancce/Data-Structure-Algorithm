arr = [1, 2, 3, 4, 5]

print(arr[0])    # Output: 1

arr[0] = 10
print(arr)       # Output: [10, 2, 3, 4, 5]

print(len(arr))  # Output: 5

print(arr[-1])   # Output: 5

arr.append(6)    # Adds to end
print(arr)       # Output: [10, 2, 3, 4, 5, 6]

arr.pop()        # Removes last element
print(arr)       # Output: [10, 2, 3, 4, 5]