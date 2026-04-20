'''
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive
and negative integers.

You should return the array of nums such that the array follows the given conditions:
    a. Every consecutive pair of integers have opposite signs.
    b. For all integers with the same sign, the order in which they were present in nums is preserved.
    c. The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do 
not satisfy one or more conditions.  

Example 2:

Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].

Constraints:

    2 <= nums.length <= 2 * 10^5
    nums.length is even
    1 <= |nums[i]| <= 10^5
    nums consists of equal number of positive and negative integers.

'''
# Solution 1
'''
1. Create two arrays for positive and negative numbers.
2. Iterate over the input array and copy positive and negative numbers in respective arrays.
3. Copy the positive and negative values from the arrays to result arrar in correct order based
    on odd and even indexing.
Time Complexity: O(n)
Space Complexity: O(n)
'''
def rearrangeNumbers1(nums):
    p = []
    n = []

    for x in nums:
        if x>0:
            p.append(x)
        else:
            n.append(x)
    for i in range(len(nums)):
        if i%2==0:
            nums[i]=p[int(i/2)]
        else:
            nums[i]=n[int(i/2)]
    return nums

# Solution 2:
'''
Above solution can be optimised by creating a single array and copying values in correct order
directly using two pointers p and n for tracking positive and negative numbers in the result array.
1. initialize p with 0 and n with 1 to mark isitial positions for positive and negative numbers.
2. iterate over input array and if the number is positive, place it at index p in res array and increment
    p by 2 and if the number is negative, place it at index n in res array and increment n by 2.

Time Complexity: O(n)
Space Complexity: O(n)
'''
def rearrangeNumbers2(nums):
    res = [0]*len(nums)
    p,n=0,1
    for x in nums:
        if x>0:
            res[p] = x
            p+=2
        else:
            res[n]=x
            n+=2
    return res

# Solution 3: (Not maintaining Order)
'''
If we don't need to maintain the order then it can be done O(1) space complexity.
1. Create two pointers p=0 and n=1.
2. Iterate over the array and check below conditions:
    a. If index is odd and number is positive, increment p by 2.
    b. If index is even and number is negative, increment n by 2.
    c. If both conditions are not met, it means both the numbers are not in correct place, swap p and n.
'''
def rearrangeNumbersUnordered(nums):
    p,n = 0,1
    while n<len(nums) and p<len(nums):
        if nums[p]>0:
            p+=2
        elif nums[n]<0:
            n+=2
        else:
            nums[p], nums[n] = nums[n], nums[p]
    return nums


if __name__ == "__main__":
    print("Enter input array: ")
    nums = list(map(int, input().split()))
    print(f"The rearranged array is: {rearrangeNumbers1(nums.copy())}")
    print(f"The rearranged array is: {rearrangeNumbers2(nums.copy())}")
    print(f"The rearranged array is: {rearrangeNumbersUnordered(nums.copy())}")