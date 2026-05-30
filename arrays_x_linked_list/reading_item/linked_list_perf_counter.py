# Linked List O(n)

import time

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(0)
current = head

for i in range(1, 10_000_000):
    current.next = Node(i)
    current = current.next

target_index = 9_000_000

start_time = time.perf_counter()

current = head

for _ in range(target_index):
    current = current.next

value = current.value

end_time = time.perf_counter()

print("Value Got From Linked List:", value)
print("Execution Time:", end_time - start_time)
