# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """1 dict"""

        ptos = {}
        ss = s.split()

        # early stop
        if len(pattern) != len(ss):
            return False
        if len(set(pattern)) != len(set(ss)):
            return False

        # 패턴 확인
        for p, s in zip(pattern, ss):
            # p가 ptos에 없다면, 새롭게 기록
            if p not in ptos:
                ptos[p] = s
            # ptos[p]가 s와 다르다면 False 반환
            elif ptos[p] != s:
                return False

        return True

    def wordPattern3(self, pattern: str, s: str) -> bool:
        """1 dict"""

        stop = {}
        ss = s.split()

        # early stop
        if len(pattern) != len(ss):
            return False
        # single dict인 stop를 이용하므로, p는 이전에 등장했으나 s가 다른 경우(즉, False 반환해야 하는 경우)를 잡을 수 없음
        # ex) pattern = "abba" , ss = ["dog", "cat", "cat", "fish"]
        #      => p = 마지막 "a", s = "fish" 일 때, p는 처음에 이미 등장했으나, 현재 s가 "dog"가 아닌 "fish"이므로 False 반환해야 함
        # 따라서 이러한 경우를 잡기 위해 pattern과 ss의 종류 개수가 같은지를 미리 확인함!
        if len(set(pattern)) != len(set(ss)):
            return False

        # 패턴 확인
        for p, s in zip(pattern, ss):
            # s가 stop에 없다면, 새롭게 기록
            if s not in stop:
                stop[s] = p
            # stop[s]가 p와 다르다면 False 반환
            elif stop[s] != p:
                return False

        return True

    def wordPattern2(self, pattern: str, s: str) -> bool:
        """2 dict"""

        ptos, stop = {}, {}
        ss = s.split()

        # 길이 확인
        if len(pattern) != len(ss):
            return False

        # 패턴 확인
        for p, s in zip(pattern, ss):
            # ptos에 기록된 것과 일치하지 않으면 False
            if p in ptos and ptos[p] != s:
                return False

            # stop에 기록된 것과 일치하지 않으면 False
            if s in stop and stop[s] != p:
                return False

            # 위에 모두 해당하지 않으면 기록
            ptos[p] = s
            stop[s] = p

        return True
