# https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0

    skill_set = set(skill)

    def is_valid(skill_tree):
        """
        - skill을 pointer p를 이용하여 가리키기
        - 현재 보고 있는 skill_tree 내 skill이 skill_set 안에 있으면서, 해당 skill이 skill[p]가 아닌 경우 X
        """
        p = 0

        for sk in skill_tree:
            # (1) 현재 보고 있는 skill_tree 내 skill이 skill_set 안에 있으면서
            if sk in skill_set:
                # (2) 해당 skill이 skill[p]가 아니라면 순서가 맞지 않으므로 빠르게 종료
                if sk != skill[p]:
                    return False
                # (3) 해당 skill이 skill[p]와 동일하다면 순서가 맞으므로 p++
                p += 1

        return True

    for st in skill_trees:
        answer += is_valid(st)

    return answer
