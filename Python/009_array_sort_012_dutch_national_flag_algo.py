'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that
objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
    n == nums.length
    1 <= n <= 300
    nums[i] is either 0, 1, or 2.
'''

# Solution 1:
'''
1. Create an array of size 3 to count the occurrence of 0, 1 and 2.
2. Iterate over the input array and increment the related counter.
3. Now iterate over the counter array and fill the input array with 0s, 1s and 2s in order.

Time Complexity: O(n) => two separate for loops
Space Complexity: O(1) => fixed size array for counters
'''
def sortArray(nums):
    counter = [0]*3
    for n in nums:
        counter[n]+=1
    
    j=0 # Pointer for the result array
    for i in range(3):
        while counter[i]:
            nums[j] = i
            j+=1
            counter[i]-=1
    return nums

# Solution 2
'''
1. Maintain 3 pointers, low, mid and high where low represents 0, mid represents 1 and high represents 2.
2. We'll move mid as the running pointer. so low and mid will be at 0th index and high will be at the end.
3. If value at mid is 0, swap with low and increment low and mid.
4. If value at mid is 1, no operation needed just increment mid.
5. If value at mid is 2, swap with high and decrement high, here don't incremnt mid because high could
    be 0 or 1, so we again need to process it in next iteration.
Note: step 3 we are also incrementing mid because we are sure that it can be only 0 or 1 where 
    we can safely increment mid, it can not be 2 after the swap because if it were, it would
    have already got swapped with high.

Time Complexity: O(n) => Single iteration
Space Complexity: O(1) => just using 3 pointers

'''
def dutchNationalFlag(nums):
    low, mid = 0,0
    high = len(nums)-1

    # Since we are sorting and mid is representing 1s, mid can not go higher than high pointer.
    while mid<=high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low+=1
            mid+=1
        elif nums[mid] == 1:
            mid+=1
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high-=1           
    return nums

if __name__ == "__main__":
    print("Enter input array: ")
    nums = list(map(int, input().split()))
    print(f"Sorted array of 0,1 and 2 is {sortArray(nums.copy())}")
    print(f"Sorted array of 0,1 and 2 is {dutchNationalFlag(nums.copy())}")
