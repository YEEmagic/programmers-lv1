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
