def solution(people, limit):
    sum=0
    count=0
    if people.count(limit//2)==1:
        count+=1
        people.remove(limit//2)
    while len(people)!=0:
        if min(people)>(limit//2):
            count+=len(people)
            break
        else:
            sum+=min(people)
            if sum>=limit:
                count+=1
                sum-=min(people)
                people.append(min(people))
                sum=0
            people.remove(min(people))
              
    return count