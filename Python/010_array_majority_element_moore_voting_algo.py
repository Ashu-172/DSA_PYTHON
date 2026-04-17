'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
    n == nums.length
    1 <= n <= 5 * 10^4
    -10^9 <= nums[i] <= 10^9
    The input is generated such that a majority element will exist in the array.
'''

# Solution 1: Using Hash map
'''
1. Create a Hashmap to store the count of each element.
2. Iterate over the input array and increment the count for it in the map.
3. If the count of any element becomes greated than n/2, return the element.

Time complexity: O(n)
Space complexity: O(n) => Map size can be n/2 if except majority element, all elements are different.
'''
def findMajorityElement(nums):
    counter = {}
    for n in nums:
        c = counter.get(n, 0)
        counter[n] = c+1
        if counter[n]>len(nums)/2:
            return n

# Solution 2: Moore's Voting algorithm
'''
Concept: If a majority element exists, it will survive elimination when paired against different elements.
    Since the majority element will apprear more then n/2 times in the array, if we pair it with all remaining
    other elements and cancel it out, we'll still have at least one occurrance of it remaining in the array.

1. Select first number as current majority element candidate.
2. Iterate over the loop and increment the counter for it when it appears and decrement the counter when any
    other element appears to cancel it out.
3. When the counter becomes 0, it means till the current index no element has majority all appearances of the
    majority element has been cancelled out. Here pick the current index element as new candidate and continue
    step 2.
4. In the end all elements will be cancelled out and counter will remain a positive number, that candiate
    will be the majority element.

Time complexity: O(n)
Space Complexity: O(1)
'''
def mooreVotingAlgo(nums):
    candidate = nums[0]
    counter = 0
    for n in nums:
        if counter == 0:
            candidate = n
        if n == candidate:
            counter+=1
        else:
            counter-=1
    return candidate


if __name__ == "__main__":
    print("Enter input array: ")
    nums = list(map(int, input().split()))
    print(f"The Majority Number is: {findMajorityElement(nums)}")
    print(f"The Majority Number is: {mooreVotingAlgo(nums)}")