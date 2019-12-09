#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 22:15:31 2019

@author: luojierong
"""

class Solution:
    def convert(self, s: str, numRows: int):
        n=len(s)
        res=['' for i in range(numRows)]
        if numRows == 1:
            return s
        for i in range(n):
            k=i % (2 * numRows - 2)
            if k<=numRows - 1:
                res[k] += s[i]
            if k >= numRows:
                j = 2 * numRows - 2 - k
                res[j] += s[i]
        
            
        s1=''
        for item in res:
            s1 += item
        return s1