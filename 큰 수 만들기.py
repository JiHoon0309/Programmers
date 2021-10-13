def solution(number, k):
    
    num=list(number)
    
    for _ in range(k):
        num.remove(min(num))
    result=''.join(num)
    
    return result