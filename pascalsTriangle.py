'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        # List of rows that we will return
        rows = []
        
        # First and second row edge cases - always [1] and [1,1] respectivly
        for i in range(numRows):
            # First row
            if i == 0:
                rows.append([1])
            # Second row
            elif i == 1:
                rows.append([1,1])
            # General case rows
            else:
                # New row MUST start with 1
                new_row = [1]
                
                # Middle value in row will be equal to its row index - 1
                middle_number_count = i - 1
                
                for j in range(middle_number_count):
                    # Column index will be middle value of row + 1
                    col_index = j + 1
                    # Previous row will be set to the last element in rows[]
                    prev_row = rows[-1]
                    # The new value will be the sum of its parent above and to the left
                    value = prev_row[col_index] + prev_row[col_index - 1]
                    # Add that value to new row
                    new_row.append(value)
                # Last value in row MUST be 1
                new_row.append(1)
                # Add the new row to the list of rows
                rows.append(new_row)
        # Return Pascals's Triangle
        return rows
