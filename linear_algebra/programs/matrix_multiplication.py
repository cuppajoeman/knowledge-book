def multiply_matrices(matrix_A, matrix_B):
  """
  Given two matrices, we compute the matrix multiplication of the two of them

  Supposing that matrix_A is MxN and that matrix_B is NxK
  then the resulting matrix is M x K (1)
  """

  transpose_matrix_B = transpose_matrix(matrix_B)

  num_rows_of_matrix_A = len(matrix_A) # This is M
  num_columns_of_matrix_A = len(matrix_A[0]) #This is N

  num_rows_of_matrix_B = len(matrix_B) #this is N
  num_columns_of_matrix_B = len(matrix_B[0])# This is K

  resulting_matrix = []

  #initialize the matir xto be all zeros
  # then we will fill in the entries with the correct values
  for i in range(num_rows_of_matrix_A):
    blank_row = []
    for j in range(num_columns_of_matrix_B):
      blank_row.append(0)
    resulting_matrix.append(blank_row)
  # Notice that the matrix now has dimenisions `num_rowsof_matrix_A` x `num_columns_of_matrix_B`
  # Or equivalently M x K , as we noted by  (1)

  for row_index in range(num_rows_of_matrix_A):
    for column_index in range(num_rows_of_matrix_B):
      row_from_matrix_A = matrix_A[row_index]
      transposed_column_from_matrix_B = transpose_matrix_B[column_index]
      resulting_matrix[row_index][column_index] = dot_product(row_from_matrix_A, transposed_column_from_matrix_B)

  return resulting_matrix


def transpose_matrix(matrix):
  """Given a matrix turn it into a new matrix where it's rows are equal to it's columns"""
  rows = len(matrix)
  columns = len(matrix[0]) # assuming matrix is non-empty
  
  transpose_matrix = []
  for i in range(columns):
    temp_new_row = []
    for j in range(rows):
      temp_new_row.append(matrix[j][i])
    transpose_matrix.append(temp_new_row)
  
  return transpose_matrix



def dot_product(v1, v2): 
  dot_product = 0
  for i in range(len(row)):
    dot_product += v1[i] * v2[i]
  return dot_product


