#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 13:40:52 2019

@author: luojierong
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [0 for i in range(n + 1)]
        decision = [['' for i in range(n)] for j in range(m) ]
        for i in range(m):
            if i == 0:
                for j in range(1,n + 1):
                    dp[j] = dp[j - 1] + grid[i][j - 1]
                    if j > 1:
                        decision[i][j - 1] = 'r'
            else:
                for j in range(1,n + 1):
                    if j == 1:
                        dp[j] += grid[i][j - 1]
                        decision[i][j - 1] = 'd'
                    else:
                        dp[j] = min(dp[j - 1],dp[j]) + grid[i][j - 1]
                        if dp[j - 1] < dp[j]:
                            decision[i][j - 1] = 'r'
                        else:
                            decision[i][j - 1] = 'd'
        strategy = []
        i,j = m - 1, n - 1
        while i > 0 or j > 0:
            if decision[i][j] == 'd':
                strategy.append('d')
                i -= 1
            else:
                strategy.append('r')
                j -= 1
        strategy.reverse()
        print(strategy)
        return dp[-1]
            
        