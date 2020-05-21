inputFile = open('rosalind_ps.txt')
arrLen = inputFile.readline()
arrLen = int(arrLen)
list1 = inputFile.readline()
list1 = list1.split()
list1a = [int(i) for i in list1]
list1a.sort()
numEl = inputFile.readline()
numEl = int(numEl)
outputList = []
for i in range(numEl):
    outputList.append(list1a[i])

output1 = [str(i) for i in outputList]
outputString = ""
for i in output1:
    outputString += i
    outputString += " "
print(outputString, file=open("partial_sort_output.txt", "a"))