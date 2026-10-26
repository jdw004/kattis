r, c = map(int, input().split())
grid = []
for _ in range(r):
    line = list(input())
    grid.append(line)

string = []
targetR, targetC = -1, -1
for r in range(len(grid[0])):
    if grid[r][0] != ".":
        targetR = r
        targetC = 0
        break
string.append(grid[targetR][targetC])


while True:
    if targetC == c:
        break

    print(targetR, targetC)

    if targetR+1 < r and grid[targetR+1][targetC+1] != '.':
        targetR += 1
    elif targetR-1 >= 0 and grid[targetR-1][targetC+1] != '.':
        targetR -= 1

    targetC += 1
    string.append(grid[targetR][targetC])

    
print("".join(string))
    

