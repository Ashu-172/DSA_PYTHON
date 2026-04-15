
'''
Given two sorted arrays nums1 and nums2, return an array that contains the
union of these two arrays. The elements in the union must be in ascending order.
The union of two arrays is an array where all values are distinct and are 
present in either the first array, the second array, or both.

Example 1
Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]
Output: [1, 2, 3, 4, 5, 7]
Explanation:
The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2

Example 2
Input: nums1 = [3, 4, 6, 7, 9, 9], nums2 = [1, 5, 7, 8, 8]
Output: [1, 3, 4, 5, 6, 7, 8, 9]
Explanation:
The element 7 is common to both, 3, 4, 6, 9 are from nums1 and 1, 5, 8 is from nums2
'''


# Solution 1: Without using any hash based data structure
'''
1. Run the loop over the arrays and put smaller number in the result array.
2. To avoid adding duplicate values in result, check if last element in the result
    array is same, if it is same then just increemnt i or j without adding value in result array.
3. Once this loop is over, it means either arr1 or arr2 has been completely covered, not iterate
    over the remaining array and add non-duplicate values to result array like step 2.

Time Complexity: O(n1+n2)
Note: We can use set based solution, putting all the values in the set and then 
converting it into array but it'll not preserve the order of the values. To get
sorted order we need to do the sorting which will take O(nlogn) much slower than
the current sulution.
'''
def getUnion(nums1, nums2):
    ret = []
    i,j=0,0
    while i<len(nums1) and j<len(nums2):
        if nums1[i] <= nums2[j]:
            if len(ret)==0 or ret[len(ret)-1] != nums1[i]:
                ret.append(nums1[i])
            i+=1
        else:
            if len(ret)==0 or ret[len(ret)-1] != nums2[j]:
                ret.append(nums2[j])
            j+=1
        
    while i<len(nums1):
        if len(ret)==0 or ret[len(ret)-1] != nums1[i]:
            ret.append(nums1[i])
        i+=1

    while j<len(nums2):
        if len(ret)==0 or ret[len(ret)-1] != nums2[j]:
            ret.append(nums2[j])
        j+=1

    return ret

if __name__=="__main__":
    print("Enter the 1st input array: ")
    arr1 = list(map(int, input().split()))
    print("Enter the 2nd input array: ")
    arr2 = list(map(int, input().split()))
    print(f"Union of the given arrays: {getUnion(arr1, arr2)}")