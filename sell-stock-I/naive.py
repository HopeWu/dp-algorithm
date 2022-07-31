import sys

#a = [6,1,4,2,3,5]
a = [6, 1, 4, 2, 5, 3]
a = [5, 4, 3, 2, 1]


def _max(start: int) -> int:
    return max(a[start:])

MIN = 0

MAXS=[0]
MAXS = MAXS*(len(a)+1)

for i in range(0, len(a)-1):
    profit = _max(i+1) - a[i]
    if profit  > MAXS[1]:
        MAXS[0] = profit

print(max(MAXS))

