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

### 
#In this project, I built custom data structures to solve two different problems. The first one was an undo and redo system. A stack is the best choice for this because it works in a last in, first out way. This makes sense since the most recent action should be the first one undone. When a user does something, it gets added to the undo stack. When undo is pressed, that action is removed from the undo stack and added to the redo stack. If redo is pressed, it moves back to the undo stack. This keeps everything in the correct order.

The second part of the project was a help desk ticket system. For this, I used a queue. A queue works in a first in, first out order, which fits how a help desk should work. The first customer to ask for help should be helped first. New customers are added to the end of the line, and customers are removed from the front when they are helped. This makes the system fair and easy to manage.

These custom data structures are different from Python’s built in lists because they limit how data can be accessed. With lists, you can change or access any position, but stacks and queues only allow certain actions. This helps avoid mistakes and makes the code easier to understand. A real engineer might use a custom stack or queue for things like undo features, support systems, or managing tasks where order really matters.