def solution(numbers):
    answer = list(map(str,numbers))
    answer.sort(reverse=True)
    result="".join(answer)
    return result
