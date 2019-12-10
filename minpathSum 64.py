#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:20:42 2019

@author: luojierong
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [0 for i in range(n + 1)]
        for i in range(m):
            if i == 0:
                for j in range(1,n + 1):
                    dp[j] = dp[j - 1] + grid[i][j - 1]
            else:
                for j in range(1,n + 1):
                    if j == 1:
                        dp[j] += grid[i][j - 1]
                    else:
                        dp[j] = min(dp[j - 1],dp[j]) + grid[i][j - 1]
        return dp[-1]