def solution(s):
    word=list(s)
    next=[]
    count=0
    loop=0
    result=[]
    while True:
        for i in range(len(word)):
            if word[i]=='0':
                count+=1
            else:
                next.append(word[i])
        word==next
        b=bin(len(next))
        word=list(b)
        word.remove(word[:1])
        loop+=1
    result.append(loop,count)
    return b

print(solution("110010101001"))