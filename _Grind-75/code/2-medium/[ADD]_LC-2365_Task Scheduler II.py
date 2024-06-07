# https://leetcode.com/problems/task-scheduler-ii/

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        """
        ex. tasks = [5, 8, 8, 5], space = 2

        | day    | 1 | 2 | 3 | 4 | 5 | 6 |
        ---------+---+---+---+---+---+----
        | task   | 5 | 8 | . | . | 8 | 5 |


        - dct에 {task: recent day}를 기록하고, 매 iteration마다 day를 1씩 증가시킨다.
        - 세 번째 8
            - dct = {5: 1, 8: 2}
            - day가 dct[8] + space + 1 (= 5)이어야 한다.
        - 네 번째 5
            - dct = {5: 1, 8: 5}
            - day(= 6)가 dct[5] + space + 1 (= 4)보다 크므로, day는 그대로 유지한다.
        """

        dct = {}  # {task: recent day}
        day = 0

        for task in tasks:
            day += 1

            # 현재 task가 이전에 등장했다면, space 만큼 지날 때까지 day 증가
            # 이때, ++(1씩 증가) 하면 TLE!
            if task in dct and day < (new_day := dct[task] + space + 1):
                day = new_day

            # dct에 기록
            dct[task] = day

        return day
