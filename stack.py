stack = []

stack.append(1)
stack.append(2)
stack.append(3)   # Let's add one more for better demonstration

print("Stack after pushing:", stack)   # [1, 2, 3]

print("Popped element:", stack.pop())   # Output: 3
print("Popped element:", stack.pop())   # Output: 2

print("Stack after popping:", stack)    # [1]