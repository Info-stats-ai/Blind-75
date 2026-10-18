class Solution:
    def countBits(self, n: int) -> list[int]:
        res =[]
        for i in range(n+1):
            count = 0
            tmp = i
            while tmp : 

                tmp= tmp & (tmp-1)
                count += 1
            res.append(count)
        return res



