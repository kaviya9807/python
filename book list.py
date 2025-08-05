stack = []
MAX = 5 
def push():
    if len(stack) == MAX:
        print("Book stack is full!")
    else:
        book = input("Enter the book title to add: ")
        stack.append(book)
        print(f"'{book}' has been added to the stack.")
def pop():
    if not stack:
        print("Book stack is empty!")
    else:
        book = stack.pop()
        print(f"'{book}' has been removed from the stack.")
def peek():
    if not stack:
        print("Book stack is empty!")
    else:
        print("Top book in the stack:", stack[-1])
def display():
    if not stack:
        print("Book stack is empty!")
    else:
        print("Books in stack (top to bottom):")
        for book in reversed(stack):
            print(book)
while True:
    print("\n------ Book Stack Menu ------")
    print("1. Add Book (Push)")
    print("2. Remove Book (Pop)")
    print("3. View Top Book (Peek)")
    print("4. Display All Books")
    print("5. Exit")
    choice = int(input("Enter your choice (1-5): "))
    
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Exiting Book Stack Program...")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")

