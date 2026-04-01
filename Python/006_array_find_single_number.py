'''
Given a non-empty array of integers nums, every element appears
twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity 
and use only constant extra space.

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

'''
# Add numver to a set on first occurrance and remove it on second occurrance.
# In the end only single value will remain in the set.
# Time Complexity = O(n)
# Space complexity = O(n/2) = O(n) because each number is present twice.
def findSingle1(nums):
    s = set()
    for num in nums:
        if num not in s:
            s.add(num)
        else:
            s.remove(num)
    return next(iter(s))

# xor all the numbers, XOR of same number will result in 0 andXOR of 0 and 
#any number x will result in x. Sine all numbers are present twice they 
# will result in 0 after doing XOR and XOR of 0 and remaining single value 
# will remain as the result which will be the number itself.
# Time Complexity = O(n)
# Space Complexity = O(1)
def findSingle2(nums):
    res = 0
    for num in nums:
        res = res^num
    return res

if __name__=="__main__":
    print("Enter input array: ")
    nums = list(map(int, input().split()))
    print(f"Element with single occurrence: {findSingle1(nums.copy())}")
    print(f"Element with single occurrence: {findSingle2(nums.copy())}")