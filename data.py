def max_subarray(arr):
    max_current = arr[0]
    max_global = arr[0]

    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        max_global = max(max_global, max_current)

    return max_global

arr = list(map(int, input("Enter elements: ").split()))
print("Maximum Subarray Sum:", max_subarray(arr))
