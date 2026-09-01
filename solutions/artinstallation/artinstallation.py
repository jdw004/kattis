needR, needG, needB = map(int, input().split())
haveR, haveG, haveB = map(int, input().split())
rOrG, gOrB = map(int, input().split())

needR -= haveR
needG -= haveG
needB -= haveB

ans = 0

if needR > 0:
    if rOrG < needR:
        print(-1)
        exit()

    rOrG -= needR
    ans += needR

if needB > 0:
    if gOrB < needB:
        print(-1)
        exit()

    gOrB -= needB
    ans += needB

if needG > 0:
    if rOrG + gOrB < needG:
        print(-1)
        exit()

    ans += needG

print(ans)
