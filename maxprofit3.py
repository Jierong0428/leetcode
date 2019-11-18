#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 20:33:59 2019

@author: luojierong
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f1 = [0 for i in range(n)]
        f2 = [0 for i in range(n)]
        if not n:
            return 0
        current_min = prices[0]
        current_max = prices[-1]
        for i in range(1,n):
            if prices[i] < current_min:
                current_min = prices[i]
            f1[i] = max(f1[i-1],prices[i] -  current_min)
   
        for i in range(n-2,-1,-1):
            if prices[i] > current_max:
                current_max = prices[i]
            f2[i] = max(f2[i + 1], current_max - prices[i])
        
      
        return max([f1[i] + f2[i] for i in range(n)])
    
            
            
        