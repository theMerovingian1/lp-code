# Rushikesh Borade TE Comp 7
# Exp 3: Greedy Algorithm using Selection Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        print(f"Iteration: {i}")
        print(arr)
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


arr = []
n = int(input("Number of elements in array: "))
for i in range(n):
    element = int(input("Enter element for index {}: ".format(i)))
    arr.append(element)

print("Array before sorting: ", arr)
print("Array after sorting: ", selection_sort(arr))
