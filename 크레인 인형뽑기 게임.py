def solution(board, moves):
    result=[]
    count=0
    for i in range(len(moves)):
            for j in range(len(board[0])):
                if board[j][moves[i]-1]==0:
                    continue
                elif board[j][moves[i]-1]!=0:
                    result.append(board[j][moves[i]-1])
                    board[j][moves[i]-1]=0
                    break
            if len(result)>=2 and result[-1]==result[-2]:
                result.pop()
                result.pop()
                count+=2
            else:
                continue
    return count    