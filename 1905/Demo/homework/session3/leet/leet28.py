# Leet code problem 28 Find the index of First Occurance in a string
# Given two strings needle and haystack, 
# return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

import re

def strStrFind(haystack, needle):
    return haystack.find(needle)

def strStrLoop(haystack, needle):
    ln = len(needle)
    for i in range(len(haystack)-ln+1):
        if haystack[i:i+ln] == needle:
            return i
    return -1

def strStrRegEx(haystack, needle):
    match = re.search(needle, haystack)
    if match:
        return match.start()
    else:
        return -1

strStr = strStrFind
strStr = strStrLoop
strStr = strStrRegEx

haystack = "sadbutsad"
needle = "sad"
ret = strStr(haystack, needle)
print(f'first occurance of {needle} in {haystack} is {ret}')

haystack = "leetcode"
needle = "leeto"
ret = strStr(haystack, needle)
print(f'first occurance of {needle} in {haystack} is {ret}')
