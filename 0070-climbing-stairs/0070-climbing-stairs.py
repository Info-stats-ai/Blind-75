class Solution:
    def climbStairs(self, n: int) -> int:
        fb1 , fb2 = 1 , 1
        for i in range(1, n):
            temp =fb1 
            fb1 = fb1+ fb2
            fb2 = temp 
        return fb1


        