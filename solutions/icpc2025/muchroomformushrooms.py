r, c = map(int, input().split())
import math

area = r * c

if c == 1:
    print(1)
elif r > 2:
    print(-1)
elif r == 1:
    x = math.ceil(area/3)
    print(x)
else:
    count = 1
    area -= 3
    if area > 0:
        count += math.ceil(area/4)
    print(count)
