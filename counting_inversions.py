inputFile = open('rosalind_inv.txt')
size = inputFile.readline()
size = int(size)
list1 = inputFile.readline()
list1 = list1.split()
list1a = [int(i) for i in list1]
inversions = 0


def countingInversions(list1a, newList, left, right):
    inversions = 0
    if left < right:
        half = (left+right)//2
        inversions += countingInversions(list1a, newList, left, half)
        inversions += countingInversions(list1a, newList, half+1, right)
        inversions += mergeTwoLists(list1a, newList, left, half, right)
    return inversions
inversions = countingInversions(list1a)
print(inversions)
