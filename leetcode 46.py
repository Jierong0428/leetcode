#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:28:08 2020

@author: luojierong
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        judge = [False] * n
        a = []
        ans = []
        def dfs(x):
            if x == n:
                ans.append(a.copy())
                return
            for i in range(n):
                if judge[i] != True:
                    a.append(nums[i])
                    judge[i] = True
                    dfs(x + 1)
                    judge[i] = False
                    a.pop()
        dfs(0)
        return ans