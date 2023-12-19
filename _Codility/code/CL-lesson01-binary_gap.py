# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
# https://app.codility.com/demo/results/trainingN3WFDG-3B4/

def solution(N):
    binary = bin(N)[2:]

    cnt = max_len = 0

    for b in binary:
        if b == "1":
            if cnt > max_len:
                max_len = cnt
                cnt = 0
            else:
                cnt = 0
        else:
            cnt += 1

    return max_len
