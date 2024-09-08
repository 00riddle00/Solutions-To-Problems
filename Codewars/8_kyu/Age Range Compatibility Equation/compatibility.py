def dating_range(a):
    return [f"{9*a//10}-{11*a//10}", f"{a//2+7}-{2*(a-7)}"][a>14]
