from collections import deque
m, n = map(int, input().split())
grid = []

for i in range(m):
    grid.append([])
    line = input()
    for ch in line:
        grid[i].append(ch)

visited = set()
q = deque()

directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [1,1], [-1, 1], [1, -1]]

count = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == "#" and (i, j) not in visited:
            q.append((i, j))
            visited.add((i, j))
            count += 1
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    xr, xc = r+dr, c+dc
                    if (xr, xc) not in visited:
                        if 0 <= xr < m and 0 <= xc < n and grid[xr][xc] == "#":
                            visited.add((xr, xc))
                            q.append((xr, xc))
print(count)
