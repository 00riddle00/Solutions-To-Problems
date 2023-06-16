def solution(a, b):
    return [f"{a}{b}{a}", f"{b}{a}{b}"][len(a) > len(b)]
