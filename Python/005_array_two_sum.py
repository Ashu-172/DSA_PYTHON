'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they
add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
    2 <= nums.length <= 104
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9

'''
# Solution 1: Brute force
# Using two loops O(n^2)
def findTwoSum1(arr, k):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == k:
                return [i,j]
    return []

# Solution 2:
'''
nums = [2,11,7,15], target = 9
1. since arr[i] + x = k is true, x = k - arr[i]
2. create a map of arr[i] as key and i as value.
3. now in a loop for each i, calculate x and see if x is already present in the map,
this means if the pair number is already passed. this is O(1) operation.
4. If present, retrun [i],map[x], if not present, add arr[i], i in the map
5. Time complexity = O(n), space complexity = O(n)
'''
def findTwoSum2(arr, k):
    mapping = {}
    for i in range(len(arr)):
        x = k-arr[i]
        if mapping.get(x) is not None:
            return [i, mapping[x]]
        mapping[arr[i]]=i
    return []

if __name__ == "__main__":
    print("Enter input array: ")
    in_arr = list(map(int, input().split()))
    k = int(input("Enter sum value K: "))
    print(f"Two numbers from input {in_arr} with sum k={k} is {findTwoSum1(list(in_arr), k)}")
    print(f"Two numbers from input {in_arr} with sum k={k} is {findTwoSum2(list(in_arr), k)}")
