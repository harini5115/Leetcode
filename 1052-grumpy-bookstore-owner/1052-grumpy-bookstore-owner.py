class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        might_miss = 0
        for i in range(minutes):
            might_miss += customers[i] * grumpy[i]
        max_might_miss = might_miss
        for i in range(minutes, n):
            might_miss += customers[i] * grumpy[i]
            might_miss -= customers[i - minutes] * grumpy[i - minutes]
            max_might_miss = max(max_might_miss, might_miss)
        happy_customers = max_might_miss
        for i in range(n):
            happy_customers += customers[i] * (1 - grumpy[i])
        return happy_customers      