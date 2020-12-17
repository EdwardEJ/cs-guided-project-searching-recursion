def iter_search(arr, target):
    ''' 
    Input: array of things, target will the thing we're
    searching for 
    Output: int, the index of the element that we found 
    in the array or -1 if we didn't find it 
    ''' 
    for i, thing in enumerate(arr): # O(n)
        # base case 1: we found our thing 
        if thing == target:
            return i
    # base case 2: we traversed the entire array 
    # and we didn't find the thing
    return -1
    
# O(n) time 
# A recursive search function 
def rec_search(arr, target):
    ''' 
    Input: array of things, target will the thing we're
    searching for 
    Output: int, the index of the element that we found 
    in the array or -1 if we didn't find it 
    ''' 
    # base case 1: we traversed the entire array 
    # and we didn't find the thing
    # another we can think about this is if our 
    # input array was empty to begin with 
    if len(arr) == 0:
        return -1
    # base case 2: we find our target in the array 
    # we're going to check the last element in the 
    # array and see if it matches our target 
    if arr[-1] == target:
        return len(arr) - 1
    # what are we missing at this point? 
    # what if we aren't in one of these two situations?
    # the "iteration" step, or, how we move closer to 
    # a base case 
    arr.pop()
    return rec_search(arr, target)

'''
rec_search([4, 6, 5, 1, 8, 9], 100)
rec_search([4, 6, 5, 1, 8], 100)
rec_search([4, 6, 5, 1], 100)
rec_search([4, 6, 5], 100)
rec_search([4, 6], 100)
rec_search([4], 100)
rec_search([], 100) => -1 
'''

# print("Iterative search: ", iter_search(arr, target))
# print("Recursive search: ", rec_search(arr, target))

def fibonacciSimpleSum2(n):
    fib = [0,1] # The Fibonacci sequence starts with 0 and 1 every time. Because of that we will start an array with the first 2 indices whose values are 0 and 1.
    for i in range(2,n+1): ## Now we are going to imitate the Fib sequence but first we need to start with the 3rd number in the sequence and stop one more than the number of the parameter (n) so that we can have everything except the first two number 0 and 1
        seq = fib[i-1] + fib[i-2] ###Here is the way the Fib seq works. the sum of the number -1 plus the number -2
        fib.append(seq) #### Now you take that sequence and append it to the 0 and 1 in the list
        if seq >= n:
            break ### Finally you want to stop at the number given
    for j in fib: # For each number in that Fib sequence
        if n-j in fib: ## If the number minus each number is in the sequence, then it must be a Fibonacci number
            return True
    return False