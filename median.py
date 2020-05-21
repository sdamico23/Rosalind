inputFile = open('rosalind_med.txt')
arrLen = inputFile.readline()
arrLen = int(arrLen)
list1 = inputFile.readline()
list1 = list1.split()
list1a = [int(i) for i in list1]
list1a.sort()
element = inputFile.readline()
element = int(element)
output = int(list1a[element-1])

print(output, file=open("median_output.txt", "a"))