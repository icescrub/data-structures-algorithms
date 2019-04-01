"""
coin change prob
0-1 knapsack
unbounded knapsack
edit distance
Longest common subseq (LCS)
longest incr subseq (LIS)
longest palindrome subseq (LPS)
TSP (iterative AND recursive)
min weight perfect matching (graph prob)

exec(open('/home/duchess/Desktop/dp').read())
values = [60,100,120]
weights = [10,20,30]
capacity = 50
knapsack(values, weights, capacity)

"""

def knapsack(values, weights, capacity):
    """
    Decision version of knapsack is NP-complete, but we can achieve pseudopolynomial time complexity with DP implementation.

    For each of n items: item i --> (values[i], weights[i]). Return the maximum value of items that doesn't exceed capacity.
    """

    def knapsack_helper(values, weights, w, m, i):
        """Return maximum value of first i items attainable with weight <= w.
 
        m[i][w] will store the maximum value that can be attained with a maximum
        capacity of w and using only the first i items
        This function fills m as smaller subproblems needed to compute m[i][w] are
        solved.
 
        value[i] is the value of item i and weights[i] is the weight of item i
        for 1 <= i <= n where n is the number of items.
        """

        if m[i][w] >= 0:
            return m[i][w]

        if i == 0:
            q = 0
        elif weights[i] <= w:
            decide_NO = knapsack_helper(values, weights, w, m, i-1)
            decide_YES = knapsack_helper(values, weights, w-weights[i]) + values[i], m, i-1)
            q = max(decide_NO, decide_YES)
        else:
            q = decide_NO

        m[i][w] = q
        return q
    
    table = [[-1]*(capacity + 1) for _ in range(len(values))]

    return knapsack_helper(values, weights, capacity, table, len(values)-1)
