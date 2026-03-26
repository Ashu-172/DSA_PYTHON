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
5. Repeat these steps until i<j, once this condition breaks, pivot will be at its right place.
6. Now left side of the pivot we have unsorted array of smaller values and on right side
we have unsorted array of larger values. repeat this algorithm for both parts until only
one element remain in the array (i==j).

Complexity: Since we are dividing the array in two parts every time, it'll give O(log n)
and for every time processing all the elements in array the total complexity is O(n log n).
'''

def quickSort(arr, start, end):
    pivot = 0
    i,j = start, end
    while (i<=j):
        while (arr[i]<=arr[pivot]):
            i+=1
        while (arr[j]> arr[pivot]):
            J-=1
        arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[pivot] = arr[pivot], arr[j]
    quickSort(arr, start, j-1)
    quickSort(arr, j+1, end)
    

if __name__ == "__main__":
    print("Enter array to sort: ")
    input_arr = list(map(int, input().split()))
    print(f"Selection Sorted array is {selectionSort(input_arr.copy())}")
    print(f"Bubble Sorted array is {bubbleSort(input_arr.copy())}")
    print(f"Insertion Sorted array is {insertionSort(input_arr.copy())}")

