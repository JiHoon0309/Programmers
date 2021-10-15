def solution(s):
    word=list(s)
    i=1
    while True:
        if word[i-1]==word[i]:
            word.remove(word[i-1])
            word.remove(word[i-1])
            i=1
        else:
            i+=1
        if i==len(word) or len(word)==0:
            break

    if len(word)==0:
        result=1
    else:
        result=0
    return result