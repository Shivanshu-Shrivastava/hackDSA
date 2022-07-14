#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'getNode' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER positionFromTail
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def getNode(llist, positionFromTail):
    i=1
    prev=None
    curr = llist
    length = 1
    
    while curr.next:
        
        length+=1
        curr = curr.next
    print(length,'length1')
    
    length-=positionFromTail
    print(length,'length')
    while i!=length and llist:
        llist = llist.next
        i+=1
    return llist.data
        
    # return prev.data
    # i=0
    # prev=None
    # current = llist
    
    # while current:
        # nxt = curr.next
        # print(nxt.data,'nxt')
        # curr.next = prev
        # prev = curr
        # print(prev.data,'prev')
        # 1 2 3 4

        # curr = curr.next
        # next = current.next

        # current.next = prev
       
        # prev = current
        # print(prev.data,'prev')

        # current = next
        # print(current.data,'curr')
    # llist  = prev
    
    # return llist
    # Write your code here

tests = int(input('testt--'))

for tests_itr in range(tests):
    llist_count = int(input('count ---'))

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input('item---'))
        llist.insert_node(llist_item)

    position = int(input('positio==='))

    result = getNode(llist.head, position)
    print(result)