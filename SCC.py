def get_edge(inputFile):
    edge = inputFile.readline()
    edge = edge.split()
    u = int(edge[0])
    v = int(edge[1])
    return (u, v)


inputFile = open('rosalind_scc.txt')
n, m = get_edge(inputFile)  # get vertices and edges
adjListsR = [[] for i in range(n+1)]
adjLists = [[] for i in range(n+1)]
for i in range(m):
    u, v = get_edge(inputFile)
    adjListsR[v].append(u)
    adjLists[u].append(v)
for i in adjListsR:
    i.sort()
for i in adjLists:
    i.sort()
order = []


def exploreR(adjListsR, v):
    visited[v] = True
    for u in adjListsR[v]:
        if visited[u] == False:
            exploreR(adjListsR, u)
    order.append(v)


visited = [False]*(n+1)


def dfsR(adjListsR):
    for v in range(len(adjListsR)):
        if visited[v] == False:
            exploreR(adjListsR, v)


visited1 = [False]*(n+1)
# order.pop(0)


def explore(adjLists, v):
    visited1[v] = True
    for u in adjLists[v]:
        if visited1[u] == False:
            explore(adjLists, u)


def dfs(adjLists):
    cc = 0
    for v in order:
        if visited1[v] == False:
            cc += 1
            print(cc)
            explore(adjLists, v)


dfsR(adjListsR)
order.pop(0)
order.reverse()
dfs(adjLists)
