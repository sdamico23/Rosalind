# https://www.google.com/search?q=quicksort+wikipedia&oq=quicksort+wiki&aqs=chrome.0.0j69i57j0l6.2802j1j7&sourceid=chrome&ie=UTF-8
# i used wiki for help
inputFile = open('rosalind_qs.txt')
arrLen = inputFile.readline()
arrLen = int(arrLen)
list1 = inputFile.readline()
list1 = list1.split()
list1a = [int(i) for i in list1]


def partition(list1a, left, right):
    index = left - 1
    part = list1a[right]
    for i in range(left, right):
        if list1a[i] <= part:
            index += 1
            list1a[index], list1a[i] = list1a[i], list1a[index]
    list1a[index+1], list1a[right] = list1a[right], list1a[index+1]
    return index + 1


def quickSort(list1a, left, right):
    if left < right:
        p = partition(list1a, left, right)
        quickSort(list1a, left, p-1)
        quickSort(list1a, p+1, right)


quickSort(list1a, 0, len(list1a)-1)
output1 = [str(i) for i in list1a]
outputString = ""
for i in output1:
    outputString += i
    outputString += " "

print(outputString, file=open("qs_output.txt", "a"))
#
