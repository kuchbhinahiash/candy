"""
GB 5 - Real-time Event Processing using a QUEUE (FIFO)
  Add Event, Process Next Event, Display Pending, Cancel Event
"""


class EventQueue:
    def __init__(self):
        self.queue = []                 # front = index 0, rear = end

    def add_event(self, event):
        self.queue.append(event)        # enqueue at rear
        print(f"Event '{event}' added.")

    def process_next(self):
        if not self.queue:
            print("No events to process.")
            return
        event = self.queue.pop(0)       # dequeue from front (oldest)
        print(f"Processed event: '{event}'")

    def display_pending(self):
        if not self.queue:
            print("No pending events.")
            return
        print("Pending (front -> rear):")
        for i, e in enumerate(self.queue, 1):
            print(f"  {i}. {e}")

    def cancel_event(self, event):
        if event in self.queue:
            self.queue.remove(event)
            print(f"Event '{event}' cancelled.")
        else:
            print("Event not found (already processed or never added).")


def main():
    q = EventQueue()
    print("=== Event Processing System (Queue) ===")
    while True:
        print("\n--- MENU ---")
        print("1. Add event")
        print("2. Process next event")
        print("3. Display pending events")
        print("4. Cancel an event")
        print("0. Exit")
        ch = input("Choice: ")
        if ch == "1":
            q.add_event(input("Event name: "))
        elif ch == "2":
            q.process_next()
        elif ch == "3":
            q.display_pending()
        elif ch == "4":
            q.cancel_event(input("Event to cancel: "))
        elif ch == "0":
            break
    print("\nComplexity: add O(1); process O(n) with list.pop(0) "
          "(O(1) with collections.deque); display O(n); cancel O(n). Space O(n)")


if __name__ == "__main__":
    main()
