import time

def measure_time(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start


def linear_loop(n):
    total = 0
    for i in range(n):
        total += i
    return total


def quadratic_loop(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += i + j
    return total


def logarithmic_loop(n):
    total = 0
    i = 1
    while i < n:
        total += i
        i *= 2
    return total

n
n = 10**4  

print(f"Linear loop time for n={n}: {measure_time(linear_loop, n):.6f} seconds")
print(f"Quadratic loop time for n={n//10}: {measure_time(quadratic_loop, n//10):.6f} seconds")
print(f"Logarithmic loop time for n={n}: {measure_time(logarithmic_loop, n):.6f} seconds")