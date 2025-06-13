# check if array is sorted or not ?

# Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false

# Examples:

# Input: arr[] = [10, 20, 30, 40, 50]
# Output: true
# Explanation: The given array is sorted.

# Input: arr[] = [90, 80, 100, 70, 40, 30]
# Output: false
# Explanation: The given array is not sorted.

# Constraints:
# 1 ≤ arr.size ≤ 10^6
# - 10^9 ≤ arr[i] ≤ 10^9

# Expected Complexities
# Time Complexity: O(n)
# Auxiliary Space: O(1)

def arraySortedOrNot(arr):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True

def Optimal(arr1):
     return all(arr1[i] < arr1[i + 1] for i in range(len(arr) - 1))

arr = [10, 20, 30, 40, 50]

arr1 = [90, 80, 100, 70, 40, 30]

print(arraySortedOrNot(arr))

print(Optimal(arr1))

