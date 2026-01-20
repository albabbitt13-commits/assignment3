from node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        removed_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed_value

    def peek(self):
        if self.front is None:
            return None
        return self.front.value

    def print_queue(self):
        if self.front is None:
            print("Queue is empty")
            return
        current = self.front
        while current:
            print(f"- {current.value}")
            current = current.next


def help_desk_manager():
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            queue.enqueue(name)
            print(f"{name} added to the queue.")

        elif choice == "2":
            customer = queue.dequeue()
            if customer is None:
                print("No customers to help")
            else:
                print(f"Helped: {customer}")

        elif choice == "3":
            customer = queue.peek()
            if customer is None:
                print("No customers waiting")
            else:
                print(f"Next customer: {customer}")

        elif choice == "4":
            print("Waiting customers:")
            queue.print_queue()

        elif choice == "5":
            break
help_desk_manager()
