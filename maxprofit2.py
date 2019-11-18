#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 19:58:30 2019

@author: luojierong
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        i = 0
        ans = 0
        while i < n - 1:
            if  prices[i + 1] > prices[i]:
                ans += prices[i + 1] - prices[i]
            i += 1
        return ans
            