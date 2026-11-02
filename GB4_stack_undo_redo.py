"""
GB 4 - Undo/Redo system for a text editor using STACKS
  undo_stack : holds past changes
  redo_stack : holds undone changes
Each change = a piece of text appended to the document.
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

    def is_empty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []


class Editor:
    def __init__(self):
        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def document(self):
        return "".join(self.undo_stack.items)

    def make_change(self, text):
        self.undo_stack.push(text)
        self.redo_stack.clear()         # new change invalidates redo history
        print(f"Added: '{text}'")

    def undo(self):
        if self.undo_stack.is_empty():
            print("Nothing to undo.")
            return
        change = self.undo_stack.pop()
        self.redo_stack.push(change)    # store for potential redo
        print(f"Undid: '{change}'")

    def redo(self):
        if self.redo_stack.is_empty():
            print("Nothing to redo.")
            return
        change = self.redo_stack.pop()
        self.undo_stack.push(change)
        print(f"Redid: '{change}'")

    def display(self):
        print(f"Document State : '{self.document()}'")
        print(f"Undo stack     : {self.undo_stack.items}")
        print(f"Redo stack     : {self.redo_stack.items}")


def main():
    ed = Editor()
    print("=== Text Editor Undo/Redo (Stack) ===")
    while True:
        print("\n--- MENU ---")
        print("1. Make a change")
        print("2. Undo")
        print("3. Redo")
        print("4. Display document state")
        print("0. Exit")
        ch = input("Choice: ")
        if ch == "1":
            ed.make_change(input("Enter text to add: "))
        elif ch == "2":
            ed.undo()
        elif ch == "3":
            ed.redo()
        elif ch == "4":
            ed.display()
        elif ch == "0":
            break
    print("\nComplexity: push/pop/peek/undo/redo = O(1) each; Space O(n)")


if __name__ == "__main__":
    main()
