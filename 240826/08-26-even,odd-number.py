def solution(num_list):
    answer = []
    A=0
    B=0
    for i in num_list :
        if i%2==1 :
            A+=1
        elif i%2== 0:
            B+=1
    
    answer.append(B)
    answer.append(A)
    return answer
