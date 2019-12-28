#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 17:36:02 2019

@author: luojierong
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1, p2 = head, head
        for i in range(n + 1):
            p2 = p2.next
            if i < n and p2 == None:
                return p1.next
        while p2 != None:
            p1, p2 = p1.next, p2.next
        p1.next = p1.next.next
        return head
        