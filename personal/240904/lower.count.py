def solution(s):
    if s.count('p') + s.count('P') == s.count('y') + s.count('Y'):
        return True
    elif s.count('p') + s.count('P') + s.count('y') + s.count('Y') == 0:
        return True
    else:
        return False


#--------------------------------------

def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')