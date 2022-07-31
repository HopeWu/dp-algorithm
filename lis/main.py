lkDict = dict()
length = 0
maxLen = 0
result = []
a = [10, 20, 2, 5, 3, 8, 8, 25, 6]
a = [71, 0, 4, 42, -31, 4, -42]
a = [77, 0, -2, 25, 1, 70]


def _getLengthOfLIS(A):
    global lkDict
    n = len(A)
    for i in range(0, n):
        li = []
        for j in range(i+1, n):
            if A[j] > A[i]:
                li.append(j)
        lkDict[i] = li


def getLengthOfLIS(index):
    global lkDict, maxLen, length, a, result
    result.append(a[index])
    length += 1
    if lkDict[index]:
        for i in lkDict[index]:
            getLengthOfLIS(i)
    else:
        if length > maxLen:
            maxLen = length
        length = 0
        result = []


_getLengthOfLIS(a)
for i in range(len(a)):
    length = 0
    result = []
    getLengthOfLIS(i)

print(maxLen)
