#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 17:57:08 2020

@author: luojierong
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix2 = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                matrix2[j][n - 1 - i] = matrix[i][j]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = matrix2[i][j]
            