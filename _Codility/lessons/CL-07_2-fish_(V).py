# https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/
# https://app.codility.com/demo/results/trainingFH5FDE-MEG/

def solution(A, B):
    down = []
    alive_cnt = 0

    for i in range(len(A)):
        # downstream이라면 down에 추가
        if B[i] == 1:
            down.append(i)

        # upstream이라면, 존재하는 모든 downstream 물고기들과 끝에서부터 비교
        else:
            while down:
                idx = down.pop()
                # i가 down top보다 작은 경우, i가 잡아먹힘
                if A[idx] > A[i]:
                    down.append(idx)  # pop한 값 다시 넣어주기
                    break
            # i가 모든 downstream 물고기들을 이겼다면, cnt++
            if not down:
                alive_cnt += 1

    # 최종적으로, down에 남아있는 물고기들도 alive_cnt에 반영
    return alive_cnt + len(down)
