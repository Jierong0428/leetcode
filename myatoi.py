#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 22:02:21 2019

@author: luojierong
"""

class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.strip()
        if not s: 
            return 0
        res = 0
        positive = True
        if s[0] == '-':
            positive = False
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        for char in s:
            if '0' <= char <= '9':
                res = res * 10 + int(char)
            else:
                break
        if not positive:
            res = -res
        res = min (2**31 - 1,res)
        res = max(-2**31, res)
        return res