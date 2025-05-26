def recursive_log(n):
    if n <= 1:
        return 1
    else:
        # Recursive call with n divided by 2
        return recursive_log(n // 2)

import time

# Measure the time taken for a large n
n = 10**8

start_time = time.time()
recursive_log(n)
end_time = time.time()

print(f"Time taken for recursive_log({n}): {end_time - start_time:.6f} seconds")
