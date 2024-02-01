def subtotal(arr):
    for i in range(1, len(arr)):
        arr[i] = arr[i] + arr[i - 1]

    return arr

# Test the function with an example array
arr = [5.8, 2.6, 9.1, 3.4, 7.0]
subtotal(arr)

# Print the modified array 
print("Modified Array:", arr)

