def get_edge(inputFile):
    edge = inputFile.readline()
    edge = edge.split()
    u = int(edge[0])
    v = int(edge[1])
    return (u, v)


inputFile = open('rosalind_cc.txt')
n, m = get_edge(inputFile)  # get vertices and edges
adjLists = [[] for i in range(n+1)]

for i in range(m):
    visited = [False] * n
    output = []
    u, v = get_edge(inputFile)
    adjLists[u].append(v)
    adjLists[v].append(u)
for i in adjLists:
    i.sort()
visited = [False]*(n+1)



def explore(adjLists, v):
    visited[v] = True
    for u in adjLists[v]:
        if visited[u] == False:
            explore(adjLists, u)


def dfs(adjLists):
    cc = 0
    for v in range(len(adjLists)):
        if visited[v] == False:
            cc += 1
            print(cc)
            explore(adjLists, v)


dfs(adjLists)
#subtract one because 0 index array for Adjlists