# https://school.programmers.co.kr/learn/courses/30/lessons/118667
# ===== greedy =====
def solution(queue1, queue2):
    from collections import deque

    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(queue1), sum(queue2)

    # 전체 합이 절반으로 나누어떨어지지 않는다면 불가능
    if (s1 + s2) % 2 == 1:
        return -1

    cnt, max_cnt = 0, len(q1) * 4  # 두 큐가 초기 상태 그대로 돌아오게 된다면 두 큐의 합을 같게 만들 수 없는데, 그때의 연산 횟수는 len(q1) * 4 임!
    target = (s1 + s2) // 2

    for i in range(max_cnt + 1):
        if s1 < target:
            tmp = q2.popleft()
            q1.append(tmp)
            s1 += tmp
        elif s1 > target:
            tmp = q1.popleft()
            q2.append(tmp)
            s1 -= tmp
        else:
            return i

    return -1


# ===== two pointer =====
def solution_two_pointer(queue1, queue2):
    q = queue1 + queue2
    tot_sum = sum(q)

    # 전체 합이 절반으로 나누어떨어지지 않는다면 불가능
    if tot_sum % 2 == 1:
        return -1

    # queue1 + queue2에서 two pointer 접근
    target = tot_sum // 2
    lo, hi = 0, len(queue1)  # curr_sum = sum(q[lo:hi])
    curr_sum = sum(queue1)
    cnt = 0

    while lo < len(q) and hi < len(q):
        if curr_sum > target:
            curr_sum -= q[lo]
            lo += 1
            cnt += 1
        elif curr_sum < target:
            curr_sum += q[hi]
            hi += 1
            cnt += 1
        else:
            return cnt

    return -1
