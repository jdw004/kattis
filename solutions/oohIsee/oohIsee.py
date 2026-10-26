r, c = map(int, input().split())
grid = []

for _ in range(r):
    line = list(input())
    grid.append(line)

zeros = []

def search(row, column):
    directions = [-1, -1], [-1, 0], [-1, 1], [0, 1], [0, -1], [1, -1], [1, 0], [1, 1]
    count = 0
    for dr, dc in directions:
        nr, nc = row+dr, column+dc
        if nr < 0 or nc < 0 or nr >= r or nc >= c:
            continue

        if grid[nr][nc] != "O":
            break
        count += 1

    if count == 8:
        zeros.append((row+1, column+1))

for row in range(r):
    for col in range(c):
        if grid[row][col] == '0':
            search(row, col)

if not zeros:
    print("Oh no!")
elif len(zeros) >= 2:
    print(f"Oh no! {len(zeros)} locations")
else:
    x, y = zeros[0]
    print(x, y)
