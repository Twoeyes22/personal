def solution(nums):
    answer = 0
    temp=set(nums)
    count=len(nums)
    kind=len(temp)
    
    if int(len(nums)/2) <= len(temp) :# 가져갈 수 있는 마릿수 > 종류 수
        answer = len(nums)/2
    else:
        answer = len(temp)
    return answer