N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N + 1):
        cnt = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = cnt / length
            length -= cnt
        answer.append((i, fail))

    answer.sort(key=lambda x: x[1], reverse=True)

    return [i[0] for i in answer]

print(solution(N, stages))
