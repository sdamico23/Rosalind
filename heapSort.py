inputFile = open('rosalind_hs.txt')
size = inputFile.readline()
size = int(size)
list1 = inputFile.readline()
list1 = list1.split()
list1a = [int(i) for i in list1]


def max_heapify(list1a, size, root):
    max = root
    leftChild = 2*root + 1
    rightChild = 2*root + 2
    if (leftChild < size) and (list1a[leftChild] > list1a[max]):
        max = leftChild
    if (rightChild < size) and (list1a[rightChild] > list1a[max]):
        max = rightChild
    if (max != root):
        list1a[root], list1a[max] = list1a[max], list1a[root]
        max_heapify(list1a, size, max)


def max_heap(list1a, size):
    leaf = int((size/2)) - 1
    for i in range(leaf, -1, -1):
        max_heapify(list1a, size, i)


def heap_sort(list1a):
    max_heap(list1a, size)
    for i in range(size-1, 0, -1):
        list1a[i], list1a[0] = list1a[0], list1a[i]
        max_heapify(list1a, i, 0)

heap_sort(list1a)
output1 = [str(i) for i in list1a]
outputString = ""
for i in output1:
    outputString += i
    outputString += " "

print(outputString, file=open("heapSort_output.txt", "a"))



