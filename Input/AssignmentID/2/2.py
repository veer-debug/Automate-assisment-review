def solution(arr):
    n = len(arr)
    max_prod = float('-inf')
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j , n):
                max_prod = max(max_prod, arr[i] * arr[j] )
    return max_prod
