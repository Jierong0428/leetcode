#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 16:58:58 2020

@author: luojierong
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        firstrow = False
        for j in range(m):
            if not matrix[0][j]:
                firstrow = True
        for i in range(1,n):
            for j in range(m):
                if not matrix[i][j]:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1,n):
            for j in range(1,m):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        if not matrix[0][0]:
            for i in range(1,n):
                matrix[i][0] = 0
        if firstrow:
            for j in range(m):
                matrix[0][j] = 0