import copy
def solution(participant, completion):
    result=participant.copy()
    for i in range(len(participant)):
        if participant[i] in completion:
            result.remove(participant[i])
            completion.remove(participant[i])
    return ''.join(result)