class Node:
    def __init__(self, book_title):
        self.book_title = book_title
        self.next = None
class BookStack:
    def __init__(self):
        self.top = None 
    def push(self, book_title):
        new_node = Node(book_title)
        new_node.next = self.top
        self.top = new_node
        print(f"Book '{book_title}' added to the stack.")
    def pop(self):
        if self.top is None:
            print("Stack is Empty! No book to remove.")
        else:
            removed_book = self.top.book_title
            self.top = self.top.next
            print(f"Book '{removed_book}' removed from the stack.")
    def peek(self):
        if self.top is None:
            print("Stack is Empty! No book on top.")
        else:
            print(f"Top book is: '{self.top.book_title}'")
    def display(self):
        if self.top is None:
            print("Stack is Empty!")
        else:
            temp = self.top
            print("Books in the stack (Top to Bottom):")
            while temp:
                print(f"'{temp.book_title}'", end=" -> ")
                temp = temp.next
            print("NULL")


stack = BookStack()

while True:
    print("\nBOOK STACK OPERATIONS")
    print("1. Add Book (Push)")
    print("2. Remove Book (Pop)")
    print("3. View Top Book (Peek)")
    print("4. Display All Books")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        title = input("Enter book title to add: ")
        stack.push(title)
    elif choice == '2':
        stack.pop()
    elif choice == '3':
        stack.peek()
    elif choice == '4':
        stack.display()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please select from 1 to 5.")

