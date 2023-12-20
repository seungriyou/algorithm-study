# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
# https://app.codility.com/demo/results/trainingKRZPTB-CFH/

def solution(A):
    set_A = set(A)
    for i in range(1, len(A) + 2):
        if i not in set_A:
            return i
        