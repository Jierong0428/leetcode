#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 22:35:50 2020

@author: luojierong
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        if not n:
            return []
        m = len(matrix[0])
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        direction = 0 if m > 1 else 1
        visited = []
        for i in range(n):
            visited.append([False] * m)
        x, y = 0, 0
        ans = [matrix[x][y]]
        visited[x][y] = True
        while True:
            nx = x + dx[direction]
            ny = y + dy[direction]
            if not (0 <= nx < n) or not (0 <= ny < m) or visited[nx][ny]:
                break
            while 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                x, y = nx, ny
                visited[x][y] = True
                ans.append(matrix[x][y])
                nx = x + dx[direction]
                ny = y + dy[direction]
            direction = (direction + 1) % 4
        return ans
        
            