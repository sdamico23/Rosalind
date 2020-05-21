

inputFile = open('rosalind_bins.txt')
arrLen = inputFile.readline()
arrLen = int(arrLen)
searches = inputFile.readline()
searches = int(searches)

list1 = inputFile.readline()
list1 = list1.split()
list1a = [int(i) for i in list1]
searchArray = inputFile.readline()
searchArray = searchArray.split()
searchArray1 = [int(i) for i in searchArray]
outputArray = []


def binary_search(list1a, searchArray1):
    for element in searchArray1:
        left = 0
        right = len(list1a)-1
        done = False
        while (left <= right) and (done == False):
            half = (left + right)//2
            if (list1a[half] == element):
                outputArray.append(half+1)
                done = True

            if (list1a[half] < element):
                left = half + 1
            else:
                right = half-1
        if (done == False):
            outputArray.append(-1)
    return outputArray


output = binary_search(list1a, searchArray1)
output1 = [str(i) for i in output]
outputString = ""
for i in output1:
    outputString += i
    outputString += " "
print(outputString, file=open("bs_output.txt", "a"))
