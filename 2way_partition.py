inputFile = open('rosalind_par.txt')
arrLen = inputFile.readline()
arrLen = int(arrLen)
list1 = inputFile.readline()
list1 = list1.split()
list1a = [int(i) for i in list1]
partition = list1a[0]
lessThan = []
greaterThan = []
count = list1a.count(partition)
for element in list1a:
    if element > partition:
        greaterThan.append(element)
    if element < partition:
        lessThan.append(element)
output = []
for element in lessThan:
    output.append(element)
for i in range(count):
    output.append(partition)
for element in greaterThan:
    output.append(element)
    
output1 = [str(i) for i in output]
outputString = ""
for i in output1:
    outputString += i
    outputString += " "

print(outputString, file=open("partition_output.txt", "a"))