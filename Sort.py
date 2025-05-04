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


# Main program
print("Select sorting algorithm:")
print("1. Bubble Sort")
print("2. Insertion Sort")
print("3. Quick Sort")

choice = int(input("Enter choice (1/2/3): "))

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
else:
    print("Invalid choice!")
