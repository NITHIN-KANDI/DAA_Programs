import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]


def measure_bubble_sort(arr):
    start_time = time.time()
    bubble_sort(arr)
    end_time = time.time()
    return (end_time - start_time) * 1000  


def measure_builtin_sort(arr):
    start_time = time.time()
    arr.sort()
    end_time = time.time()
    return (end_time - start_time) * 1000 


array_sizes = [100, 1000, 10000]

for size in array_sizes:
    arr = generate_random_array(size)
    
    print(f"Array size: {size}")
    
    bubble_time = measure_bubble_sort(arr.copy())
    print(f"Time taken for Bubble Sort: {bubble_time:.6f} milliseconds")

    builtin_sort_time = measure_builtin_sort(arr.copy())
    print(f"Time taken for array.sort(): {builtin_sort_time:.6f} milliseconds")

    print()
