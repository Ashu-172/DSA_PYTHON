'''
Given an integer array nums, find the with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
'''

# Solution 1: Kadane's algorithm
'''
Intution:
1. Negative sum is harmful → drop it
2. Positive sum → keep extending
3. Always carry the best subarray (Max sum)

Algorithm:
1. We start by initializing two variables: maxSum and currentSum.
    a. maxSum represents the maximum sum encountered so far and is initially set to the minimum
        possible integer value to ensure that any valid subarray sum will be greater than it.
    b. currentSum represents the current sum of the subarray being considered and is initially set to 0.

2. We iterate through the nums array using a for loop, starting from the first element and going up to the last element.
3. For each element in the array, we add it to the current sum currentSum. This calculates the sum of the subarray
    ending at the current element.
4. Next, we check if the current sum currentSum is greater than the current maximum sum maxSum.
    If it is, we update maxSum with the new value of currentSum. This means we have found a new maximum subarray sum.

5. If the current sum currentSum becomes negative, it indicates that including the current element in the subarray
    would reduce the overall sum. In such cases, we reset currentSum to 0. This effectively discards the current
    subarray and allows us to start a fresh subarray from the next element.
6. We repeat steps 3 to 5 for each element in the array.
7. After iterating through the entire array, the variable maxSum will contain the maximum subarray sum encountered.

Time Complexity: O(n)
Space Complexity: O(1)
'''
def findMaxSumSubarray(nums):
    gMax = float('-inf')
    cMax = 0
    for n in nums:
        cMax+=n
        if cMax>gMax:
            gMax = cMax
        if cMax<0:
            cMax=0
    return gMax

if __name__ == "__main__":
    print("Enter input array: ")
    nums = list(map(int, input().split()))
    print(f"The sum of max subarray is: {findMaxSumSubarray(nums)}")