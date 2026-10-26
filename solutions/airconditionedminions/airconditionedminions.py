n = int(input())
temps = []
for _ in range(n):
    l, u = map(int, input().split())
    temps.append((l, u))

if not temps:
    print(0)
    exit()

temps.sort(key = lambda x: (x[1], x[0]))
currMax = temps[0][1]
rooms = 1

for i in range(len(temps)):
    if i == 0:
        continue
    if temps[i][0] > currMax:
        rooms += 1
        currMax = temps[i][1]
print(rooms)

    