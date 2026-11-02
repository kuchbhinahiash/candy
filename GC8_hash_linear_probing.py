"""
GC 8 - Fixed-size hash table, division method h(key) = key % size,
collisions resolved by LINEAR PROBING.
Operations: Insert, Search, Delete, Display
Deleted slots are marked DELETED (tombstone) so searches keep working.
"""

EMPTY = None
DELETED = "DELETED"


class HashTableLinearProbing:
    def __init__(self, size=10):
        self.size = size
        self.table = [EMPTY] * size

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        if self.search(key) != -1:
            print("Key already present.")
            return
        idx = self.hash(key)
        for i in range(self.size):
            pos = (idx + i) % self.size       # linear probe
            if self.table[pos] is EMPTY or self.table[pos] == DELETED:
                self.table[pos] = key
                if i > 0:
                    print(f"Collision! Inserted {key} at index {pos} after {i} probe(s).")
                else:
                    print(f"Inserted {key} at index {pos}.")
                return
        print("Table is FULL. Cannot insert.")

    def search(self, key):
        idx = self.hash(key)
        for i in range(self.size):
            pos = (idx + i) % self.size
            if self.table[pos] is EMPTY:      # never used -> key can't be further
                return -1
            if self.table[pos] == key:
                return pos
        return -1

    def delete(self, key):
        pos = self.search(key)
        if pos == -1:
            print("Key not found.")
        else:
            self.table[pos] = DELETED
            print(f"Key {key} deleted from index {pos}.")

    def display(self):
        for i, v in enumerate(self.table):
            print(f"[{i}] {'empty' if v is EMPTY else v}")


def main():
    size = int(input("Enter hash table size (e.g. 10): "))
    ht = HashTableLinearProbing(size)
    print(f"=== Hash Table (Linear Probing, size {size}) ===")
    while True:
        print("\n--- MENU ---")
        print("1. Insert   2. Search   3. Delete   4. Display   0. Exit")
        ch = input("Choice: ")
        if ch == "1":
            ht.insert(int(input("Key: ")))
        elif ch == "2":
            p = ht.search(int(input("Key to search: ")))
            print(f"Found at index {p}" if p != -1 else "Key not found.")
        elif ch == "3":
            ht.delete(int(input("Key to delete: ")))
        elif ch == "4":
            ht.display()
        elif ch == "0":
            break
    print("\nComplexity: Insert/Search/Delete avg O(1), worst O(n) (clustering); Space O(m)")


if __name__ == "__main__":
    main()
