import matplotlib.pyplot as plt

array_indices = list(range(1, 11))
quick_sort_times = [0.000435, 0.000212, 0.000327, 0.000226, 0.000119, 0.000062, 0.000077, 0.000083, 0.000066, 0.000073]
merge_sort_times = [0.000072, 0.000123, 0.000122, 0.000068, 0.000091, 0.000119, 0.000137, 0.000124, 0.000127, 0.000131]
heap_sort_times = [0.000142, 0.000133, 0.000164, 0.000093, 0.000087, 0.000146, 0.000145, 0.000153, 0.000159, 0.000145]
bubble_sort_times = [0.000004, 0.000614, 0.000256, 0.000082, 0.000233, 0.000404, 0.000393, 0.000396, 0.000412, 0.000399]

quick_sort_avg = sum(quick_sort_times) / len(quick_sort_times)
merge_sort_avg = sum(merge_sort_times) / len(merge_sort_times)
heap_sort_avg = sum(heap_sort_times) / len(heap_sort_times)
bubble_sort_avg = sum(bubble_sort_times) / len(bubble_sort_times)

print(f"{'Array':<10} {'QuickSort':<12} {'MergeSort':<12} {'HeapSort':<12} {'BubbleSort':<12}")
print("=" * 60)

for i in range(len(array_indices)):
    print(f"{array_indices[i]:<10} {quick_sort_times[i]:<12.6f} {merge_sort_times[i]:<12.6f} {heap_sort_times[i]:<12.6f} {bubble_sort_times[i]:<12.6f}")

print("=" * 60)
print(f"{'Average':<10} {quick_sort_avg:<12.6f} {merge_sort_avg:<12.6f} {heap_sort_avg:<12.6f} {bubble_sort_avg:<12.6f}")


plt.figure(figsize=(10, 6))
plt.plot(array_indices, quick_sort_times, label='QuickSort', marker='o')
plt.plot(array_indices, merge_sort_times, label='MergeSort', marker='s')
plt.plot(array_indices, heap_sort_times, label='HeapSort', marker='^')
plt.plot(array_indices, bubble_sort_times, label='BubbleSort', marker='D')

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
plt.plot(array_indices, bubble_sort_times, marker='o', label='BubbleSort Times')
plt.axhline(y=bubble_sort_avg, color='black', linestyle='--', label='Average')
plt.xlabel('Array Number')
plt.ylabel('Runtime (seconds)')
plt.title('BubbleSort Execution Times')
plt.legend()
plt.savefig('bubble_sort_times.png')
plt.show()
