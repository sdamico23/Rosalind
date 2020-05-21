inputFile = open('rosalind_mer.txt')
aLen = inputFile.readline()
aLen = int(aLen)
list1 = inputFile.readline()
list1 = list1.split()
list1a = [int(i) for i in list1]
bLen = inputFile.readline()
bLen = int(bLen)
list2 = inputFile.readline()
list2 = list2.split()
list2a = [int(i) for i in list2]

def mergeTwoLists(list1, list2):
    i = 0
    j = 0
    outputList = []
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            outputList.append(list2[j])
            j += 1
        else:
            outputList.append(list1[i])
            i += 1
    if (j == len(list2)):
        extra = list1[i:]
    if (i == len(list1)):
        extra = list2[j:]
    for i in extra:
        outputList.append(i)
    return outputList



output = mergeTwoLists(list1a, list2a)
output1 = [str(i) for i in output]
outputString = ""
for i in output1:
    outputString += i
    outputString += " "
print(outputString, file=open("merge_output.txt", "a"))
