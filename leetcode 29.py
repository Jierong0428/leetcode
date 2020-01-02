#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:18:04 2020

@author: luojierong
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        ans = 0
        for i in range(31,-1,-1):
            x = divisor << i
            if dividend >= x:
                dividend -= x
                ans += 1 << i
            if dividend == 0:
                break
        if neg:
            ans = -ans
        return min(ans,2 ** 31 - 1)
        