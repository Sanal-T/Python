def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Main program
print("Select sorting algorithm:")
print("1. Bubble Sort")
print("2. Insertion Sort")
print("3. Quick Sort")
print("4. Merge Sort")

choice = int(input("Enter choice (1/2/3/4): "))

arr = list(map(int, input("Enter numbers separated by space: ").split()))

if choice == 1:
    bubble_sort(arr)
    print("Sorted array (Bubble Sort):", arr)
elif choice == 2:
    insertion_sort(arr)
    print("Sorted array (Insertion Sort):", arr)
elif choice == 3:
    arr = quick_sort(arr)
    print("Sorted array (Quick Sort):", arr)
elif choice == 4:
    merge_sort(arr)
    print("Sorted array (Merge Sort):", arr)
else:
    print("Invalid choice!")
