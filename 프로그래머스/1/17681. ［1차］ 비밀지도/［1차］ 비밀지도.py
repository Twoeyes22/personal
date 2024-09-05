def solution(n, arr1, arr2):
    answer = []
    map=[]
    
    # OR 연산을 통한 숫자 지도 확보
    for i in range(n):
        map.append(arr1[i]|arr2[i])
    
    temp=[]
    for i in range(n):
        for j in range(n):
            if map[i]>=2**(n-j-1):
                map[i]-=2**(n-j-1)
                temp.append('#')
            elif map[i]<2**(n-j-1):
                temp.append(' ')
        answer.append(''.join(temp))
        temp=[]
           
    return answer