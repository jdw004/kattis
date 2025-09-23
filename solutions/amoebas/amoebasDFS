from itertools import product

m, n = map(int, input().split())
graph = [list(input()) for _ in range(m)]


visited = set()
neighbors = list(product([-1,0,1], repeat=2))

def dfs(i, j):
    if (i, j) in visited:
        return 0

    visited.add((i, j))
    
    if graph[i][j] == ".":
        return 0

    for dx, dy in neighbors:
        xx, xy = i+dx, j+dy
        if 0<=xx<m and 0<=xy<n:
            dfs(xx, xy)
    return 1

print(graph)
count = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == "#" and (i, j) not in visited:
            count += dfs(i, j)
print(count)
    
