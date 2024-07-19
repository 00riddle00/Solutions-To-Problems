def elevator(left, right, call):
    return ["right","left"][abs(left-call) < abs(right-call)]
