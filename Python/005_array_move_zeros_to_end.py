'''
Given an integer array nums, move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''
# Solution: Two pointer solution:
# Keep the slow pointer on first 0 in current array and fast pointer on next 
# positive element. swap values on these pointer and increment slow pointer.
def moveZeros(arr):
    i=0
    for j in range(len(arr)):
        if arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    return arr

if __name__=="__main__":
    print("Enter input array: ")
    nums = list(map(int, input().split()))
    print(f"array with all zeros moved to end: {moveZeros(nums.copy())}")