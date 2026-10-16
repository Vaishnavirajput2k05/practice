MOD = 10**9 + 7

class Node:
    def __init__(self):
        self.sum_sq = 0
        self.sum_c = 0
        self.lazy = 0
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, n):
        self.root = Node()
        self.n = n

    def push(self, l, r, node):
        if node.lazy == 0:
            return
        
        mid = (l + r) // 2
        if not node.left:
            node.left = Node()
        if not node.right:
            node.right = Node()
            
        lazy = node.lazy
        
        # Update left child
        length_left = mid - l + 1
        node.left.sum_sq = (node.left.sum_sq + 2 * lazy * node.left.sum_c + length_left * lazy * lazy) % MOD
        node.left.sum_c = (node.left.sum_c + length_left * lazy) % MOD
        node.left.lazy = (node.left.lazy + lazy) % MOD
        
        # Update right child
        length_right = r - mid
        node.right.sum_sq = (node.right.sum_sq + 2 * lazy * node.right.sum_c + length_right * lazy * lazy) % MOD
        node.right.sum_c = (node.right.sum_c + length_right * lazy) % MOD
        node.right.lazy = (node.right.lazy + lazy) % MOD
        
        node.lazy = 0

    def update(self, l, r, node, ql, qr):
        if ql <= l and r <= qr:
            length = r - l + 1
            node.sum_sq = (node.sum_sq + 2 * node.sum_c + length) % MOD
            node.sum_c = (node.sum_c + length) % MOD
            node.lazy = (node.lazy + 1) % MOD
            return

        self.push(l, r, node)
        mid = (l + r) // 2
        
        if not node.left:
            node.left = Node()
        if not node.right:
            node.right = Node()
            
        if ql <= mid:
            self.update(l, mid, node.left, ql, qr)
        if qr > mid:
            self.update(mid + 1, r, node.right, ql, qr)
            
        node.sum_sq = (node.left.sum_sq + node.right.sum_sq) % MOD
        node.sum_c = (node.left.sum_c + node.right.sum_c) % MOD

class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        tree = SegmentTree(n)
        last_seen = {}
        total_sum = 0
        
        for i, x in enumerate(nums):
            left = last_seen.get(x, -1) + 1
            tree.update(0, n - 1, tree.root, left, i)
            last_seen[x] = i
            total_sum = (total_sum + tree.root.sum_sq) % MOD
            
        return total_sum
