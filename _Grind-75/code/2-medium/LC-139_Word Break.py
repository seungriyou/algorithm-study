# https://leetcode.com/problems/word-break/

from typing import List
from functools import cache

class Solution:
    # 뒤에서부터 확인해나가는 것이 포인트인 것 같다!
    # ref: https://leetcode.com/problems/word-break/solutions/1455100/python-3-solutions-top-down-dp-bottom-up-dp-then-optimised-with-trie-clean-concise

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """bottom up & trie"""
        from collections import defaultdict

        class TrieNode:
            def __init__(self):
                self.is_word = False
                self.child = defaultdict(TrieNode)

            def add_word(self, word):
                curr = self

                # word의 문자들을 타고 내려가기
                for c in word:
                    curr = curr.child[c]

                # 단어가 완료됨을 표시하기
                curr.is_word = True

        # trie 구성하기                             -- O(t)
        root = TrieNode()
        for word in wordDict:
            root.add_word(word)

        n = len(s)

        # dp[i] = s[i:]가 wordDict의 word로 구성될 수 있는지 여부
        dp = [False] * (n + 1)
        dp[n] = True

        for start in range(n - 1, -1, -1):
            curr = root
            for end in range(start + 1, n + 1):  # -- O(n^2)
                c = s[end - 1]

                # c가 curr.child에 없다면 중단
                if c not in curr.child:
                    break

                # c가 curr.child에 있다면 타고 내려가기
                curr = curr.child[c]

                # (1) word가 완성됐고 (2) dp[end]가 True이면
                if curr.is_word and dp[end]:
                    dp[start] = True
                    break

        return dp[0]

    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        """bottom up"""
        n = len(s)
        words = set(wordDict)                           # -- O(m)

        # dp[i] = s[i:]가 wordDict의 word로 구성될 수 있는지 여부
        dp = [False] * (n + 1)
        dp[n] = True

        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n + 1):         # -- O(n^2)
                # (1) dp[end]가 True이고 (2) wordDict에 현재 찾고 있는 word가 있다면
                if dp[end] and s[start:end] in words:   # -- O(n)
                    dp[start] = True
                    break

        return dp[0]

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        """top down"""
        n = len(s)
        words = set(wordDict)

        @cache
        def dp(start):
            # base condition
            if start == n:
                return True

            # substring인 word의 right end를 늘려가며 확인
            for end in range(start + 1, n + 1):
                # (1) wordDict에 word가 있고 (2) dp(end)가 True라면
                if s[start:end] in words and dp(end):
                    return True

            return False

        return dp(0)
