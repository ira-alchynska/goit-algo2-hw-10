import random
import time
import sys
import matplotlib.pyplot as plt

# Increase recursion limit for large arrays
sys.setrecursionlimit(1000000)

# Deterministic QuickSort (pivot = middle element)
def deterministic_quick_sort(arr):
    a = arr.copy()
    def partition(a, low, high, pivot_index):
        pivot = a[pivot_index]
        a[pivot_index], a[high] = a[high], a[pivot_index]
        store = low
        for i in range(low, high):
            if a[i] < pivot:
                a[i], a[store] = a[store], a[i]
                store += 1
        a[store], a[high] = a[high], a[store]
        return store
    def _qs(a, low, high):
        if low < high:
            pivot_index = (low + high) // 2
            pivot_new = partition(a, low, high, pivot_index)
            _qs(a, low, pivot_new - 1)
            _qs(a, pivot_new + 1, high)
    _qs(a, 0, len(a) - 1)
    return a

# Randomized QuickSort (pivot random)
def randomized_quick_sort(arr):
    a = arr.copy()
    def partition(a, low, high, pivot_index):
        pivot = a[pivot_index]
        a[pivot_index], a[high] = a[high], a[pivot_index]
        store = low
        for i in range(low, high):
            if a[i] < pivot:
                a[i], a[store] = a[store], a[i]
                store += 1
        a[store], a[high] = a[high], a[store]
        return store
    def _qs(a, low, high):
        if low < high:
            pivot_index = random.randint(low, high)
            pivot_new = partition(a, low, high, pivot_index)
            _qs(a, low, pivot_new - 1)
            _qs(a, pivot_new + 1, high)
    _qs(a, 0, len(a) - 1)
    return a

# Benchmark function
def benchmark():
    sizes = [10_000, 50_000, 100_000, 500_000]
    repeats = 5
    results = []

    for n in sizes:
        rnd_times = []
        det_times = []
        for _ in range(repeats):
            arr = [random.randint(0, 1_000_000) for _ in range(n)]
            start = time.time()
            randomized_quick_sort(arr)
            rnd_times.append(time.time() - start)
            start = time.time()
            deterministic_quick_sort(arr)
            det_times.append(time.time() - start)
        rnd_avg = sum(rnd_times) / repeats
        det_avg = sum(det_times) / repeats
        results.append((n, rnd_avg, det_avg))

    # Print results table
    print(f"{'Size':>10} | {'Randomized (s)':>15} | {'Deterministic (s)':>17}")
    print("-" * 50)
    for n, rnd_avg, det_avg in results:
        print(f"{n:>10} | {rnd_avg:>15.4f} | {det_avg:>17.4f}")

    # Plotting
    sizes = [r[0] for r in results]
    rnd_avgs = [r[1] for r in results]
    det_avgs = [r[2] for r in results]

    plt.figure()
    plt.plot(sizes, rnd_avgs, label='Randomized QS')
    plt.plot(sizes, det_avgs, label='Deterministic QS')
    plt.xlabel('Array Size')
    plt.ylabel('Average Time (sec)')
    plt.title('QuickSort: Randomized vs Deterministic')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    benchmark()
