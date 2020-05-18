#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 00:19:49 2020

@author: luojierong
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        le = 1
        re = n 
        while le <= re:
            mid = le + (re - le) // 2
            if not guess(mid):
                return mid
            elif guess(mid) == 1:
                le = mid + 1
            else:
                re = mid - 1
        return -1 