#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 17:20:48 2019

@author: luojierong
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = amount 
        m = len(coins)
        f = [1] + [0 for i in range(n)]
        for i in range(m):
            for j in range(coins[i],n + 1):
                f[j] += f[j - coins[i]]
        return f[n]
                