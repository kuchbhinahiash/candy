"""
GA 3 - Sort employee salaries (floats) using Selection Sort and Bubble Sort,
then display the top 5 highest salaries.
"""

salaries = [45000.50, 32000.75, 78000.00, 56000.25, 91000.10,
            23000.00, 67000.80, 88000.45, 41000.30]


def selection_sort(arr):
    a = arr[:]                          # work on a copy
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:                 # already sorted -> stop early
            break
    return a


def top_five(sorted_asc):
    top = sorted_asc[-5:]               # last 5 of ascending list
    top.reverse()                       # highest first
    return top


def main():
    global salaries
    print("=== Employee Salary Sorting ===")
    if input("Use sample data? (y/n): ").lower() == "n":
        n = int(input("How many salaries? "))
        salaries = [float(input(f"  Salary {i+1}: ")) for i in range(n)]
    print("Original:", salaries)

    s = selection_sort(salaries)
    print("\nSelection Sort (ascending):", s)
    print("  Time: O(n^2) in all cases   Space: O(1)")

    b = bubble_sort(salaries)
    print("\nBubble Sort (ascending):", b)
    print("  Time: O(n^2) worst/avg, O(n) best (optimized)   Space: O(1)")

    print("\nTop 5 highest salaries:")
    for rank, sal in enumerate(top_five(b), 1):
        print(f"  {rank}. {sal:.2f}")


if __name__ == "__main__":
    main()
