"""
GA 2 - Linear Search & Binary Search on customer account IDs
  Linear Search : works on any list            -> O(n)
  Binary Search : needs a SORTED list          -> O(log n)
"""

account_ids = [1005, 1020, 1003, 1099, 1050, 1012, 1076, 1001]


def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i              # index where found
    return -1


def binary_search(arr, key):      # iterative; arr must be sorted
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def binary_search_recursive(arr, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    if key < arr[mid]:
        return binary_search_recursive(arr, key, low, mid - 1)
    return binary_search_recursive(arr, key, mid + 1, high)


def main():
    global account_ids
    print("=== Customer Account ID Search ===")
    print("Account IDs:", account_ids)
    while True:
        print("\n--- MENU ---")
        print("1. Add account ID")
        print("2. Linear Search")
        print("3. Binary Search (iterative)")
        print("4. Binary Search (recursive)")
        print("5. Display list")
        print("0. Exit")
        ch = input("Choice: ")

        if ch == "1":
            account_ids.append(int(input("Enter new ID: ")))
        elif ch == "2":
            key = int(input("ID to search: "))
            pos = linear_search(account_ids, key)
            print(f"Found at index {pos}" if pos != -1 else "ID NOT found")
            print("Time: O(n) (best O(1))   Space: O(1)")
        elif ch in ("3", "4"):
            key = int(input("ID to search: "))
            sorted_ids = sorted(account_ids)     # binary search needs sorted data
            print("Sorted list:", sorted_ids)
            if ch == "3":
                pos = binary_search(sorted_ids, key)
                print("Space: O(1)")
            else:
                pos = binary_search_recursive(sorted_ids, key, 0, len(sorted_ids) - 1)
                print("Space: O(log n) (recursion stack)")
            print(f"Found at index {pos} of sorted list" if pos != -1 else "ID NOT found")
            print("Time: O(log n) (best O(1))")
        elif ch == "5":
            print(account_ids)
        elif ch == "0":
            break


if __name__ == "__main__":
    main()
