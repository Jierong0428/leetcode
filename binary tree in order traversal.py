#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 11:25:58 2020

@author: luojierong
"""

#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        current = root
        res = []
        stack = []
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack[-1]
            res.append(stack[-1].val)
            del stack[-1]
            current = current.right
        return res
        