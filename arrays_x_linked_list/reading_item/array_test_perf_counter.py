# Array O(1)
import time

numbers = list(range(10_000_000))

target_index = 9_000_000

start_time = time.perf_counter()

value = numbers[target_index]

end_time = time.perf_counter()

print("Value Got From Array:", value)
print("Execution Time:", end_time - start_time)
