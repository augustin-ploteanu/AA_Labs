from decimal import Decimal, Context, ROUND_HALF_EVEN
import time

def recursion(n):
    if n<=1:
        return n
    else:
        return recursion(n-1)+recursion(n-2)
    
def dp(n):
    arr=[0,1]
    for i in range(2, n+1):
        arr.append(arr[i-1]+arr[i-2])
    return arr[n]

def matrinpow(n):
    F=[[1,1],
       [1,0]]
    if(n==0):
        return 0
    power(F, n-1)

    return F[0][0]

def power(F, n):
    M=[[1,1],
       [1,0]]
    
    for i in range(2, n+1):
        multiply(F, M)

def multiply(F, M):
    x = (F[0][0]*M[0][0]+
         F[0][1]*M[1][0])
    y = (F[0][0]*M[0][1]+
         F[0][1]*M[1][1])
    z = (F[1][0]*M[0][0]+
         F[1][1]*M[1][0])
    w = (F[1][0]*M[0][1]+
         F[1][1]*M[1][1])
    
    F[0][0]=x
    F[0][1]=y
    F[1][0]=z
    F[1][1]=w

def binet(n):
    ctx=Context(prec=60, rounding=ROUND_HALF_EVEN)
    phi1=Decimal(1+Decimal(5**(1/2)))
    phi2=Decimal(1-Decimal(5**(1/2)))
    
    return int((ctx.power(phi1, Decimal(n))-ctx.power(phi2, Decimal(n)))/(2**n*Decimal(5**(1/2))))

###
###
###

def iterative(n):
    num1 = 0
    num2 = 1
    next_number = num2  
    i = 1

    while i <= n:
        i += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
    
    return next_number

def backtracking(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = backtracking(n-1) + backtracking(n-2)
        return memo[n]

def fastdoubling(n):
	if n == 0:
		return (0, 1)
	else:
		a, b = fastdoubling(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)

numbers2 = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42]
numbers = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

def measure_runtime(func, n):
    start_time = time.time()
    func(n)
    end_time = time.time()
    return end_time - start_time

recursion_runtimes = []
dp_runtimes = []
matrinpow_runtimes = []
binet_runtimes = []
iterative_runtimes = []
backtracking_runtimes = []
fastdoubling_runtimes = []



for num in numbers:
    dp_runtimes.append(measure_runtime(dp, num))
    matrinpow_runtimes.append(measure_runtime(matrinpow, num))
    binet_runtimes.append(measure_runtime(binet, num))
    iterative_runtimes.append(measure_runtime(iterative, num))
    fastdoubling_runtimes.append(measure_runtime(fastdoubling, num))

for num in numbers2:
    recursion_runtimes.append(measure_runtime(recursion, num))
    backtracking_runtimes.append(measure_runtime(backtracking, num))

print(" ", end=" ")
for num in numbers:
    print(f"{num:>8}", end=" ")
print()

runtimes = [dp_runtimes, matrinpow_runtimes, binet_runtimes, iterative_runtimes, fastdoubling_runtimes]

for i, runtime in enumerate(runtimes):
    print(f"{i:<2}", end=" ")
    for time in runtime:
        print(f"{time:>8.6f}", end=" ")
    print()

print(" ", end=" ")
for num in numbers2:
    print(f"{num:>8}", end=" ")
print()

runtimes2 = [recursion_runtimes, backtracking_runtimes]

for i, runtime in enumerate(runtimes):
    print(f"{i+5:<2}", end=" ") 
    for time in runtime:
        print(f"{time:>8.6f}", end=" ")
    print()