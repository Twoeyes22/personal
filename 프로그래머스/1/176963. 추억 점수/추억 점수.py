def solution(name, yearning, photo):
    answer = []
    for pict in photo:
        temp =0 
        for i in range(len(name)):
            if name[i] in pict :
                temp+=yearning[i]
        answer.append(temp)
    return answer