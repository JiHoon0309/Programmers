def solution(n):
    i=1
    binary=bin(n)[2:]
    c=binary.count('1')
    while True:
        n=n+i
        binary=bin(n)[2:]
        count=binary.count('1')
        if c==count:
            break
    
    return n