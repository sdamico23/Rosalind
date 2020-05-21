
def get_edge(inputFile):
    edge = inputFile.readline()
    edge = edge.split()
    u = int(edge[0])
    v = int(edge[1])
    return (u, v)


def dfs(adjLists, visited, u, output):
    visited[u] = True
    for v in adjLists[u]:
        if not visited[v]:
            dfs(adjLists, visited, v, output)
    output.append(u + 1)


inputFile = open('rosalind_ts.txt')
n, m = get_edge(inputFile)  # get vertices and edges
adjLists = [[] for i in range(n)]
#top sort using DFS
for i in range(m):
    visited = [False] * n
    output = []
    u, v = get_edge(inputFile)
    adjLists[u-1].append(v-1)

    for u in range(n):
        if not visited[u]:
            dfs(adjLists, visited, u, output)
# get in output form for rosalind
output.reverse()

output1 = [str(i) for i in output]
outputString = ""
for i in output1:
    outputString += i
    outputString += " "

print(outputString, file=open("ts_output.txt", "a"))
