'''
Given an array arr[] of integers, determine the Next Greater Element (NGE) for every element
in the array, maintaining the order of appearance.

The Next Greater Element for an element x is defined as the first element to the right of x in
the array that is strictly greater than x.
If no such element exists for an element, its Next Greater Element is -1.

Examples: 

    Input: arr[] = [1, 3, 2, 4]
    Output: [3, 4, 4, -1]
    Explanation: The next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4, since it doesn't exist, it is -1.

    Input: arr[] = [6, 8, 0, 1, 3]
    Output: [8, -1, 1, 3, -1]
    Explanation: The next larger element to 6 is 8, for 8 there is no larger elements hence it is -1, for 0 it is 1 ,
    for 1 it is 3 and then for 3 there is no larger element on right and hence -1.
'''

# Solution using brute force:
'''
1. using nested loop we can find next greater element.
2. outer loop will run for each element.
3. inner loop will run from i+1 till end of the array.

Complexity: O(n^2)
'''

# Solution using stack
'''
Identification: Since bruteforce approach gives O(n^2) complexity and j is dependent on i (outer loop index),
it is most likely to be solved using Stack.
1. Because we are looking for next greater value on the right, we'll start processing elements from the right side.
2. Check if the stack has any element, if present then check if its greater then the current input element.
3. If top < current, pop the top element. continue doing that untill we find larger element or stack becomes empty.
    3.1 if we find larger element, put it into the result array.
    3.2 if stack becomes empty, put -1 in the result array since there is no greater element on the right.
4. If the element is greater, then put it in the result array.
5. If stack is empty, put -1 in the result array.

Time Complexity: O(n) => traversal is happening only once.
Space Complexity: O(n) => size of the stack can be n.
'''

def find_next_ngr(input):
    s = []
    n = len(input)
    res = [-1]*n
    for i in range(n-1, -1, -1):
        if len(s) == 0:
            res[i] = -1
        elif s[-1] > input[i]:
            res[i] = s[-1]
        else:
            while len(s)>0 and s[-1]<=input[i]:
                s.pop()
            if len(s)==0:  
                res[i] = -1
            else:
                res[i] = s[-1]
        s.append(input[i])

    return res
            
    
