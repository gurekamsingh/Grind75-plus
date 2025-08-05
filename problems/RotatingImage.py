# Problem: Rotate Image: You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# Do not allocate another 2D matrix and do the rotation.

# Refer to the matrix 4x4 as an example
class Solution:   
    def rotate(self, matrix: int) -> None:
        n = len(matrix)
        l = 0 
        r = len(matrix) - 1
        
        while l < r:
            for i in range(r-l):
                top = l
                bottom = r
                # save the topleft
                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1

# Example usage:
matrix = [
    [1, 2, 3],  
    [4, 5, 6],
    [7, 8, 9]
]
Solution().rotate(matrix)
print(matrix)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

# Time Complexity: O(n^2) where n is the number of rows (or columns) in the matrix. Each element is moved once.
# Space Complexity: O(1) as we are modifying the matrix in-place without using any additional space.
# This approach uses a layer-by-layer rotation, moving elements from one position to another in a clockwise manner.
        

