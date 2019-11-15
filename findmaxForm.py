#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 17:48:43 2019

@author: luojierong
"""

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        c = []
        w = []
        for item in strs:
            c.append(item.count('0'))
            w.append(item.count('1'))
        l = len(strs)
        f = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(l):
            for j in range(m,c[i] - 1,-1):
                for k in range(n,w[i] - 1,-1):
                    f[j][k] = max(f[j][k],f[j - c[i]][k - w[i]] + 1)
        return f[m][n]
    