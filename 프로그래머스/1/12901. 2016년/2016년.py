from datetime import datetime, date

def solution(a, b):
    # 요일 이름을 리스트로 정의 (월요일부터 시작)
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    
    # 2016년 a월 b일의 날짜 객체 생성
    target_date = date(2016, a, b)
    
    # weekday() 메서드는 0(월요일)부터 6(일요일)까지의 값을 반환
    day_index = target_date.weekday()
    
    # 해당 요일 이름 반환
    return days[day_index]