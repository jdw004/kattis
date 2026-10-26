n, s = map(int, input().split())

for _ in range(n):
    lower, upper = map(int, input().split())
    if s >= lower and s <= upper:
        s += 1
print(s)
    

