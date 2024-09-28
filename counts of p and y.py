def solution(s):
    a=0
    b=0

    c = list(s)
    for i in c:
        if i == 'p' or i =='P':
            a += 1
        elif i == 'y' or i == 'Y':
            b += 1
    if a == b or a == 0:
        return True
    elif a != b:
        return False
        
    '''결론은 p랑 y의 개수가 문자열 내에서 같아야 됨.
        대소문자 관계 없음 짝만 맞으면 됨.
    '''

    # 솔직히 더 쉬운 풀이도 있을 것 같지만 다음번에 고민해보자.
    # 중요한 건 조건을 두 번 주는 것, 
    # 그리고 range함수는 integer만 받을 수 있으므로 
    # 비슷한 문제를 만난다면 
    # range함수 보다는 다른 방법을 생각해볼 것
