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

"""You are given a 0-indexed integer array nums.

The distinct count of a subarray of nums is defined as:

Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.

Since the answer may be very large, return it modulo 109 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.
Example 2:

Input: nums = [2,2]
Output: 3
Explanation: Three possible subarrays are:
[2]: 1 distinct value
[2]: 1 distinct value
[2,2]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105"""
