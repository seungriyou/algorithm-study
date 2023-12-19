# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
# https://app.codility.com/demo/results/trainingXUERTN-NKP/

def solution(X, Y, D):
    d, m = divmod(Y - X, D)

    return d + (1 if m else 0)
