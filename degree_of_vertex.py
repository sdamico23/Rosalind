def get_edge(inputFile):
    edge = inputFile.readline()
    edge = edge.split()
    u = int(edge[0])
    v = int(edge[1])
    return (u, v)


inputFile = open('rosalind_deg.txt')
n, m = get_edge(inputFile)  # get vertices and edges
output = [0] * (n+1)
inputArray = []
for i in range(m):
    u, v = get_edge(inputFile)
    inputArray.append(u)
    inputArray.append(v)

def degree_of_vertex(inputArray):
    for i in inputArray:
        output[i] +=1
    return output
output = degree_of_vertex(inputArray)
output.remove(0)
output1 = [str(i) for i in output]
outputString = ""
for i in output1:
    outputString += i
    outputString += " "
print(outputString, file=open("deg_output.txt", "a"))


