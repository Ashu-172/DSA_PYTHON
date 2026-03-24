# Solution 1:  O(2^n * n) => 
# 2^n is because for eah char we have 2 choices (include and not include) 
# n is for concatination loop (sol 1) or join method (sol 2).
'''
Example: 123
1. Take first char out and calculate the sub-sequences of remaining string.
    1, substring(23)
2. Now add the char to the result since it itself is a sub-sequence,
    res = [1]
3. add returned sub-sequences of the substring to the result set.
    res = [1, 2, 3, 23]
4. concatenate the previously removed char to all returned subsequesnces
   to get the remaining sub-sequences and add it to the result.
    res = [1, 2, 3, 23, 12, 13, 123]
5. Base condition will be the case when only one char is present in the substring, return it as it is.
'''
def getSubsequence(seq, i, j):
    if i==j:
        return [seq[i]]

    ret = getSubsequence(seq, i+1, j)
    res = [str(seq[i])+x for x in ret]
    res.append(seq[i])
    res.extend(ret)
    return res

    '''
    [123], 0, 2
    ret = [123], 1, 2
          ret = [123], 2, 2
          ret = [3]
          res = [2][3] = [23]
          res = [23, 2, 3]
    ret = [23, 2, 3]
    res = [1][23, 2, 3] = [123, 12, 13]
    res = [123, 12, 13, 1, 23, 2, 3]
    complexity = O(n+n-1+n-2+n-3....) because of the for loop running n, n-1, n-2 etc times
               = O(n*(n+1)/2) = O(n^2)
    '''

# Solution 2:
'''
1. For example subsequence for 123 is [123, 12, 13, 23, 1, 2, 3]
Here if we observe we are making a choice on each char, where to include it in the sequence or not include it.
2. Include 1st char in the sequence and call the funcion for the remaining string.
3. Don't include the first char in the sequence and call the function for the remaining string.
3. When index reached to the last character, add the current sequence to the list of the sub-sequences.
'''
def getSubsequence2(seq, i, res, curr):
    if i>=len(seq):
        res.append("".join(curr))
        # res.append(curr.copy())
        return
    
    curr.append(seq[i])
    getSubsequence2(seq, i+1, res, curr)
    curr.pop()
    getSubsequence2(seq, i+1, res, curr)



if __name__=="__main__":
    seq = input("Enter string to get sub sequences: ")
    print(f"List of sub-sequences for the given string {seq} is {getSubsequence(list(seq), 0, len(seq)-1)}")
    result = []
    getSubsequence2(list(seq), 0, result, [])
    print(f"List of sub-sequences for the given string {seq} is {result}")
