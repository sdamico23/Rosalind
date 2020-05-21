def get_edge(inputFile):
    edge = inputFile.readline()
    edge = edge.split()
    u = int(edge[0])
    v = int(edge[1])
    return (u, v)


inputFile = open('rosalind_3sum.txt')
numArr, arrLen = get_edge(inputFile)


def threeSum(numArr):
    outputString = ""
    for i in range(numArr):
        list1 = inputFile.readline()
        list1 = list1.split()
        list1a = [int(i) for i in list1]
        done = False
        for i in range(arrLen-1):
            present = []
            for j in range(i+1, arrLen):
                element = -(list1a[i] + list1a[j])
                if element in present:
                    done = True
                    Aindex = str(i + 1)
                    Bindex = str(list1a.index(element) + 1)
                    Cindex = str(j+1)
                    outputString += Aindex + " " + Bindex + " " + Cindex + " \n"
                else:
                    present.append(list1a[j])
        if done == False:
            outputString += "-1 "
            outputString += "\n"
    return outputString


output = threeSum(numArr)
output = output[:output.rfind('\n')]

print(output, file=open("3sum_output.txt", "a"))
