# https://leetcode.com/problems/accounts-merge/

from typing import List

from collections import defaultdict


class UF:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, child, parent):
        self.parent[self.find(child)] = self.find(parent)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        Union Find
        ref: https://leetcode.com/problems/accounts-merge/solutions/1084738/python-the-clean-union-find-solution-you-are-looking-for
        complexity: https://leetcode.com/problems/accounts-merge/solutions/1084738/python-the-clean-union-find-solution-you-are-looking-for/comments/1221297
        """
        uf = UF(len(accounts))

        # 1. create unions
        ownership = {}  # {email: accounts_idx}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    # ownership에 이미 email 정보가 존재한다면, union으로 합쳐나가기
                    uf.union(i, ownership[email])

                # ownership 정보 기록
                ownership[email] = i

        # 2. create result
        result = defaultdict(list)
        for email, acc_idx in ownership.items():
            result[uf.find(acc_idx)].append(email)

        return [[accounts[idx][0]] + sorted(emails) for idx, emails in result.items()]


class Solution2:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        DFS
        ref: https://leetcode.com/problems/accounts-merge/solutions/109161/python-simple-dfs-with-explanation
        """
        # 그래프 구성 {email: [account idx]}
        graph = defaultdict(list)
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                graph[email].append(i)

        # visited[i] = accounts[i]를 방문했는지 여부
        visited = [False] * len(accounts)

        # dfs 함수 작성
        def dfs(acc_idx: int, emails: set[str]):
            # 현재 account 방문 처리
            visited[acc_idx] = True

            # 현재 account의 _email을 순회
            for i in range(1, len(accounts[acc_idx])):
                _email = accounts[acc_idx][i]

                # _email이 이미 속해있으면 넘어가기
                # if _email in emails:
                #     continue

                # 현재 account에 속하는 _email 기록
                emails.add(_email)

                # _email이 속하는 다른 account를 찾아 dfs
                for ngbr_idx in graph[_email]:
                    if not visited[ngbr_idx]:
                        dfs(ngbr_idx, emails)

        # 모든 account에 대해 각각 dfs 수행
        result = []
        for i, (name, *emails) in enumerate(accounts):
            if not visited[i]:
                emails = set()
                dfs(i, emails)
                result.append([name] + sorted(list(emails)))

        return result


###### review ######
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """union find"""
        from collections import defaultdict

        def find_parent(x):
            if x != parent[x]:
                parent[x] = find_parent(parent[x])
            return parent

        def union_parent(child, parent):
            child, parent = find_parent(child), find_parent(parent)
            parent[child] = parent

        n = len(accounts)  # account 개수
        parent = list(range(n))  # account를 merge 할 것이므로

        # 1. union
        ownership = {}  # {email: account idx}
        for i, (name, *emails) in enumerate(accounts):
            for email in emails:
                # 이미 해당 email 정보가 ownership에 존재한다면, union
                if email in ownership:
                    union_parent(i, ownership[email])

                # ownership 업데이트
                ownership[email] = i

        # 2. res
        res = defaultdict(list)
        for email, idx in ownership.items():
            res[find_parent(idx)].append(email)

        return [[accounts[idx][0], *emails] for idx, emails in res.items()]

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """DFS"""
        from collections import defaultdict

        # graph 구성 ({email: [account idx]})
        graph = defaultdict(list)
        for i, (name, *emails) in enumerate(accounts):
            for email in emails:
                graph[email].append(i)

        # dfs -> 같은 email을 가지는 account 끼리는 neighbor
        visited = [False] * len(accounts)

        def dfs(idx: int, emails: set[int]):
            """
            idx: account의 index
            emails: 현재 person에 해당하는 email로 구성된 set
            """
            visited[idx] = True

            # idx에 해당하는 account의 email 순회
            for i in range(1, len(accounts[idx])):
                email = accounts[idx][i]

                # 이미 기록한 email이라면 넘어가기
                if email in emails:
                    continue

                # 현재 account에 속하는 email 기록
                emails.add(email)

                # 해당 email을 가지고 있는 account에 대해서 dfs
                for nidx in graph[email]:
                    if not visited[nidx]:
                        dfs(nidx, emails)

        # 모든 account에 대해 각각 dfs 수행 (w/ visited)
        res = []
        for i, (name, *emails) in enumerate(accounts):
            if not visited[i]:
                emails = set()
                dfs(i, emails)
                res.append([name, *sorted(emails)])

        return res
