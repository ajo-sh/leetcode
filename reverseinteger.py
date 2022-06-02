# Runtime: 20 ms, faster than 99.90% of Python3 online submissions for Reverse Integer on date of upload.
# Memory Usage: 13.8 MB, less than 62.88% of Python3 online submissions for Reverse Integer on date of upload.
# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            y=-1*int(str(-x)[::-1]) # Reversing negative integer
        else:
            y=int(str(x)[::-1]) # Reversing positive intiger
        N=2**31
        if y>(N-1) or y<(-N): # Checking for 32-bit integer range
            return 0
        else:
            return y
