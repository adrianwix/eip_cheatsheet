def allowed(positions):
    k = len(positions)
    for i in range(k - 1):
        if positions[i] == positions[k - 1]:
            return False
        if (positions[k - 1] - positions[i]) == k - 1 - i:
            return False
        if (positions[k - 1] - positions[i]) == -(k - 1 - i):
            return False
    return True


def setPositions(s):
    if len(s) == n:
        return True
    for i in range(n):
        s.append(i)
        # If the current position is allowed and
        # With they given position there is still a set of position such that
        # the board can be filled
        if allowed(s) and setPositions(s):
            return True
        s.pop()

    return False


n = 6
places = []
print(setPositions(places))
print(places)
