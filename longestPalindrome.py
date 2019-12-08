#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 20:14:48 2019

@author: luojierong
"""

class Solution:
    def longestPalindrome(self,s: str) -> str:
        res = ''
        len_s = len(s)
        len_res = 0
        for i in range(len_s):
            halflen_even = min(i,len_s - i - 2)
            for j in range(halflen_even + 1):
                if s[i - j] != s[i + 1 + j]:
                    halflen_even = j - 1
                    break
            if 2 * halflen_even + 2 > len_res:
                res = s[i - halflen_even:i + 1 + halflen_even + 1]
                len_res = 2 * halflen_even + 2
            halflen_odd = min(i,len_s - i - 1)
            for j in range(halflen_odd + 1):
                if s[i - j] != s[i + j]:
                    halflen_odd = j -1
                    break
            if 2 * halflen_odd + 1 > len_res:
                res = s[i - halflen_odd:i + halflen_odd + 1]
                len_res = 2 * halflen_odd + 1
        return res
                    