# ref: https://leetcode.com/problems/task-scheduler/

from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        import heapq

        """w/ heap
        ref: https://leetcode.com/problems/task-scheduler/solutions/104528/python-solution-max-heap-queue-easier-than-awice-s
        """

        q = []
        for task, cnt in Counter(tasks).items():
            heapq.heappush(q, -cnt)  # most frequent 한 순서대로

        res, cycle = 0, n + 1

        while q:
            tmp_time = 0
            tmp = []

            # most frequent 순서대로 cycle 수만큼 pop
            for _ in range(cycle):
                if not q:
                    break
                tmp.append(heapq.heappop(q))
                tmp_time += 1

            # 이번에 pop 한 원소들의 등장 횟수 1 감소
            for cnt in tmp:
                if (new_cnt := cnt + 1) < 0:
                    heapq.heappush(q, new_cnt)

            # q에 원소가 남아있다면 이번 cycle을 꽉 채웠으며(idle이든 task이든) 다음 cycle에서 pop 할 task가 남아있다는 뜻이므로 cycle을 더해주고,
            # 아니라면 이번 cycle을 꽉 채우지 못했을 수도 있으므로 이번 turn에서 기록한 tmp_time을 더해줌
            res += cycle if q else tmp_time

        return res

    def leastInterval1(self, tasks: List[str], n: int) -> int:
        from collections import Counter

        """w/o heap
        ref: https://leetcode.com/problems/task-scheduler/solutions/104504/c-8lines-o-n,
             https://leetcode.com/problems/task-scheduler/solutions/104507/python-straightforward-with-explanation

        -----

        cnts = {"A": 3, "B": 2}, n = 3이라면,
        most frequent task가 "A"이므로 이것부터 배치해본다.
        이때, / 는 most frequent task의 마지막 등장 직전의 위치를 표시한다.

            A _ _ _ A _ _ _ / A
            [______][______]
            (n + 1)칸
                [_______]
              (max_cnt - 1)개

        우선, most frequent task의 맨 마지막 등장을 제외하고(위에서 / 전까지), 확보해야 할 칸(= CPU cycle)의 수를 구해보면
        (n + 1) * (max_cnt - 1)이 된다.

        이 값에 max_cnt와 같은 횟수로 등장하는 원소의 개수(= n_max_cnt)만큼 더해주면 필요한 interval의 최소 개수를 구할 수 있다.

        -----

        하지만 cnts = {"A": 2, "B": 2, "C": 1, "D": 1}, n = 1이라면,
        most frequent task인 "A"를 먼저 배치했을 때

            A _ / A

        와 같이 되므로, 위의 식대로 구하면 (n + 1) * (max_cnt - 1) + n_max_cnt = 2 * 1 + 2 = 4이다.

        그러나 이 값(4)은 전체 tasks의 개수보다 작기 때문에 부족하다.
        따라서 이때는 최소한 모든 tasks를 전부 돌기 위해 필요한 CPU cycle 값으로 len(tasks)를 반환해주어야 한다.
        """

        cnts = list(Counter(tasks).values())
        max_cnt = max(cnts)  # most frequent task의 등장 횟수
        n_max_cnt = cnts.count(max_cnt)  # most frequent task의 개수

        return max(len(tasks), (n + 1) * (max_cnt - 1) + n_max_cnt)
