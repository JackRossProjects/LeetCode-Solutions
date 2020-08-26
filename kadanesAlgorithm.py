'''
Write a function that takes in an array of integers and then returns the
max sum that can be made by summing a subarray of only adjacent numbers of the input array.

Example:
array = [-10, -2, -9, -4, -8, -6, -7, -1, -3, -5]
Output: -1

def kadanesAlgorithm(array):
  # Base case || 0th index is the largest subarray
	maxEndingHere = array[0]
	maxSoFar = array[0]
  # For each number in the array AFTER the base case
	for num in array[1:]:
    # Update variables
		maxEndingHere = max(num, maxEndingHere + num)
		maxSoFar = max(maxSoFar, maxEndingHere)
  # Return maximum sum
	return maxSoFar
