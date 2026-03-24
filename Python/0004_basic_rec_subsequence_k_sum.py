def findKsumSubsequence(seq, k, i, curr):
    if i==len(seq):
        total = sum (int(x) for x in curr)
        return total == k

    curr.append(seq[i])
    res = findKsumSubsequence(seq, k, i+1, curr)
    if res:
        return res
    curr.pop()
    res = findKsumSubsequence(seq, k, i+1, curr)
    return res

if __name__=="__main__":
    seq = input("Enter input to find sub-sequence with sum K: ")
    k = int(input("Enter value for K: "))
    result = []
    findKsumSubsequence(seq, k, 0, result)
    print(f"Subsequence with K sum is {result}")