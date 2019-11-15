#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 14:33:40 2019

@author: luojierong
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = len(coins)
        n = amount
        f = [0] + [n + 1 for i in range(n)]
        
        for i in range(m):
            for j in range(coins[i] ,n + 1):
                f[j] = min(f[j] , f[j - coins[i]] + 1)
        if f[n] == n+1:
            return -1
            
        return f[n]
        