import random
import time

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = arr[l:m + 1]
    R = arr[m + 1:r + 1]
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arrays = [
    list(range(1, 101)), 
    list(range(100, 0, -1)),  
    list(range(1, 26)) + list(range(75, 25, -1)) + list(range(76, 101)),  
    list(range(25, 0, -1)) + list(range(26, 76)) + list(range(100, 75, -1)), 
    list(range(50, 0, -1)) + list(range(100, 50, -1))  
]

arrays.extend([random.sample(range(1, 101), 100) for _ in range(5)])

sort_algorithms = {
    "QuickSort": lambda arr: quickSort(arr, 0, len(arr) - 1),
    "MergeSort": lambda arr: mergeSort(arr, 0, len(arr) - 1),
    "HeapSort": lambda arr: heapSort(arr),
    "InsertionSort": lambda arr: insertionSort(arr)
}

cumulative_runtimes = {algo: 0.0 for algo in sort_algorithms}

print(f"{'Array #':<10} {'QuickSort':<12} {'MergeSort':<12} {'HeapSort':<12} {'InsertionSort':<12}")
print("=" * 60)

for i, arr in enumerate(arrays, start=1):
    times = []
    for sort_name, sort_func in sort_algorithms.items():
        arr_copy = arr[:]
        start_time = time.time()
        sort_func(arr_copy)
        elapsed_time = time.time() - start_time
        cumulative_runtimes[sort_name] += elapsed_time  
        times.append(f"{elapsed_time:.6f}")
    print(f"{i:<10} {times[0]:<12} {times[1]:<12} {times[2]:<12} {times[3]:<12}")

avg_times = [f"{(cumulative_runtimes[algo] / 10):.6f}" for algo in sort_algorithms]
print("=" * 60)
print(f"{'Average':<10} {avg_times[0]:<12} {avg_times[1]:<12} {avg_times[2]:<12} {avg_times[3]:<12}")