def solution(k, score):
    # 위에서 K번째 등수만 기록
    answer = []
    temp = []
    
    for i in range(len(score)):
        temp.append(score[i])
        temp.sort()
        if i < k :
            answer.append(temp[0])
        else:
            answer.append(temp[-k])
            
    return answer