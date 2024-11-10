def solution(arr):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    return result
