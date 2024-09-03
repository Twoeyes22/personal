import statistics

def solution(sides):
    answer = 0
    if max(sides) >= statistics.median(sides) + min(sides):
        return 2
    else:
        return 1

#def solution(sides):
#    return 1 if max(sides) < (sum(sides) - max(sides)) else 2
