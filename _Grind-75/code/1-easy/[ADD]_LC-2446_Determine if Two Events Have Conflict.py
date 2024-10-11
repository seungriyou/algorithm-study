# https://leetcode.com/problems/determine-if-two-events-have-conflict/

from typing import List


class Solution:
    def haveConflict1(self, event1: List[str], event2: List[str]) -> bool:
        def convert(event):
            return (int(time.replace(":", "")) for time in event)

        s1, e1 = convert(event1)
        s2, e2 = convert(event2)

        return e1 >= s2 and e2 >= s1

    def haveConflict2(self, event1: List[str], event2: List[str]) -> bool:
        (s1, e1), (s2, e2) = event1, event2

        return min(e1, e2) >= max(s1, s2)

    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        (s1, e1), (s2, e2) = event1, event2

        return e1 >= s2 and e2 >= s1
    