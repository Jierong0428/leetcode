#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 17:26:43 2020

@author: luojierong
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        a = []
        ans = []
        candidates.sort()
        candidates2 = []
        used = []
        n = len(candidates)
        for i in range(n):
            if candidates[i] not in candidates2:
                candidates2.append(candidates[i])
                used.append(1)
            else:
                index = candidates2.index(candidates[i])
                used[index] += 1
                
        n1 = len(candidates2)        
        def dfs(x,m):
            if m == 0:
                ans.append(a.copy())
            if x == n1 or m < candidates2[x]:
                return
            if used[x]:
                a.append(candidates2[x])
                used[x] -= 1
                dfs(x,m - candidates2[x])
                used[x] += 1
                a.pop()
            dfs(x + 1,m)
        dfs(0,target)
        return ans