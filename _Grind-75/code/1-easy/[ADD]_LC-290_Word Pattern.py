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


###### review ######
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """1-dict"""

        """
        p_to_s 혹은 s_to_p 중 p_to_s만 사용하는 경우를 살펴보자.

            pattern s                   p_to_s                      result  correct
            ------- ------------------- --------------------------- ------- -------
        <1> abba    dog cat cat cow     {a: dog, b: cat}            False   O
        <2> abbc    dog cat cat cat     {a: dog, b: cat, c: cat}    True    X

        <1>, <2>는 모두 False를 반환해야 하지만,
        <1> 케이스에서만 올바르게 False를 반환하며, <2> 케이스에서는 True를 반환하게 된다.
        <2> 케이스를 1-dict로 동작할 수 있도록 하려면, pattern의 종류 개수와 s의 종류 개수가 동일한지를 살펴보면 된다.
        """

        ss = s.split()

        # 개수가 동일하지 않다면 빠르게 stop
        if len(pattern) != len(ss):
            return False

        # pattern의 종류 개수와 s의 종류 개수가 동일하지 않다면 빠르게 stop
        if len(set(pattern)) != len(set(ss)):
            return False

        # 1-dict
        p_to_s = {}

        for p, s in zip(pattern, ss):
            # if p in p_to_s and p_to_s[p] != s:
            #     return False

            # p_to_s[p] = s

            if p not in p_to_s:
                p_to_s[p] = s

            elif p_to_s[p] != s:
                return False

        return True

    def wordPattern2(self, pattern: str, s: str) -> bool:
        """2-dict"""

        ss = s.split()

        # 개수가 동일하지 않다면 빠르게 stop
        if len(pattern) != len(ss):
            return False

        # p_to_s = {pattern: word}, s_to_p = {word: pattern}
        p_to_s, s_to_p = {}, {}
        """
        p_to_s 만 사용하면, <1> 케이스에서는 옳은 결과를 반환하지만, <2> 케이스에서는 올바르지 않은 결과를 반환하게 된다.

            pattern s                   p_to_s                      correct
            ------- ------------------- --------------------------- -------
        <1> abba    dog cat cat dog     {a: dog, b: cat}            O
        <2> abbc    dog cat cat cat     {a: dog, b: cat, c: cat}    X

        따라서 {word: pattern}을 저장하는 s_to_p도 확인해야 한다.
        """

        for p, s in zip(pattern, ss):
            # p_to_s 확인
            if p in p_to_s and p_to_s[p] != s:
                return False

            # s_to_p 확인
            if s in s_to_p and s_to_p[s] != p:
                return False

            # 기록하기
            p_to_s[p], s_to_p[s] = s, p

        return True
