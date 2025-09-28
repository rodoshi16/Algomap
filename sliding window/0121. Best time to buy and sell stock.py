def maxProfit(prices: list[int]) -> int:
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



    Example 1:

    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
    Example 2:

    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.


    Constraints:

    1 <= prices.length <= 105
    0 <= prices[i] <= 104

    Time complexity: 0(n)
    Space complexity: 0(1)

    Thought process: Iterate through and track lowest price seen,
    at every price calc profit and return the max as needed

    """

    #naive solution -> brute force

    max_profit = 0
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit

    return max_profit



#solution2: slice the list from i+1 to find the max selling price
def maxProfit2(prices: list[int]) -> int:
    """

    Another naive solution where you would think




    """




    max_profit = 0

    for i in range(len(prices) -1):
        max_sell = max(prices[i+1:])
        profit = max_sell - prices[i]
        if profit > max_profit:
            max_profit = profit

    return max_profit









