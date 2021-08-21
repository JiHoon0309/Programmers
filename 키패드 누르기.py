def solution(numbers, hand):
    key=[[1,4,7,'*'],[2,5,8,0],[3,6,9,'#']]
    result=[]
    right_finger='#'
    left_finger='*'
    for i in range(len(numbers)):
        if numbers[i] in key[0]:
            result.append('L')
            left_finger=numbers[i]
        elif numbers[i] in key[2]:
            result.append('R')
            right_finger=numbers[i]
        elif numbers[i] in key[1]:   #다음 숫자가 가운데 줄일때
            if left_finger in key[0] and right_finger in key[2]:   #왼 오
                if abs(key[0].index(left_finger)-key[1].index(numbers[i]))>abs(key[2].index(right_finger)-key[1].index(numbers[i])):
                    result.append('R')
                    right_finger=numbers[i]
                elif abs(key[0].index(left_finger)-key[1].index(numbers[i]))<abs(key[2].index(right_finger)-key[1].index(numbers[i])):
                    result.append('L')
                    left_finger=numbers[i]
                elif abs(key[0].index(left_finger)-key[1].index(numbers[i]))==abs(key[2].index(right_finger)-key[1].index(numbers[i])):
                    if hand=='right':
                        result.append('R')
                        right_finger=numbers[i]
                    else:
                        result.append('L')
                        left_finger=numbers[i]
            elif left_finger in key[1] and right_finger in key[2]:   #중 오
                if abs(key[1].index(left_finger)-key[1].index(numbers[i]))>abs(key[2].index(right_finger)-key[1].index(numbers[i]))+1:
                    result.append('R')
                    right_finger=numbers[i]
                elif abs(key[1].index(left_finger)-key[1].index(numbers[i]))<abs(key[2].index(right_finger)-key[1].index(numbers[i]))+1:
                    result.append('L')
                    left_finger=numbers[i]
                elif abs(key[1].index(left_finger)-key[1].index(numbers[i]))==abs(key[2].index(right_finger)-key[1].index(numbers[i]))+1:
                    if hand=='right':
                        result.append('R')
                        right_finger=numbers[i]
                    else:
                        result.append('L')
                        left_finger=numbers[i]
            elif left_finger in key[0] and right_finger in key[1]:   #왼 중
                if abs(key[0].index(left_finger)-key[1].index(numbers[i]))+1>abs(key[1].index(right_finger)-key[1].index(numbers[i])):
                    result.append('R')
                    right_finger=numbers[i]
                elif abs(key[0].index(left_finger)-key[1].index(numbers[i]))+1<abs(key[1].index(right_finger)-key[1].index(numbers[i])):
                    result.append('L')
                    left_finger=numbers[i]
                elif abs(key[0].index(left_finger)-key[1].index(numbers[i]))+1==abs(key[1].index(right_finger)-key[1].index(numbers[i])):
                    if hand=='right':
                        result.append('R')
                        right_finger=numbers[i]
                    else:
                        result.append('L')
                        left_finger=numbers[i]
            elif left_finger in key[1] and right_finger in key[1]:   #중 중
                if abs(key[1].index(left_finger)-key[1].index(numbers[i]))>abs(key[1].index(right_finger)-key[1].index(numbers[i])):
                    result.append('R')
                    right_finger=numbers[i]
                elif abs(key[1].index(left_finger)-key[1].index(numbers[i]))<abs(key[1].index(right_finger)-key[1].index(numbers[i])):
                    result.append('L')
                    left_finger=numbers[i]
                elif abs(key[1].index(left_finger)-key[1].index(numbers[i]))==abs(key[1].index(right_finger)-key[1].index(numbers[i])):
                    if hand=='right':
                        result.append('R')
                        right_finger=numbers[i]
                    else:
                        result.append('L')
                        left_finger=numbers[i]
    answer="".join(result)
    return answer