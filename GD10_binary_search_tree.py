"""
GD 10 - Binary Search Tree
Operations: Insert, Delete, Display (Inorder / Preorder / Postorder), Search
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # ---- Insert ----
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            print("Duplicate key ignored.")
        return node

    # ---- Search ----
    def search(self, key):
        cur = self.root
        while cur:
            if key == cur.key:
                return True
            cur = cur.left if key < cur.key else cur.right
        return False

    # ---- Delete ----
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            print("Key not found.")
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Case 1 & 2: zero or one child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Case 3: two children -> replace with inorder successor
            succ = node.right
            while succ.left:
                succ = succ.left
            node.key = succ.key
            node.right = self._delete(node.right, succ.key)
        return node

    # ---- Traversals ----
    def inorder(self, node, out):
        if node:
            self.inorder(node.left, out)
            out.append(node.key)
            self.inorder(node.right, out)
        return out

    def preorder(self, node, out):
        if node:
            out.append(node.key)
            self.preorder(node.left, out)
            self.preorder(node.right, out)
        return out

    def postorder(self, node, out):
        if node:
            self.postorder(node.left, out)
            self.postorder(node.right, out)
            out.append(node.key)
        return out

    # ---- Sideways tree picture ----
    def show_tree(self, node, level=0):
        if node:
            self.show_tree(node.right, level + 1)
            print("     " * level + str(node.key))
            self.show_tree(node.left, level + 1)

    def display(self):
        if self.root is None:
            print("Tree is empty.")
            return
        print("Inorder   :", self.inorder(self.root, []))
        print("Preorder  :", self.preorder(self.root, []))
        print("Postorder :", self.postorder(self.root, []))
        print("\nTree (rotated, root at left):")
        self.show_tree(self.root)


def main():
    t = BST()
    for k in [50, 30, 70, 20, 40, 60, 80]:   # sample data
        t.insert(k)
    print("=== Binary Search Tree ===")
    print("(Sample tree loaded: 50 30 70 20 40 60 80)")
    while True:
        print("\n--- MENU ---")
        print("1. Insert   2. Delete   3. Search   4. Display   0. Exit")
        ch = input("Choice: ")
        if ch == "1":
            t.insert(int(input("Key: ")))
        elif ch == "2":
            t.delete(int(input("Key to delete: ")))
        elif ch == "3":
            print("Found!" if t.search(int(input("Key to search: "))) else "Not found.")
        elif ch == "4":
            t.display()
        elif ch == "0":
            break
    print("\nComplexity: Insert/Search/Delete avg O(log n), worst O(n) (skewed tree); "
          "Traversal O(n); Space O(h) recursion (h = height)")


if __name__ == "__main__":
    main()
