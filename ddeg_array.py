def get_edge(inputFile):
    edge = inputFile.readline()
    edge = edge.split()
    u = int(edge[0])
    v = int(edge[1])
    return (u, v)


inputFile = open('rosalind_ddeg.txt')
n, m = get_edge(inputFile)  # get vertices and edges
adjLists = [[] for i in range(n+1)]
for i in range(m):
    visited = [False] * n
    output = []
    u, v = get_edge(inputFile)
    adjLists[u].append(v)
    adjLists[v].append(u)
output = []
for i in adjLists:
    neighbors = 0
    for element in i:
        neighbors += len(adjLists[element])
    output.append(neighbors)
output.pop(0)
output1 = [str(i) for i in output]
outputString = ""
for i in output1:
    outputString += i
    outputString += " "

print(outputString, file=open("ddeg_output.txt", "a"))

