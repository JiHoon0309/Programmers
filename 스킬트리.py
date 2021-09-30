def solution(skill, skill_trees):
    count=0
    for i in range(len(skill_trees)):
        a=[]
        result=list(skill)
        answer=list(skill_trees[i])
        for j in range(len(answer)):
            if len(result)==0:
                break
            if answer[j]==result[0]:
                result.remove(result[0])
            else:
                a.append(answer[j])
        if len(result)==len(skill):
            break
        elif len(result)==0:
            count+=1
        elif result[0] not in a:
            count+=1

    return count