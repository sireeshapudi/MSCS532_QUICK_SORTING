import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)  # random pivot selection
    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return randomized_quicksort(left) + middle + randomized_quicksort(right)


arr = [8, 3, 1, 7, 0, 10, 2]
print(randomized_quicksort(arr))
