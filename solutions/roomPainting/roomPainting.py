n, m = map(int, input().split())
canSizes, need = [], []

for _ in range(n):
    canSizes.append(int(input()))

for _ in range(m):
    need.append(int(input()))

wasted = 0
canSizes.sort()

for n in need:
    l, r = 0, len(canSizes)-1
    while l < r:
        m = (l+r)//2

        if canSizes[m] < n:
            l = m + 1
        else:
            r = m 
    wasted += canSizes[r]-n
print(wasted)


