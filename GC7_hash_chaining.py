"""
GC 7 - Hash table of size 10, division method h(key) = key % 10,
collision handling by CHAINING (each slot holds a list of (key, value) pairs).
Operations: Insert, Search, Delete, Display
"""

SIZE = 10


class HashTableChaining:
    def __init__(self, size=SIZE):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return key % self.size            # division method

    def insert(self, key, value):
        idx = self.hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:                  # key exists -> update value
                self.table[idx][i] = (key, value)
                print(f"Key {key} updated at index {idx}.")
                return
        self.table[idx].append((key, value))
        print(f"Inserted ({key}, {value}) at index {idx}.")

    def search(self, key):
        idx = self.hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    def delete(self, key):
        idx = self.hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                del self.table[idx][i]
                print(f"Key {key} deleted from index {idx}.")
                return
        print("Key not found.")

    def display(self):
        for i in range(self.size):
            chain = " -> ".join(f"({k}:{v})" for k, v in self.table[i])
            print(f"[{i}] {chain if chain else 'empty'}")


def main():
    ht = HashTableChaining()
    print("=== Hash Table (Chaining, size 10, key % 10) ===")
    while True:
        print("\n--- MENU ---")
        print("1. Insert   2. Search   3. Delete   4. Display   0. Exit")
        ch = input("Choice: ")
        if ch == "1":
            ht.insert(int(input("Key (integer): ")), input("Value: "))
        elif ch == "2":
            r = ht.search(int(input("Key to search: ")))
            print(f"Value = {r}" if r is not None else "Key not found.")
        elif ch == "3":
            ht.delete(int(input("Key to delete: ")))
        elif ch == "4":
            ht.display()
        elif ch == "0":
            break
    print("\nComplexity: Insert/Search/Delete avg O(1), worst O(n) (all keys in one chain); "
          "Space O(n + m)")


if __name__ == "__main__":
    main()
