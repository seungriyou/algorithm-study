# https://school.programmers.co.kr/learn/courses/30/lessons/12946

def solution(n):
    answer = []

    def hanoi(n, src, dest, aux):
        """
        n: 원판 번호 (개수)
        src: 시작 기둥
        dest: 도착 기둥
        aux: 여분 기둥
        """
        # base condition
        if n == 1:
            # print(f"Rod {src} == (Disk {n}) => Rod {dest}")
            answer.append([src, dest])
            return

        # recur
        # (1) (n - 1)개 원판을 aux로 옮기기
        hanoi(n - 1, src, aux, dest)
        # (2) 마지막 원판을 dest로 옮기기
        # print(f"Rod {src} == (Disk {n}) => Rod {dest}")
        answer.append([src, dest])
        # (3) (1)번에서 옮긴 원판을 dest로 옮기기
        hanoi(n - 1, aux, dest, src)

    hanoi(n, 1, 3, 2)

    return answer
