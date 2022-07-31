import sys
count = 0
steps = []


def climb_stairs(n: int) -> int:
    """
    dp easy challenge
    """
    global count
    global steps
    # add your logic here
    rmn = n
    if rmn > 1:
        # step of 1 or 2
        s1 = rmn - 1
        steps.append(1)
        climb_stairs(s1)
        steps.pop()

        s2 = rmn - 2
        steps.append(2)
        climb_stairs(s2)
        steps.pop()
    elif rmn == 1:
        # only step of 1
        count += 1
        steps.append(1)
        print(steps)
        steps.pop()
    elif rmn == 0:
        count += 1
        print(steps)


climb_stairs(int(sys.argv[1]))

print(count)
