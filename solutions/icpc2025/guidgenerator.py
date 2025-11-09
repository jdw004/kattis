from collections import defaultdict
import sys
sys.setrecursionlimit(100000)


n = int(input())
data = ' ' + input()

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


trie = {}
out = [0]


def dfs(node, trieNode):
    for nbr in graph[node]:
        if nbr not in visited:
            visited.add(nbr)
            if data[nbr] not in trieNode:
                trieNode[data[nbr]] = {}
                out[0] += 1
            prev = trieNode
            trieNode = trieNode[data[nbr]]
            dfs(nbr, trieNode)
            trieNode = prev


for start in range(1, n+1):
    visited = set()
    visited.add(start)

    if data[start] not in trie:
        trie[data[start]] = {}
        out[0] += 1
    trieNode = trie[data[start]] 


    dfs(start, trieNode)


print(out[0])
