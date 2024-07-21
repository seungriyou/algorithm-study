# https://school.programmers.co.kr/learn/courses/30/lessons/172927

def solution(picks, minerals):
    """Greedy (참고)"""

    answer = 0

    # (1) 광산에 있는 모든 광물을 캐거나 (2) 더 사용할 곡괭이가 없을 때까지 캐야하므로
    minerals = minerals[:sum(picks) * 5]  # (2)번 반영
    minerals = [minerals[i:i + 5] for i in range(0, len(minerals), 5)]

    mapping = {"diamond": 0, "iron": 1, "stone": 2}
    damage_table = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]

    damages = []
    for mineral in minerals:
        damage = [0] * 3  # [dia, iron, stone]
        for m in mineral:
            # 세 가지 곡괭이로 현재 광물 m을 캘 때의 피로도를 각각 기록
            for i in range(3):
                damage[i] += damage_table[i][mapping[m]]
        damages.append(damage)

    # greedy - 광물셋별 피로도 값 계산한 값을 내림차순 정렬 (우선순위: stone > iron > dia 순)
    damages = sorted(damages, key=lambda x: (-x[2], -x[1], -x[0]))

    # 가장 피로도가 높은 광물셋 부터 dia > iron > stone 순으로 사용하며 캐기
    for damage in damages:
        # 세 가지 곡괭이 (dia > iron > stone 순으로)
        for i in range(3):
            if picks[i]:
                picks[i] -= 1  # 곡괭이 하나 사용
                answer += damage[i]  # 이 구간에서 해당 곡괭이를 사용했을 때의 피로도 기록
                break  # 현재 광물셋은 캤으므로 넘어가기

    return answer


def solution_dfs(picks, minerals):
    """DFS"""

    mapping = {"diamond": 0, "iron": 1, "stone": 2}
    damage = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    n = len(minerals)
    min_damage_val = 1e9

    def dfs(idx, capacity, damage_val):
        nonlocal min_damage_val

        # base condition
        # (1) 모든 광물을 캤거나 (2) 더 사용할 곡괭이가 없는 경우 종료
        if idx == n or capacity == [0, 0, 0]:
            min_damage_val = min(min_damage_val, damage_val)
            return

        # recur
        # 세 종류의 곡괭이
        for i in range(3):
            # 해당 곡괭이 수가 남았다면
            if capacity[i]:
                # capacity에서 현재 곡괭이 수 --
                new_capacity = capacity[:]
                new_capacity[i] -= 1

                # idx 부터 5개를 볼 때, 오른쪽의 인덱스 값 (idx 오른쪽에 원소가 4개 미만이라면 n)
                last_idx = min(idx + 5, n)

                # 지금 보고 있는 광물들을 캘 때 얻는 tmp_damage_val 계산 (damage_val에 바로 += 하면 에러..?)
                tmp_damage_val = sum(
                    damage[i][mapping[minerals[j]]]
                    for j in range(idx, last_idx)
                )

                # 다음
                dfs(last_idx, new_capacity, damage_val + tmp_damage_val)

    dfs(0, picks, 0)

    return min_damage_val
