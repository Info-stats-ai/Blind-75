
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0              # base case: 0 coins to make amount 0

        for i in range(1, amount + 1):      # every amount 1 to n
            for coin in coins:              # try every coin
                if coin <= i:               # coin can't exceed amount
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
        