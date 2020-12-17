# Binary Search 

# [4, 6, 5, 1, 8, 9] - Best we can we is O(n) for searching
# since there's no order to the order of the elements

# [1, 4, 5, 6, 8, 9] - If our input is sorted, we have 
# more information about the input that we can leverage 
# Target = 8

# [1, 4, 5, { 6, 8, 9 }]
          
# How many comparisons did we actually do? 2 

# 1. We want to narrow down the possible range of 
#    where our target must exist in the sorted array 
# 2. With each comparison, the idea is that we split 
#    the range in half.
# 3. Find the midpoint index of the current range
# 4. Compare the element at the midpoint index against 
#    the target
# 5. Depending on the result of the comparison:
#        - the midpoint element is our target 
#        - the midpoint element < target 
#        - the midpoint element > target 

# Since we're cutting the range in half on each 
# iteration, the runtime is logarithmic 
def binary_search(arr, target, left, right):
    '''
    Input: An array of numbers, target is a number
    Output: Int, the index of the target in the array 
    if we find it, or -1 if we don't find it 
    '''
    # base case(s)? 
    # 1. we found the thing, return its index 
    # 2. we looked through our entire sorted array 
    #    and didn't find the thing, return -1 
    # how do we ensure that our code eventually gets to 
    # a base case? 
    # on each recursive call, we'll have split the range 
    # of possible numbers in half 
    
    # as long as there are elements left in our range
    # we'll keep searching 
    if left <= right:
        # calculate the midpoint 
        midpoint = (right + left) // 2

        if arr[midpoint] == target:
            return midpoint
            
        if arr[midpoint] < target:
            # this means that our target, if it exists
            # in the array, has to be on the right 
            # side of the midpoint 
            # we can toss out the left side of our range 
            # update our left pointer to be midpoint + 1
            return binary_search(arr, target, midpoint + 1, right)

        else:
            # our target, if it exists in the array, has to 
            # be on the left side of the midpoint 
            # we can toss out the right side of our range
            # update our right pointer to be midpoint - 1
            return binary_search(arr, target, left, midpoint - 1)

    return -1
    
print(binary_search([1, 4, 5, 6, 8, 9], 9, 0, 5))



