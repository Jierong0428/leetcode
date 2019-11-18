#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 19:43:41 2019

@author: luojierong
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        current_min=prices[0]
        max_profit=0
        n=len(prices)
        for i in range(n):
            max_profit=max(max_profit,prices[i]-current_min)
            current_min=min(current_min,prices[i])
        return max_profit
        