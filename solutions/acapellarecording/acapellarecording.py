n, d = map(int, input().split())

notes = []

for _ in range(n):
    notes.append(int(input()))

notes.sort()

ans = 1
start = notes[0]

for i in range(1, n):
    if notes[i] - start > d:
        ans += 1
        start = notes[i]

print(ans)