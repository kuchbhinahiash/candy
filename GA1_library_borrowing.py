"""
GA 1 - Library Borrowing Records
Operations:
  1. Average number of books borrowed by all members
  2. Book with highest and lowest number of borrowings
  3. Count of members who borrowed 0 books
  4. Most frequently borrowed book count (MODE of borrow counts)
Each operation prints its Time and Space complexity.
"""

# ---------- Sample data ----------
members = {"Amit": 3, "Riya": 0, "Sam": 5, "Neha": 3, "John": 0, "Priya": 2, "Karan": 3}
books = {"Python Basics": 12, "Data Structures": 25, "Algorithms": 25,
         "DBMS": 7, "Networks": 3, "OS Concepts": 9}


# ---------- Operation 1: Average ----------
def average_borrowed(member_data):
    total = 0
    for name in member_data:          # loop through every member
        total += member_data[name]
    return total / len(member_data)


# ---------- Operation 2: Highest and lowest borrowed book ----------
def highest_lowest(book_data):
    names = list(book_data.keys())
    high = low = names[0]
    for b in names:
        if book_data[b] > book_data[high]:
            high = b
        if book_data[b] < book_data[low]:
            low = b
    return high, low


# ---------- Operation 3: Members with zero borrows ----------
def count_zero(member_data):
    count = 0
    for name in member_data:
        if member_data[name] == 0:
            count += 1
    return count


# ---------- Operation 4: Mode of borrow counts ----------
def mode_of_counts(member_data):
    freq = {}                         # borrow count -> how many members have it
    for name in member_data:
        c = member_data[name]
        freq[c] = freq.get(c, 0) + 1
    best = None
    for c in freq:
        if best is None or freq[c] > freq[best]:
            best = c
    return best, freq[best]


def most_borrowed_book(book_data):
    high, _ = highest_lowest(book_data)
    return high, book_data[high]


def read_data():
    m, b = {}, {}
    n = int(input("Number of members: "))
    for i in range(n):
        name = input(f"  Member {i+1} name: ")
        m[name] = int(input(f"  Books borrowed by {name}: "))
    n = int(input("Number of books: "))
    for i in range(n):
        title = input(f"  Book {i+1} title: ")
        b[title] = int(input(f"  Times '{title}' was borrowed: "))
    return m, b


def main():
    global members, books
    print("=== Library Borrowing Records ===")
    if input("Use sample data? (y/n): ").lower() == "n":
        members, books = read_data()
    print("\nMembers :", members)
    print("Books   :", books)

    while True:
        print("\n--- MENU ---")
        print("1. Average books borrowed per member")
        print("2. Highest & lowest borrowed book")
        print("3. Members who borrowed no books")
        print("4. Most frequently borrowed (mode of borrow counts)")
        print("5. Run ALL operations")
        print("0. Exit")
        ch = input("Choice: ")

        if ch in ("1", "5"):
            print("\n[1] Average borrowed =", round(average_borrowed(members), 2))
            print("    Time: O(n)   Space: O(1)")
        if ch in ("2", "5"):
            h, l = highest_lowest(books)
            print(f"\n[2] Highest: {h} ({books[h]})   Lowest: {l} ({books[l]})")
            print("    Time: O(n)   Space: O(1)")
        if ch in ("3", "5"):
            print("\n[3] Members with 0 borrows =", count_zero(members))
            print("    Time: O(n)   Space: O(1)")
        if ch in ("4", "5"):
            val, times = mode_of_counts(members)
            print(f"\n[4] Mode of borrow counts = {val} (shared by {times} members)")
            bk, cnt = most_borrowed_book(books)
            print(f"    Most frequently borrowed book = {bk} ({cnt} times)")
            print("    Time: O(n)   Space: O(k) where k = distinct borrow counts (worst O(n))")
        if ch == "0":
            break


if __name__ == "__main__":
    main()
