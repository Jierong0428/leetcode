#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 15:10:52 2020

@author: luojierong
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        a = []
        candidates.sort()
        n = len(candidates)
        ans = []
        def dfs(x,m):
            if m == 0:
                if a not in ans:
                    ans.append(a.copy())
                return
            if x == n or m < candidates[x]:
                return
            
            a.append(candidates[x])
            dfs(x + 1,m - candidates[x])
            a.pop()
            dfs(x + 1, m)
        dfs(0,target)
        return ans