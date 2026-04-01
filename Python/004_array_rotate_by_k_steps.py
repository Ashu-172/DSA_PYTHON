'''
Given an integer array nums, rotate the array to the right by k steps,
where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

'''
def rotateByK1(nums, k):
    n = len(nums)
    # To eliminate unnecessary shifts if k is larger than n, k= k%n
    # example: k=7 n=2, there will be 6 unnecessary shift, final result will be equal to k=1
    k=k%n
    # copy last k elements in temporary array
    temp=[]
    for i in range (n-k, n):
        temp.append(nums[i])
    # shift starting n-k elements by k steps
    for i in range (n-k-1, -1, -1):
        nums[i+k] = nums[i]
    # copy elements from temporary array to starting of the original array
    for i in range (len(temp)):
        nums[i] = temp[i]
    return nums

def rotateByK2(nums, k):
    n = len(nums)
    # To eliminate unnecessary shifts if k is larger than n, k= k%n
    # example: k=7 n=2, there will be 6 unnecessary shift, final result will be equal to k=1
    k = k%n 
    reverse(nums, 0, n-1) # 1. Reverse complete array
    reverse(nums, 0, k-1) # 2. Reverse first k elements in array
    reverse(nums, k, n-1) #3. Reverse remaining n-k elements in array
    return nums

def reverse( nums, start, end):
    while start<end:
        nums[start], nums[end] = nums[end], nums[start]
        start+=1
        end-=1

if __name__=="__main__":
    print("Enter input array: ")
    nums = list(map(int, input().split()))
    k = int(input("Enter K steps to rotate: "))
    print(f"array after removal of duplicates: {rotateByK1(nums.copy(), k)}")
    print(f"array after removal of duplicates: {rotateByK2(nums.copy(), k)}")