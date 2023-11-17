# https://www.acmicpc.net/problem/1991
import sys
input = sys.stdin.readline

N = int(input())
tree = dict()
for _ in range(N):
    curr, left, right = input().split()
    tree[curr] = [left, right]

def preorder(root):
    print(root, end="")    # root
    if (left := tree[root][0]) != ".":
        preorder(left) # left
    if (right := tree[root][1]) != ".":
        preorder(right) # right

def inorder(root):
    if (left := tree[root][0]) != ".":
        inorder(left)  # left
    print(root, end="")    # root
    if (right := tree[root][1]) != ".":
        inorder(right) # right

def postorder(root):
    if (left := tree[root][0]) != ".":
        postorder(left)  # left
    if (right := tree[root][1]) != ".":
        postorder(right)  # right
    print(root, end="")    # root

preorder('A')
print()
inorder('A')
print()
postorder('A')
