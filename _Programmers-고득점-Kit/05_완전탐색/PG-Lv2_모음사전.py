# https://school.programmers.co.kr/learn/courses/30/lessons/84512
def solution(word):
    answer = cnt = -1
    terminated = False

    def dfs(curr_word):
        nonlocal cnt, answer, terminated
        cnt += 1

        # base condition
        if word == curr_word:
            answer = cnt
            terminated = True
            return

        if terminated or len(curr_word) == 5:
            return

        # recur
        for a in "AEIOU":
            dfs(curr_word + a)

    dfs("")

    return answer


word = "EIO"
print(solution(word))   # should print 1189
