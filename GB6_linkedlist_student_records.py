"""
GB 6 - Student Record Management System using a SINGLY LINKED LIST
Student = (Roll No, Name, Marks)
Operations: Add, Delete, Update, Search, Sort, Display (asc/desc by marks or roll no)
"""


class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    # ---- Add (at end) ----
    def add(self, roll, name, marks):
        if self.search(roll):
            print("Roll number already exists!")
            return
        new = Node(roll, name, marks)
        if self.head is None:
            self.head = new
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new
        print("Student added.")

    # ---- Delete by roll ----
    def delete(self, roll):
        cur, prev = self.head, None
        while cur and cur.roll != roll:
            prev = cur
            cur = cur.next
        if cur is None:
            print("Student not found.")
            return
        if prev is None:
            self.head = cur.next
        else:
            prev.next = cur.next
        print("Student deleted.")

    # ---- Update ----
    def update(self, roll, name, marks):
        node = self.search(roll)
        if node is None:
            print("Student not found.")
            return
        node.name, node.marks = name, marks
        print("Record updated.")

    # ---- Search ----
    def search(self, roll):
        cur = self.head
        while cur:
            if cur.roll == roll:
                return cur
            cur = cur.next
        return None

    # ---- Sort (bubble sort swapping node data) ----
    def sort(self, by="marks", ascending=True):
        if self.head is None:
            return
        swapped = True
        while swapped:
            swapped = False
            cur = self.head
            while cur.next:
                a = getattr(cur, by)
                b = getattr(cur.next, by)
                if (a > b) if ascending else (a < b):
                    cur.roll, cur.next.roll = cur.next.roll, cur.roll
                    cur.name, cur.next.name = cur.next.name, cur.name
                    cur.marks, cur.next.marks = cur.next.marks, cur.marks
                    swapped = True
                cur = cur.next

    # ---- Display ----
    def display(self):
        if self.head is None:
            print("No records.")
            return
        print(f"{'Roll':<8}{'Name':<15}{'Marks':<8}")
        print("-" * 31)
        cur = self.head
        while cur:
            print(f"{cur.roll:<8}{cur.name:<15}{cur.marks:<8}")
            cur = cur.next


def main():
    sl = StudentList()
    # sample data
    for r, n, m in [(3, "Amit", 78), (1, "Riya", 92), (2, "Sam", 65), (4, "Neha", 85)]:
        sl.add(r, n, m)
    print("\n=== Student Record Management (Linked List) ===")
    while True:
        print("\n--- MENU ---")
        print("1. Add   2. Delete   3. Update   4. Search")
        print("5. Sort by Marks (asc)    6. Sort by Marks (desc)")
        print("7. Sort by Roll No (asc)  8. Sort by Roll No (desc)")
        print("9. Display   0. Exit")
        ch = input("Choice: ")
        if ch == "1":
            sl.add(int(input("Roll: ")), input("Name: "), float(input("Marks: ")))
        elif ch == "2":
            sl.delete(int(input("Roll to delete: ")))
        elif ch == "3":
            sl.update(int(input("Roll to update: ")), input("New name: "),
                      float(input("New marks: ")))
        elif ch == "4":
            n = sl.search(int(input("Roll to search: ")))
            print(f"Found: {n.roll}, {n.name}, {n.marks}" if n else "Not found.")
        elif ch == "5":
            sl.sort("marks", True); sl.display()
        elif ch == "6":
            sl.sort("marks", False); sl.display()
        elif ch == "7":
            sl.sort("roll", True); sl.display()
        elif ch == "8":
            sl.sort("roll", False); sl.display()
        elif ch == "9":
            sl.display()
        elif ch == "0":
            break
    print("\nComplexity: Add O(n) (O(1) if head insert); Delete/Update/Search O(n); "
          "Sort O(n^2); Display O(n); Space O(1) extra")


if __name__ == "__main__":
    main()
