'''
Given two nodes p and q in a binary tree where each node has a pointer to its parent, find their lowest common ancestor (LCA).

The lowest common ancestor of two nodes p and q is the lowest node in the tree that has both p and q as descendants (a node can be a descendant of itself).

'''


class Node:
    def __init__(self, val: int, left: 'Node' = None, right: 'Node' = None, parent: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def lowestCommonAncestor(p: 'Node', q: 'Node') -> 'Node':
        a, b = p, q
        while a != b:
            a = a.parent if a else q
            b = b.parent if b else p
        return a