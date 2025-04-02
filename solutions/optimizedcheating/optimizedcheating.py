from collections import deque

n, m, k = map(int, input().split())

memory = set()

for i in range(n):
    if i == k - 1:
        bobMem = int(input())
    else:
        memory.add(int(input()))

operations = []
for _ in range(m):
    x, y = input().split()
    y = int(y)
    operations.append([x, y])

if bobMem not in memory:
    print(0)
    exit()

def operate(val, op, opVal):
    if op == "-":
        return val - opVal
    elif op == "+":
        return val + opVal
    elif op == "/":
        return val // opVal
    else:
        return val * opVal

queue = deque()
previousOp = dict()  
queue.append(bobMem)
found = False

while queue:
    for _ in range(len(queue)):
        current = queue.popleft()
        for i in range(len(operations)):
            newest = operate(current, operations[i][0], operations[i][1])
            if newest < 0:
                continue
            if newest not in previousOp:
                queue.append(newest)
                previousOp[newest] = [i + 1, current]
            if newest not in memory:
                result = newest
                found = True
                break
        if found:
            break
    if found:
        break
else:
    print(-1)
    exit()

#print(result)

count = 0
ans = []
cur = result  
while cur != bobMem:
    count += 1
    ans.append(previousOp[cur][0])
    cur = previousOp[cur][1]

print(count)
for x in reversed(ans):
    print(x)
