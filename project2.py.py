# Stack Implementation for MoMo
stack = []
# Push operations
stack.append("PIN")
stack.append("Service")
stack.append("Confirm")

print("Stack after pushes:", stack)

# Undo one (pop)
stack.pop()

print("Stack after undo:", stack)
# Stack Implementation for UR
stack = []
stack.append("Assignment1")
stack.append("Assignment2")
stack.append("Assignment3")

print("Stack after pushes:", stack)

# Undo all (pop until empty)
while stack:
    stack.pop()

print("Stack after undo all:", stack)
word = "LIFOSTACK"
stack = []

# Step 1 & 2: Push each character
for ch in word:
    stack.append(ch)

# Step 3: Pop all to reverse
reversed_word = ""
while stack:
    reversed_word += stack.pop()

print("Original:", word)
print("Reversed:", reversed_word)
from collections import deque

queue = deque(["C1", "C2", "C3", "C4", "C5", "C6", "C7"])
print("Initial queue:", list(queue))

# Serve 2
queue.popleft()
queue.popleft()

print("Queue after serving 2:", list(queue))
print("Front client now:", queue[0])
queue = ["C1", "C2", "C3", "C4", "C5", "C6"]
print("Queue:", queue)
print("Last served client:", queue[-1])
from collections import deque

# Pensioners arriving in order
queue = deque(["P1", "P2", "P3"])

# Serve in FIFO
served_order = []
while queue:
    served_order.append(queue.popleft())

print("Order of service:", served_order)
