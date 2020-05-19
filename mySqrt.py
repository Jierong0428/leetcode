#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 17:11:48 2020

@author: luojierong
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        le = 1
        re = x - 1
        while re >= le:
            mid = le + (re - le) // 2
            if mid > x / mid:
                re = mid - 1
            elif mid + 1 > x / (mid + 1):
                return mid
            else:
                le = mid + 1
                