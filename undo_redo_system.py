from node import Node

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        removed_value = self.top.value
        self.top = self.top.next
        return removed_value

    def peek(self):
        if self.top is None:
            return None
        return self.top.value

    def print_stack(self):
        if self.top is None:
            print("Stack is empty")
            return
        current = self.top
        while current:
            print(f"- {current.value}")
            current = current.next


def undo_redo_manager():
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action: ")
            undo_stack.push(action)
            redo_stack = Stack()
            print(f"Action performed: {action}")

        elif choice == "2":
            action = undo_stack.pop()
            if action is None:
                print("No actions to undo")
            else:
                redo_stack.push(action)
                print(f"Undid action: {action}")

        elif choice == "3":
            action = redo_stack.pop()
            if action is None:
                print("No actions to redo")
            else:
                undo_stack.push(action)
                print(f"Redid action: {action}")

        elif choice == "4":
            print("Undo Stack:")
            undo_stack.print_stack()

        elif choice == "5":
            print("Redo Stack:")
            redo_stack.print_stack()

        elif choice == "6":
            break
undo_redo_manager()