import sys
import time
import random
import matplotlib.pyplot as plt

sys.setrecursionlimit(100000)


def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def quicksort(arr):
    a = arr.copy()
    _quicksort(a, 0, len(a) - 1)
    return a


def _quicksort(a, low, high):
    while low < high:
        p = _partition(a, low, high)
        if p - low < high - p:
            _quicksort(a, low, p - 1)
            low = p + 1
        else:
            _quicksort(a, p + 1, high)
            high = p - 1


def _partition(a, low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


def generate_data(kind, n):
    if kind == "random":
        return [random.randint(0, 10**6) for _ in range(n)]
    if kind == "sorted":
        return list(range(n))
    if kind == "reversed":
        return list(range(n, 0, -1))
    raise ValueError(kind)


def measure(func, data):
    start = time.perf_counter()
    func(data)
    return time.perf_counter() - start


def run_experiment():
    sizes = [100, 200, 400, 600, 800, 1000, 1500, 2000]

    kinds = {
        "random":   "Random data",
        "sorted":   "Sorted data",
        "reversed": "Reversed data",
    }

    for kind, title in kinds.items():
        sel_times = []
        qs_times = []

        print(f"\n=== {title} ===")
        print(f"{'n':>6} | {'selection, s':>14} | {'quicksort, s':>14}")
        print("-" * 42)

        for n in sizes:
            data = generate_data(kind, n)

            t_sel = measure(selection_sort, data)
            t_qs = measure(quicksort, data)

            sel_times.append(t_sel)
            qs_times.append(t_qs)

            print(f"{n:>6} | {t_sel:>14.6f} | {t_qs:>14.6f}")

        plt.figure(figsize=(8, 5))
        plt.plot(sizes, sel_times, marker='o', label='Selection sort')
        plt.plot(sizes, qs_times, marker='s', label='Quicksort')
        plt.xlabel('Array size n')
        plt.ylabel('Time, s')
        plt.title(f'Time vs size: {title}')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        filename = f'graph_{kind}.png'
        plt.savefig(filename, dpi=150)
        plt.close()
        print(f"  -> saved {filename}")


if __name__ == "__main__":
    run_experiment()