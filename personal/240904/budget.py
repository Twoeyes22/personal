def solution(d, budget):
    answer = 0
    D = sorted(d)
    for i in D:
        budget-=i
        if budget >= 0:
            answer+=1
    return answer
#---------------------------------------- 

#def solution(d, budget):
#    d.sort()
#    while budget < sum(d):
#        d.pop()
#    return len(d)
