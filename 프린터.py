def solution(priorities, location):
    order=max(priorities)

    while priorities[0]!=order:
        priorities.append(priorities[0])
        priorities.remove(priorities[0])
        location-=1
        if location==-1:
            location=len(priorities)-1
    return location+1