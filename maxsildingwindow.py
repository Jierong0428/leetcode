#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:11:05 2019

@author: luojierong
"""

class Solution:
    def maxSlidingWindow(self, nums,k):
        ans=[]
        n=len(nums)
        a=[0]*n
        head=0
        tail=0
        for i in range(k-1):
            while head<tail and nums[i]>nums[a[tail-1]]:
                tail-=1
            a[tail]=i
            tail+=1
        for i in range(k-1,n):
            
            while head<tail and nums[i]>nums[a[tail-1]]:
                tail-=1
            a[tail]=i
            tail+=1
            while head<tail and a[head]<a[tail-1]-3:
                head+=1
            ans.append(nums[a[head]])
        return ans
            
        