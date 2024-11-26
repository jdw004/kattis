x1, y1, x2, y2 = map(int, input().split())

corners = (0,0), (0, 2024), (2024, 0), (2024, 2024)

if (x1,y1) in corners and (x2,y2) in corners:
    print(0)


elif (x1,y1) in corners or (x2,y2) in corners:
    print(1)

else:
    print(2)
