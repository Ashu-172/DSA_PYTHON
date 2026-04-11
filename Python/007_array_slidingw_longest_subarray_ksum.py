'''
Given an array arr[] containing integers and an integer k, your task is to
find the length of the longest subarray where the sum of its elements is
equal to the given value k. If there is no subarray with sum equal to k,
return 0.

Examples:

Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
Output: 6
Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6.

Input: arr[] = [-5, 8, -14, 2, 4, 12], k = -5
Output: 5
Explanation: Subarrays with sum = -5 are [-5] and [-5, 8, -14, 2, 4]. The length of the longest subarray with a sum of -5 is 5.

Input: arr[] = [10, -10, 20, 30], k = 5
Output: 0
Explanation: No subarray with sum = 5 is present in arr[].
'''

# Solution 1: when elements of array are positive numbers
'''
eg: 10 5 2 7 1 9  k=15
1. maintain two pointers i and j and initialize sum with 0.
2. if sum is less than k, add value at j to the sum and increment j
3. if sum is greater than k, deduct value at i from sum and increment i
4. if sum is equal to k, current size of sliding window is of sum k,
    set len = max(len, j-i), Here not using j-i+1 because sum is calculated 
    first then j is already incrementet.
Note: This solution works only if numbers are positive. if negative numbers
      are included, then step 3 won't give correct results because incrementing j
      can also reduce sum back to k.
'''
def getKsumArrayLen(arr, k):
    i,j = 0,0
    sum = 0
    l = 0
    while i<=j and j<len(arr):
        if sum == k:
            l = max(l, j-i)
            sum+=arr[j]
            j+=1
        elif sum>k:
            sum-=arr[i]
            i+=1
        elif sum<k:
            sum+=arr[j]
            j+=1
    return l

# Solution 2:
'''
1. maintain an index i and a hashmap for pair index,sum of values from index 0 to i.
2. Increment i and calculate current sum from 0 to i and store it in map where key is sum.
3. check if the current sum - k is already present in the map. if it is present and index is j
   then it means that sum of values between index i and j is equal to k.
4. calculate max length as len = max(len, new_idx-old_idx)
5. length of first k sum wiil not be coved by above steps, to cover that set l = max(l, i+1)
   where sum till i is equals to k.
6. Above steps will cover the cases with positive values, but if array contains negative
   values also, then we need to make sure that for the same sum value, map is not updated.
'''
def getLenKsumArray(arr, k):
    mapping = {}
    l=0
    sum=0
    for idx in range(len(arr)):
        sum+=arr[idx]
        if sum == k:
            l = max(l, idx+1)
        old_idx = mapping.get(sum-k)
        if old_idx is not None:
            l = max(l, idx-old_idx)
        # Add in map only once for a sum, never update in order to handle zeros and negatives.
        if mapping.get(sum) is None: 
            mapping[sum]=idx
    return l

if __name__=="__main__":
    print("Enter the input array: ")
    arr = list(map(int, input().split()))
    k = int(input("Enter sum k: "))
    print(f"Length of the longest sub-array with k sum is: {getKsumArrayLen(arr, k)}")
    print(f"Length of the longest sub-array with k sum is: {getLenKsumArray(arr, k)}")
