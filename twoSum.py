'''
I will use a hashtable for constant time value accessing and
enumerate will be used to access both index and its element in a list.

example:

nums=[1,2,3,10,32]
for i, num in enumerate(nums):
print(i,num)

0 1
1 2
2 3
3 10
4 32

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize hashtable for constant time lookup
        hashtable = {}
        # For each index and number in the nums list (enumerated)
        for i, num in enumerate(nums):
            # The number we want to find is equal to the target - the first num
            # because that number and our initial number will sum to the target
            potentialMatch = target - num
            # If the potential match is not in the hashtable
            if potentialMatch not in hashtable:
                # Set the number value to its index
                hashtable[num] = i
            else:
                # Return the index of our potential match in the hashtable
                # and the index of 
                return [hashtable[potentialMatch], i]
