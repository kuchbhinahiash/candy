print("Linear Search")

key = int(input("Enter ID to search: "))
customer_id = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]

found = False

for i in range(len(customer_id)):
    if customer_id[i] == key:
        print("Position of ID is:", i)
        found = True
        break

if not found:
    print("ID not found")

print("Binary Search")

found = False
low = 0
high = len(customer_id) - 1

while low <= high:
    mid = (low + high) // 2

    if customer_id[mid] == key:
        print("Position of ID is:", mid)
        found = True
        break
    elif customer_id[mid] > key:
        high = mid - 1
    else:
        low = mid + 1

if not found:
    print("ID not found")
