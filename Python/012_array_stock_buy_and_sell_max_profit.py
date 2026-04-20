'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different
day in the future to sell that stock.
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

    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^4

'''
# Solution 1 and 2:
'''
If we visualize a graph for the given array of stock prices, there will be upward and downward
price trends. To make profit we only need to focus on upward trends if we see the graph from 
the left (start of the array). If we look at the array from the end, we need to focus on the
downward trends.
So we have two ways to implement this:

Solution 1:
1. Iterate over the array from the start and maintain a variable min to maintain minimum variable.
2. Now calculate price difference for each upcoming price with the min, and if this diff is maximum till
    now then update the maxDiff variable.
3. Note that each dip in the graph will update the min variable if the price is lesser then the previous min
    and the diff we are calculating is for the upcoming prices (from next day onward) so we'll only get profit.
    The trends from low to high are in focus in this solution.

Time Complexity: O(n) => Iterating only one time.
Space Complexity: O(1)

Solution 2:
1. Iterate over the array from the end and maintain a variable max to maintain maximum variable.
2. Now calculate the difference for each upcoming element (from back side traversal) with the max, if this diff
    is maximum till now then update the maxDiff variable.
3. Here each top in the graph will update the max variable if the price is greated than the previous max and
    the diff will be calculated for each upcoming prices (from previous day onward) so we'll only get profit.
    The trends from High to low are in focus in this solution.

Time Complexity: O(n) => Iterating only one time.
Space Complexity: O(1)
'''
def getMaxProfitFromStocks1(prices):
    low = float('Inf')
    maxDiff = 0
    for p in prices:
        if p<low:
            low = p
        if p-low > maxDiff:
            maxDiff=p-low
    return maxDiff

def getMaxProfitFromStocks2(prices):
    high = 0
    maxDiff = 0
    for i in range(len(prices)-1, -1, -1):
        if prices[i]>high:
            high = prices[i]
        if high-prices[i]>maxDiff:
            maxDiff = high-prices[i]
    return maxDiff


# Solution 3: (Using Kadane's Algorithm)
'''
Here we want to calculate the max profit, so if we calculate the price difference of each day in a seperate array,
Then we'll have a array with profits and losses between consecutive days. By doing this we'll basically convert 
it into a max sum subarry problem which can be solved by Kadane's algorithm.

Time Complexity: O(2n) => O(n)
Space Complexity: O(n-1) =>O(n)
'''
def maxProfitKadane(prices):
    profit = [0]*(len(prices)-1) # One less size
    for i in range(0, len(prices)-1):
        profit[i] = prices[i+1]-prices[i]
    
    cMax=0
    gMax=0
    for x in profit:
        cMax += x # current Maximum
        if cMax > gMax: # Update global maximum
            gMax = cMax
        if cMax<0: # if current max becomes negative, reset to 0 to start freshly for max profit.
            cMax=0
    return gMax

if __name__ == "__main__":
    print("Enter input array (stock prices): ")
    nums = list(map(int, input().split()))
    print(f"The max profit from the stock is: {getMaxProfitFromStocks1(nums)}")
    print(f"The max profit from the stock is: {getMaxProfitFromStocks2(nums)}")
    print(f"The max profit from the stock is: {maxProfitKadane(nums)}")