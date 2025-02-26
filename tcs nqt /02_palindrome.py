class Solution:
    def isPalindrome(self, n):
        k = str(n)
        return k == k[::-1]
