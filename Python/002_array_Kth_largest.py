
# Solution 
# Kth smallest: In quick sort, check if the partition index is K-1 and return value if true.
# Kth largest: compare partition with n-k where N is the length of the array.
def findKthLargest(arr, k):
    return quickSelect(arr, k-1, 0, len(arr)-1)

def quickSelect(arr, k, start, end):
    if start<=end:
        p = partition(arr, start, end)
        if p==k:
            return arr[k]
        res = quickSelect(arr, k, start, p-1)
        if res == -1:
            res = quickSelect(arr, k, p+1, end)
        return res
    return -1

import random
def partition(arr, start, end):
    # Pivot should be selected randomly and swapped with start or end value
    p = random.randrange(start, end)
    arr[start], arr[p] = arr[p],arr[start]
    pivot,i, j = start, start, end
    while i<=j:
        while (i<=end and arr[i]<=arr[pivot]):
            i+=1
        while (j>=start and arr[j]>arr[pivot]):
            j-=1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[pivot] = arr[pivot], arr[j]
    return j

if __name__=="__main__":
    print("Enter Array input: ")
    arr = list(map(int, input().split()))
    k = int(input("Enter value of k: "))
    print(f"Kth largest number in arrar is {findKthLargest(arr, k)}")