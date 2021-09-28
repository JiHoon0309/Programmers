def solution(s):
    answer=[]
    word=s.split(' ')
    for i in range(len(word)):
        word[i]=word[i].lower()
        result=list(word[i])
        if len(result)==0:
            result=''
        else:
            result[0]=result[0].upper()
        join=''.join(result)
        answer.append(join)
    return ' '.join(answer)