from collections import deque
n, _ = map(int, input().split())

commands = input().split()
i = 0
stack = []

while i < len(commands):
    if commands[i] == "undo":
        toUndo = int(commands[i+1])
        for _ in range(toUndo):
            stack.pop()
        i += 2
    else:
        stack.append(int(commands[i]))
        i += 1
pos = 0
for x in stack:
    pos += x
print(pos % n)
