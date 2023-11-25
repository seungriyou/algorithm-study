# https://school.programmers.co.kr/learn/courses/30/lessons/64064

"""순열로 풀 수 있겠다는 생각 -> backtrack"""

# ===== Backtracking =====
def solution(user_id, banned_id):
    un, bn = len(user_id), len(banned_id)

    def is_matched(uid, bid):
        # user id와 banned id의 길이가 다르다면 False
        if len(uid) != len(bid):
            return False

        # 둘 중 하나라도 "*" 이거나 두 문자가 같으면 다음 문자 이어서 확인
        # 아니라면 곧바로 False 반환
        for u, b in zip(uid, bid):
            if u != "*" and b != "*" and u != b:
                return False

        return True

    result = set()
    prev_elements = list()
    seen = [False] * un  # -- user를 prev_element에 넣었다면 True

    def backtrack(b_idx):
        # base condition
        if len(prev_elements) == bn:    # -- b_idx == bn 조건은 굳이 볼 필요가 없다!
            result.add(tuple(sorted(prev_elements)))  # -- set의 원소는 hashable 해야 하므로 set 안에 set을 넣을 수 없다!
            return

        # recur
        for ui in range(un):
            if not seen[ui] and is_matched(user_id[ui], banned_id[b_idx]):
                prev_elements.append(user_id[ui])
                seen[ui] = True
                backtrack(b_idx + 1)    # -- backtrack!
                prev_elements.pop()
                seen[ui] = False

    backtrack(0)

    return len(result)


# ===== Brute-Force =====
def solution_perm(user_id, banned_id):
    from itertools import permutations

    result = set()

    def is_matched(uid, bid):
        # user id와 banned id의 길이가 다르다면 False
        if len(uid) != len(bid):
            return False

        # 둘 중 하나라도 "*" 이거나 두 문자가 같으면 다음 문자 이어서 확인
        # 아니라면 곧바로 False 반환
        for u, b in zip(uid, bid):
            if u != "*" and b != "*" and u != b:
                return False

        return True

    def check(case, banned_id):
        # user id로 만든 case와 banned id의 원소를 하나씩 비교
        for uid, bid in zip(case, banned_id):
            # 하나라도 match 되지 않으면 False 반환
            if not is_matched(uid, bid):
                return False

        return True

    for case in permutations(user_id, len(banned_id)):
        if check(case, banned_id):
            result.add(tuple(sorted(case)))

    return len(result)
