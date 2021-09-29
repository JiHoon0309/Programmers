def solution(skill, skill_trees):
    count=0
    a=set(skill)
    for i in range(len(skill_trees)):
        result=list(skill)
        for j in range(len(skill_trees[i])):
            if len(result)==0:
                break
            if skill_trees[i][j]==result[0]:
                result.remove(result[0])
        
        b=set(result)
        if len(a-b):
            count+=1

    return count