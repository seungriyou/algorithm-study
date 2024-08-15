# https://leetcode.com/problems/design-add-and-search-words-data-structure/

from collections import defaultdict, deque


class TrieNode:
    
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for w in word:
            curr = curr.children[w]

        curr.is_word = True

    def search(self, word: str) -> bool:
        """
        "."을 마주치면 해당 children을 모두 타고 내려가야 함
        """

        return self._dfs(self.root, 0, word)
        # return self._bfs(word)

    def _dfs(self, node, idx, word):
        # base condition
        if idx == len(word):
            return node.is_word

        # recur
        if word[idx] == ".":
            # "."을 마주치면 해당 level의 children을 모두 타고 내려가보고, 하나라도 is_word가 True라면 True 반환
            for child in node.children:
                if self._dfs(node.children[child], idx + 1, word):
                    return True

        if (child := word[idx]) in node.children:
            # idx에 위치한 문자가 children에 있다면 타고 내려가기
            return self._dfs(node.children[child], idx + 1, word)

        # "."도 마주치지 않고 children에 word[idx]가 없다면 False 반환
        return False

    def _bfs(self, word):
        q = deque([(self.root, 0)])  # (node, idx)

        while q:
            node, idx = q.popleft()

            # base condition
            if idx == len(word):
                # idx == len(word)인 것이 여러 개일 수 있으므로 return node.is_word X
                if node.is_word:
                    return True
            # iter
            elif word[idx] == ".":
                for child in node.children:
                    q.append((node.children[child], idx + 1))
            else:
                if (child := word[idx]) in node.children:
                    q.append((node.children[child], idx + 1))

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
