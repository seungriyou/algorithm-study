# https://leetcode.com/problems/lru-cache/

class Node:
    """
    linked list
    - 어떤 node를 사용할 때마다 linked list의 tail로 이동시키면, least recently used가 항상 head에 위치
        -> node의 usage를 constant time에 판단할 수 있게 된다!
    - 하지만 사용하는 node를 linked list에서 찾으려면 O(1)이 아닌 O(n) 소요
        -> hash table을 이용해 O(1)에 사용하는 node를 linked list에서 찾을 수 있도록 한다!
    """

    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # hash table
        self.dic = dict()  # {key: node of linked list}
        # doubly-linked list
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    #### for doubly-linked list ####
    def _remove(self, node):
        pnode = node.prev
        nnode = node.next
        pnode.next = nnode
        nnode.prev = pnode

    def _add(self, node):
        """tail에 node 추가하기"""
        # node 앞 뒤 설정
        pnode = self.tail.prev
        pnode.next = node
        self.tail.prev = node

        # node 설정
        node.prev = pnode
        node.next = self.tail

    #####################

    def get(self, key: int) -> int:
        """
        1. hash table에 key에 해당하는 node가 있는지 확인
        2. 있으면 해당 node를 linked list의 tail로 이동 (remove & add) (hash table은 그대로 둬도 ok)
        3. 없으면 -1 반환
        """
        if key in self.dic:
            node = self.dic[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        1. hash table에 key에 해당하는 node가 있는지 확인
            - 있으면 해당 node를 linked list에서 삭제
        2. 새로운 node 생성
        3. 생성한 node를 linked list와 hash table에 추가/업데이트
        4. hash table의 크기가 capacity를 넘어가는지 확인
            - 넘어간다면, linked list의 head(= least recently used) node와 hash table entry 삭제
        """
        if key in self.dic:
            self._remove(self.dic[key])

        node = Node(key, value)
        self._add(node)
        self.dic[key] = node

        if len(self.dic) > self.capacity:
            least_recently_used = self.head.next
            self._remove(least_recently_used)
            del self.dic[least_recently_used.key]


class LRUCache2:
    """어떤 node를 사용할 때마다 tail에 추가"""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = dict()
        self.next, self.prev = dict(), dict()
        self.head, self.tail = "h", "t"
        self._connect(self.head, self.tail)

    def _connect(self, a, b):
        self.next[a], self.prev[b] = b, a

    def _remove(self, key):
        self._connect(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.dic[key]

    def _add(self, key, value):
        self.dic[key] = value

        self._connect(self.prev[self.tail], key)
        self._connect(key, self.tail)

        if len(self.dic) > self.capacity:
            self._remove(self.next[self.head])

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        value = self.dic[key]
        self._remove(key)
        self._add(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self._remove(key)
        self._add(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
