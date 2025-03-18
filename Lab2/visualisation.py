import matplotlib.pyplot as plt
import random
import time

def visualize_sorting(sorting_algorithm, arr, title):
    fig, ax = plt.subplots()
    ax.set_title(title)

    bars = ax.bar(range(len(arr)), arr, color='blue')

    def update_plot(arr):
        for bar, height in zip(bars, arr):
            bar.set_height(height)
            bar.set_color('red')  
        plt.pause(0.01)  

    sorting_algorithm(arr, update_plot)
    plt.show()

def quick_sort(arr, update_plot, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                update_plot(arr)
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    if low < high:
        pi = partition(low, high)
        quick_sort(arr, update_plot, low, pi - 1)
        quick_sort(arr, update_plot, pi + 1, high)

    update_plot(arr)

def merge_sort(arr, update_plot, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    def merge(left, mid, right):
        L = arr[left:mid + 1]
        R = arr[mid + 1:right + 1]

        i = j = 0
        k = left
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            update_plot(arr)
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            update_plot(arr)

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            update_plot(arr)

    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, update_plot, left, mid)
        merge_sort(arr, update_plot, mid + 1, right)
        merge(left, mid, right)

    update_plot(arr)

def heap_sort(arr, update_plot):
    def heapify(n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            update_plot(arr)
            heapify(n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        update_plot(arr)
        heapify(i, 0)

    update_plot(arr)

def insertion_sort(arr, update_plot):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            update_plot(arr)
        arr[j + 1] = key

    update_plot(arr)

array_size = 100
arr = random.sample(range(1, array_size + 1), array_size)

sorting_algorithms = {
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort,
    "Heap Sort": heap_sort,
    "Insertion Sort": insertion_sort
}

for name, algo in sorting_algorithms.items():
    arr_copy = arr.copy()
    visualize_sorting(algo, arr_copy, name)
