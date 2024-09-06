def solution(sizes):
    answer = 0
    amax=['0','0']
    for i in range(len(sizes)):
        sizes[i].sort()
        for j in range(2):
            if int(amax[j]) < sizes[i][j] :
                amax[j] = sizes[i][j]
        
    return amax[0]*amax[1]