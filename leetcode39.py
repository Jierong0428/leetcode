#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:53:34 2020

@author: luojierong
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        a = []
        ans = []
        candidates.sort()
        n = len(candidates)
        def dfs(x,m):
            if m == 0:
                ans.append(a.copy())
                return
            if x == n or m < candidates[x]:
                return
            a.append(candidates[x])
            dfs(x,m - candidates[x])
            a.pop()
            dfs(x + 1,m)
        dfs(0,target)
        return ans
            