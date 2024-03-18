# https://leetcode.com/problems/implement-trie-prefix-tree/

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # 노드를 타고 내려가기 (defaultdict로 인해 없다면 새로 생성)
        curr = self.root
        for w in word:
            curr = curr.children[w]

        # word가 완성되었음을 표시
        curr.is_word = True

    def search(self, word: str) -> bool:
        # 노드를 타고 내려가면서, 글자가 trie에 없으면 곧바로 False 반환
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]

        # 마지막 글자의 is_word를 반환
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        # 노드를 타고 내려가면서, 글자가 trie에 없으면 곧바로 False 반환
        curr = self.root
        for p in prefix:
            if p not in curr.children:
                return False
            curr = curr.children[p]

        # search와 다르게, prefix가 모두 trie에 포함되어있으면 True 반환
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
