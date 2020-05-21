def get_edge(inputFile):
    edge = inputFile.readline()
    edge = edge.split()
    u = int(edge[0])
    v = int(edge[1])
    return (u, v)
inputFile = open('rosalind_maj.txt')
numArr, arrLen = get_edge(inputFile)
outputList = []
key = arrLen/2
def majorityElement(numArr):
    for i in range(numArr): 
        list1 = inputFile.readline()
        list1 = list1.split()
        list1a = [int(i) for i in list1]
        done = False
        for element in list1a:
            conj = element*(-1)
            for j in list1a: 
                if (list1a[j] == conj):
                    output.append(element.index())
                    output.append(j+1)
                    done = True 
                    break 
        if (done == False):
            outputList.append(int(-1))
    return outputList
output = majorityElement(numArr)
output1 = [str(i) for i in output]
outputString = ""
for i in output1:
    outputString += i
    outputString += " "
print(outputString, file=open("majority_element.txt", "a"))