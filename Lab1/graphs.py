import matplotlib.pyplot as plt

numbers = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
numbers2 = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42]

dp_runtimes = [0.000054, 0.000059, 0.000070, 0.000098, 0.000130, 0.000169, 0.000222, 0.000293, 0.000456, 0.000597, 0.000823, 0.001254, 0.001832, 0.002864, 0.004270, 0.007224]
matrinpow_runtimes = [0.000325, 0.000376, 0.000533, 0.000628, 0.000837, 0.001079, 0.001441, 0.001998, 0.002715, 0.003705, 0.005436, 0.007486, 0.010963, 0.016105, 0.024984, 0.038742]
binet_runtimes = [0.000051, 0.000020, 0.000021, 0.000020, 0.000024, 0.000024, 0.000028, 0.000040, 0.000057, 0.000078, 0.000102, 0.000142, 0.000192, 0.000267, 0.000399, 0.000606]
iterative_runtimes = [0.000028, 0.000035, 0.000044, 0.000057, 0.000073, 0.000096, 0.000127, 0.000175, 0.000235, 0.000337, 0.000452, 0.000652, 0.000925, 0.001352, 0.002086, 0.003185]
fastdoubling_runtimes = [0.000008, 0.000005, 0.000006, 0.000005, 0.000006, 0.000007, 0.000008, 0.000009, 0.000012, 0.000015, 0.000026, 0.000027, 0.000034, 0.000046, 0.000064, 0.000095]
recursion_runtimes = [0.000003, 0.000002, 0.000007, 0.000019, 0.000078, 0.000210, 0.000869, 0.002298, 0.009761, 0.025911, 0.118047, 0.288712, 1.189740, 3.173382, 13.610119, 36.428835]
backtracking_runtimes = [0.000005, 0.000001, 0.000001, 0.000001, 0.000001, 0.000001, 0.000001, 0.000001, 0.000002, 0.000004, 0.000005, 0.000004, 0.000005, 0.000004, 0.000006, 0.000005]

plt.figure(figsize=(10, 6))
plt.plot(numbers, iterative_runtimes, label='Iterative Approach', marker='o')
plt.xlabel('Input Number (n)')
plt.ylabel('Runtime (seconds)')
plt.title('Fibonacci Computation Time - Iterative Approach')
plt.xscale("log")
plt.savefig('iterative.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(numbers, iterative_runtimes, label='Fast Doubling', marker='o')
plt.xlabel('Input Number (n)')
plt.ylabel('Runtime (seconds)')
plt.title('Fibonacci Computation Time - Fast Doubling')
plt.xscale("log")
plt.savefig('fastdoubling.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(numbers2, iterative_runtimes, label='Backtracking', marker='o')
plt.xlabel('Input Number (n)')
plt.ylabel('Runtime (seconds)')
plt.title('Fibonacci Computation Time - Backtracking')
plt.xscale("log")
plt.savefig('backtracking.png')
plt.show()