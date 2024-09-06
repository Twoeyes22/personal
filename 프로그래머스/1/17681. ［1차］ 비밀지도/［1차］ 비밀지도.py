def solution(n, arr1, arr2):
    answer = []
    
    for i, j in zip(arr1, arr2):
        # or 연산으로 숫자 지도 만듦 (앞의 2개 인덱스는 '0b'를 갖게되어 2부터 시작)
        a12 = str(bin(i|j)[2:])
        # rjust로 리스트를 n개의 인덱스를 갖게 만들어 줌
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1','#')
        a12 = a12.replace('0',' ')
        answer.append(a12)
        
    return answer