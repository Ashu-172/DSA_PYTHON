# 1. Sum of first N numbers
def printSumTillN(n):
    if n==0:
        return n
    return n+(printSumTillN(n-1))

def printSumParameterizedRec(n, sum):
    if n==0:
        return sum
    return printSumParameterizedRec(n-1, sum+n)

def getFactorial(n):
    if n==1:
        return 1
    return n*getFactorial(n-1)

def checkPalidrome(str, i):
    if i >= len(str)/2:
        return True
    if str[i] != str[len(str)-1-i]:
        return False
    else:
        return checkPalidrome(str, i+1)

def printFibonacci(length):
    fibonacci = [0,1]
    calculateFibonacci(fibonacci, length)
    return fibonacci

def calculateFibonacci(fibonacci, length):
    n = len(fibonacci)
    if n >= length:
        return
    next = fibonacci[n-2] + fibonacci[n-1]
    fibonacci.append(next)
    return calculateFibonacci(fibonacci, length)

# Find Nth febonacci element
def printFibonacciAtN(n):
    if n<=1:
        return n
    else:
        return printFibonacciAtN(n-1)+printFibonacciAtN(n-2)

def reverseArray(arr, i):
    n=len(arr)
    if i>=n/2:
        return "".join(arr)
    arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
    return reverseArray(arr, i+1)

if __name__ == "__main__":
    n = int(input("Enter number to calculate sum/factorial: "))
    print(f"Sum of {n} is {printSumTillN(n)}")
    print(f"Sum of {n} with parameterized rec is {printSumParameterizedRec(n, 0)}")

    print(f"Factorial of {n} is {getFactorial(n)}")

    str_input = input("Enter string to check if it a palindrome: ")
    print(f"Given string {str_input} is {'not ' if not checkPalidrome(list(str_input), 0) else ''}a Palindrome")
    print(f"Reverse of given string {str_input} is {reverseArray(list(str_input), 0)}")

    length = int(input("Enter max length of fibonacci series: "))
    print(f"Fibonacci series of length {length} is {printFibonacci(length)}")
    print(f"The {length} febonacci element is {printFibonacciAtN(length)}")