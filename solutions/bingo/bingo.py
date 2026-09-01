inS = input().split()

x = inS[-1]
if int(x) % 10 == 0:
    print(10)
else:
    print(x[-1])
