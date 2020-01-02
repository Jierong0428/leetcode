#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 20:37:25 2020

@author: luojierong
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p1, p2 = head, head.next
        while True:
            p1.next = p2.next
            p2.next = p1
            if p1 == head:
                head = p2
            if p1.next and p1.next.next:
                temp = p1. next
                p1.next = temp.next
                p1 = temp
                p2 = p1.next
            else:
                break
        return head
            
        
        