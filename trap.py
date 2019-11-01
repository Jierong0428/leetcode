#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:59:01 2019

@author: luojierong
"""
class Solution:
    def trap(self, height):
        n=len(height)
        ans=0
        stack=[]
        for i in range(n):
            while stack!=[] and height[stack[-1]]< height[i]:
                top=stack[-1]
                stack.pop()
                if  stack!=[]:
                    distance=i-stack[-1]-1
                    bound_height=min(height[stack[-1]],height[i])-height[top]
                    ans+=bound_height*distance
            stack.append(i)
        return ans
                    
                        
                   
        