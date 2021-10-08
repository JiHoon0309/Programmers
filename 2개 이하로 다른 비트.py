def solution(numbers):
    bit1=list(bin(numbers[0])[2:])
    i=0
    while True:
        count=0
        bit2=list(bin(numbers[i]+1)[2:])
        if len(bit1)!=len(bit2):
            bit1[0]=0
        for j in range(len(bit2)):
            if bit1[j]!=bit2[j]:
                count+=1
                if count>=3:
                    break
        if count<=1:
            break

    return count

print(solution([2,7]))