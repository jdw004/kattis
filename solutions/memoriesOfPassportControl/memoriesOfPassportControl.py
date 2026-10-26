k, s = map(int, (input().split()))
stamped = 0
ans = 0

while stamped < s:
    if stamped + k <= s:
        stamped += k
    else:
        stamped += 1
    ans += 1
print(ans)