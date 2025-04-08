def find(x):
    if items[x] == x:
        return x
    items[x] = find(items[x])  
    return items[x]

def union(x, y):
    items[find(x)] = find(y)

islands, bridges = map(int, input().split())
items = [i for i in range(islands + 1)]  

for _ in range(bridges):
    island, bridge = map(int, input().split())
    if 1 <= island <= islands and 1 <= bridge <= islands: 
        union(island, bridge)

main = find(1)  
for i in range(1, islands + 1):
    if find(i) != main:  
        print("NO")
        exit()
print("YES")
