import sys
from functools import cache

n, c = map(int, input().split())
softness = [*map(int, input().split())]

sys.setrecursionlimit(10**4)

@cache
def dp(i, sum, taken):
    if sum == c:
        return "YES"
    
    if i >= len(softness) or sum > c:
        return "NO"

    # take
    thisPillow = -(softness[i] // -(2 ** (taken - 1)))    
    comfort = sum + thisPillow

    if thisPillow == 1:
        if c > sum:
            return "YES"
    else:
        reset = dp(0, comfort, taken+1)
        goforward = dp(i+1, sum, taken)
        if goforward == "YES" or reset == "YES":
            return "YES"
    return "NO"
    
ans = dp(0, 0, 1)
if ans == "YES":
    print("YES")
else:
    print("NO")
