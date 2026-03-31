'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Given an integer array nums sorted in non-decreasing order, remove the 
duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k After removing 
duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted
order. The remaining elements beyond index k - 1 can be ignored.

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

# Slow and Fast pointer solution
def removeDuplicates(nums: List[int]) -> int:
    i,j = 0,1
    while j<len(nums):
        if nums[i] < nums[j]:
            i+=1
            nums[i], nums[j] = nums[j], nums[i]
        j+=1
    return i+1

if __name__=="__main__":
    print("Enter input array: ")
    nums = list(map(int, input().split()))
    k = removeDuplicates(nums)
    print(f"array after removal of duplicates: {nums[:k]}")
