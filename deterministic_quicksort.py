def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]  # choosing last element as pivot
    left = []
    right = []

    for i in range(len(arr) - 1):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quicksort(left) + [pivot] + quicksort(right)


arr = [8, 3, 1, 7, 0, 10, 2]
print(quicksort(arr))
