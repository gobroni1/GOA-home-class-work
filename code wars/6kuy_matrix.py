# def expansion(matrix, n):
#     for _ in range(n):
#         N = len(matrix)
        
#         # Calculate new column elements (based on sum of rows)
#         new_column = [sum(row) for row in matrix]
        
#         # Calculate new row elements (based on sum of columns)
#         new_row = [sum(matrix[j][i] for j in range(N)) for i in range(N)]
        
#         # Calculate element 'e' (sum of the main diagonal)
#         e = sum(matrix[i][i] for i in range(N))
#         new_row.append(e)
        
#         # Expand the matrix by adding the new column and row
#         for i in range(N):
#             matrix[i].append(new_column[i])
#         matrix.append(new_row)
    
#     return matrix


matrix = [[1,2,3],
          [5,3,8],
          [6,5,4]]

N = len(matrix)
#print([sum(row) for row in matrix])
new_row = [sum(matrix[j][i] for j in range(N)) for i in range(N)]
print(new_row)
for i in range(N):  # Loop over columns
    column_sum = 0
    for j in range(N):  # Loop over rows
        column_sum += matrix[j][i]
        new_row.append(column_sum)
        
#F*** matrix 

import random
import re




