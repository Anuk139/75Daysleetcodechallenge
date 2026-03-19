class Solution(object):
    def isPalindrome(self, s):
        c=""
        for ch in s:
            if ch.isalnum():
               c+=ch.lower() 
        return c==c[::-1]