import matplotlib.pyplot as plt

array_indices = list(range(1, 11))
quick_sort_times = [0.000286, 0.000198, 0.000191, 0.000170, 0.000109, 0.000038, 0.000043, 0.000072, 0.000040, 0.000040]
merge_sort_times = [0.000071, 0.000067, 0.000067, 0.000066, 0.000064, 0.000072, 0.000073, 0.000077, 0.000074, 0.000074]
heap_sort_times = [0.000102, 0.000082, 0.000092, 0.000093, 0.000088, 0.000091, 0.000090, 0.000093, 0.000123, 0.000138]
insertion_sort_times = [0.000007, 0.000254, 0.000067, 0.000035, 0.000124, 0.000120, 0.000155, 0.000154, 0.000208, 0.000137]

quick_sort_avg = sum(quick_sort_times) / len(quick_sort_times)
merge_sort_avg = sum(merge_sort_times) / len(merge_sort_times)
heap_sort_avg = sum(heap_sort_times) / len(heap_sort_times)
insertion_sort_avg = sum(insertion_sort_times) / len(insertion_sort_times)

print(f"{'Array':<10} {'QuickSort':<12} {'MergeSort':<12} {'HeapSort':<12} {'InsertionSort':<12}")
print("=" * 60)

for i in range(len(array_indices)):
    print(f"{array_indices[i]:<10} {quick_sort_times[i]:<12.6f} {merge_sort_times[i]:<12.6f} {heap_sort_times[i]:<12.6f} {insertion_sort_times[i]:<12.6f}")

print("=" * 60)
print(f"{'Average':<10} {quick_sort_avg:<12.6f} {merge_sort_avg:<12.6f} {heap_sort_avg:<12.6f} {insertion_sort_avg:<12.6f}")


plt.figure(figsize=(10, 6))
plt.plot(array_indices, quick_sort_times, label='QuickSort', marker='o')
plt.plot(array_indices, merge_sort_times, label='MergeSort', marker='s')
plt.plot(array_indices, heap_sort_times, label='HeapSort', marker='^')
plt.plot(array_indices, insertion_sort_times, label='InsertionSort', marker='D')

plt.xlabel('Array Number')
plt.ylabel('Runtime (seconds)')
plt.title('Sorting Algorithm Execution Times')
plt.legend()
plt.grid(True)
plt.savefig('sorting_times.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(array_indices, quick_sort_times, marker='o', label='QuickSort Times')
plt.axhline(y=quick_sort_avg, color='black', linestyle='--', label='Average')
plt.xlabel('Array Number')
plt.ylabel('Runtime (seconds)')
plt.title('QuickSort Execution Times')
plt.legend()
plt.savefig('quick_sort_times.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(array_indices, merge_sort_times, marker='o', label='MergeSort Times')
plt.axhline(y=merge_sort_avg, color='black', linestyle='--', label='Average')
plt.xlabel('Array Number')
plt.ylabel('Runtime (seconds)')
plt.title('MergeSort Execution Times')
plt.legend()
plt.savefig('merge_sort_times.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(array_indices, heap_sort_times, marker='o', label='HeapSort Times')
plt.axhline(y=heap_sort_avg, color='black', linestyle='--', label='Average')
plt.xlabel('Array Number')
plt.ylabel('Runtime (seconds)')
plt.title('HeapSort Execution Times')
plt.legend()
plt.savefig('heap_sort_times.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(array_indices, insertion_sort_times, marker='o', label='InsertionSort Times')
plt.axhline(y=insertion_sort_avg, color='black', linestyle='--', label='Average')
plt.xlabel('Array Number')
plt.ylabel('Runtime (seconds)')
plt.title('InsertionSort Execution Times')
plt.legend()
plt.savefig('insertion_sort_times.png')
plt.show()
