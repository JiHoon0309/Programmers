def solution(n):
    word_1='수'
    word_2='수박'
    if n%2!=0:
        answer=word_2*(n//2)+word_1
    else:
        answer=word_2*(n//2)
    return answer