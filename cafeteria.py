from typing import List

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    # Write your code here
    div = K + 1
    S = sorted(S)
    num_seats = (S[0] - 1)//div + (N - S[M-1])//div
    for i in range(1,M):
        num_seats = num_seats + (S[i] - S[i-1] - (K + 1))//div
    return num_seats
    
