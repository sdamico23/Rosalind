def get_edge(inputFile):
    edge = inputFile.readline()
    edge = edge.split()
    u = int(edge[0])
    v = int(edge[1])
    return (u, v)


inputFile = open('rosalind_2sum.txt')
numArr, arrLen = get_edge(inputFile)

def twoSum(numArr):
    outputString = ""
    for i in range(numArr):
        list1 = inputFile.readline()
        list1 = list1.split()
        list1a = [int(i) for i in list1]
        done = False
        for i in range(0,arrLen):
            for j in range(i+1, arrLen):
                if ((list1a[j] == list1a[i]*(-1)) and (done == False)):
                    outputString += str(i+1) + " " + str(j+1) + " \n"
                    done = True
        if done == False:
            outputString += "-1 "
            outputString += "\n"   
    return outputString


output = twoSum(numArr)
output = output[:output.rfind('\n')]

print(output, file=open("2sum_output.txt", "a"))
