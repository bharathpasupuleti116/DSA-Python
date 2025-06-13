# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

# Examples:

# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.

# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.

# Input: arr[] = [10, 10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 and the second largest element does not exist.

# Constraints:
# 2 ≤ arr.size() ≤ 105
# 1 ≤ arr[i] ≤ 105

# Expected Complexities
# Time Complexity: O(n)
# Auxiliary Space: O(1)

def getSecondLargest(arr):
        
        if (len(arr) < 2):
            return -1
        
        largest = -1
        
        for i in range(len(arr)):
            
            if (arr[i] > largest):
                
                second_largest = largest
                largest = arr[i]   

            elif (arr[i] > second_largest and arr[i] != largest):
                
                second_largest = arr[i]

            print(f"iteration(i): {i}, \n largest = {largest}, \n second_largest = {second_largest}\n---------------------------------------")
        
        return second_largest

arr = [12, 35, 1, 10, 34, 106, 45]

print(getSecondLargest(arr))


