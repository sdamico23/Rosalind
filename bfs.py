def get_edge(inputFile):
    edge = inputFile.readline()
    edge = edge.split()
    u = int(edge[0])
    v = int(edge[1])
    return (u, v)


inputFile = open('rosalind_bfs.txt')
n, m = get_edge(inputFile)  # get vertices and edges
adjLists = [[] for i in range(n+1)]
for i in range(m):
    u, v = get_edge(inputFile)
    adjLists[u].append(v)
for i in adjLists:
    i.sort()


dist = [-1] * (n+1)
dist[1] = 0
q = [1]
while (len(q) != 0):
    u = q.pop(0)
    for v in adjLists[u]:
        if (dist[v] == -1):
            q.append(v)
            dist[v] = dist[u] + 1
dist.pop(0)
output1 = [str(i) for i in dist]
outputString = ""
for i in output1:
    outputString += i
    outputString += " "


print(outputString, file=open("bfs_output.txt", "a"))