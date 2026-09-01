n, k = map(int, input().split())

mySet = set()

for _ in range(n):
    y = int(input())
    mySet.add(y)

print(min(len(mySet), k))

