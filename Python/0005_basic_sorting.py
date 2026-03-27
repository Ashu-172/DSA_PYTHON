# Implementation of Selection sort:
'''
1. Assume the array has two parts one is sorted and second is unsorted.
2. Initially sorted part will have zero values, all values are in unsorted part.
3. From the last look for the smallest, swap it with 0th index element. size of sorted part is now 1.
4. now repeat this for the remaining unsorted array, swap it with index 1.
5. continue this till only one element remains in the unsorted part, this is largest element.
Complexity: n+(n-1)+(n-2)+.......+0 = n(n+1)/2 = O(n^2)

'''
def selectionSort(arr):
    return do_sort(arr, 0)

def do_sort(arr, i):
    if i==len(arr)-1:
        return arr
    min = i
    for j in range(i, len(arr)):
        if arr[j] < arr[min]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]
    return do_sort(arr, i+1)

# Implementation of Bubble sort:
'''
1. Assume the array as bubbles in water, Bigger bubble will go to the surface first.
2. Iterate over the array and compare each adjecent pair, swap if arr[j] > arr[j+1],
after an iteration, the largest number (biggest bubble) will be places at the end of the array.
3. Since in each iteration one number will be placed in the end of the array, we don't
need iterate over all the numbers in the array on next iteration. Hence the outer loop
should run i=n-1 to 0 (n times) but inner loop should run j=0 to i-1.
Complexity: O(n*(n+1)/2) = O(n^2) like selection sort.
For best effort case (array already sorted) we can add a flag in the outer loop is_swapped=false,
and set it to true if any swap happens in ineer loop. for already sorted array this will 
remain false after the inner loop execution, break the outer loop and return in this case. The 
complexity will be O(n) here.
'''
def bubbleSort(arr):
    for i in range(len(arr)-1, -1, -1): # running loop from n-1 to 0
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Implementation of Insertion sort:
'''
1. select the part of array from left of size 1, insert next element in this array at 
correct place by left shiftiing all large numbers.
2. Now after this insertion, we have array of size 2 sorted.
3. repeat this process with the next element by inserting it at its right place in the 
current array of size 2, after this we'll have sorted array of size 3.
4. Repeat this process for all elements.
Complexity: For worst and avg case complexity will be O(n^2) for best case it will 
be O(n) because no right shift needed if array is already sorted.
'''
def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

# Implementation of Quick sort:
'''
1. In each iteration select a pivot point and place it at its correct place.
2. From the left check for the first number which is larger than the pivot. (index i)
3. From the right check for the first number which is smaller than the pivot. (index j)
4. Swap these values.
5. Repeat these steps till i<j, once this condition breaks and j<i, it means from start to j 
all elements are smaller than pivot and from j+1 to end all elements are larger than pivot.
6. Now swap the element at j with pivot, so that pivot is at its correct place.
6. Now left side of the pivot we have unsorted array of smaller values and on right side
we have unsorted array of larger values. repeat this algorithm for both parts until only
one element remain in the array (i==j).

Complexity: Since we are dividing the array in two parts every time, it'll give O(log n)
and for every time processing all the elements in array the total complexity is O(n log n).

'''
def quickSort(arr):
    doQuickSort(arr, 0, len(arr)-1)
    return arr

def doQuickSort(arr, start, end):
    if start < end:
        p = getPartition(arr, start, end)
        doQuickSort(arr, start, p-1)
        doQuickSort(arr, p+1, end)

def getPartition(arr, start, end):
    pivot, i, j = int((start+end)/2), start, end
    while i<=j:
        while i<=end and arr[i]<=arr[pivot]:
            i+=1
        while j>=start and arr[j]>arr[pivot]:
            j-=1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j

# Implementation of Merge sort:
'''
Merge sort work on divide and conquer concept, we continuously devide the array in two parts until only one element remains in the array and then merge them back while maintaining the order.
1. Divide the array in two half sized arrays (if odd size array, one part will be bigger than the other)
2. Continue it till array size becomes one because single element is always sorted in itself.
3. Now start copying elements from the two parts into a single array in correct order and return the array.
4. Keep merging it similaryly until all sub arrays are merged into one.

Time Complexity: dividing taks O(log n) and merging takes O(n) on each level of the tree. 
Total complexity is O(n log n)
Space complexity: O(n) because we use extra arry to copy the values.
'''
def mergeSort(arr):
    return doMergeSort(arr, 0, len(arr)-1)

def doMergeSort(arr, start, end):
    if start==end:
        return [arr[start]]
    mid = int((start+end)/2)
    left = doMergeSort(arr, start, mid)
    right = doMergeSort(arr, mid+1, end)

    return merge(left, right)

def merge(left, right):
    ret = []
    i, j = 0, 0
    while(i<len(left) and j<len(right)):
        if left[i] <= right[j]:
            ret.append(left[i])
            i+=1
        else:
            ret.append(right[j])
            j+=1
    while(i<len(left)):
        ret.append(left[i])
        i+=1
    while(j<len(right)):
        ret.append(right[j])
        j+=1
    return ret



if __name__ == "__main__":
    print("Enter array to sort: ")
    input_arr = list(map(int, input().split()))
    print(f"Selection Sorted array is {selectionSort(input_arr.copy())}")
    print(f"Bubble Sorted array is {bubbleSort(input_arr.copy())}")
    print(f"Insertion Sorted array is {insertionSort(input_arr.copy())}")
    print(f"Quick Sorted array is {quickSort(input_arr.copy())}")
    print(f"Merge Sorted array is {mergeSort(input_arr.copy())}")

