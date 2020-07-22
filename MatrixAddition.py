# Sample Input:  (matrix dimensions followed by each row of the matrix)
# 
# 4 5
# 1 2 3 4 5
# 3 2 3 2 1
# 8 0 9 9 1
# 1 3 4 5 6
# 4 5
# 1 1 4 4 5
# 4 4 5 7 8
# 1 2 3 9 8
# 1 0 0 0 1
# Output:
# 
# 2 3 7 8 10
# 7 6 8 9 9
# 9 2 12 18 9
# 2 3 4 5 7

# Matrix A
a_dimensions = input().split()
a_dimensions[0], a_dimensions[1] = int(a_dimensions[0]), int(a_dimensions[1])
matrix_a, matrix_b, matrix_c = [], [], []
i = 0
while i < a_dimensions[0]:
    string_row = input().split()
    int_row = []
    for element in string_row:
        int_row.append(int(element))
    matrix_a.append(int_row)
    i += 1
# Matrix B
b_dimensions = input().split()
b_dimensions[0], b_dimensions[1] = int(b_dimensions[0]), int(b_dimensions[1])
i = 0
while i < b_dimensions[0]:
    string_row = input().split()
    int_row = []
    for element in string_row:
        int_row.append(int(element))
    matrix_b.append(int_row)
    i += 1
# Add matrices
if a_dimensions != b_dimensions:
    print("ERROR")
else:
    i = 0
    while i < a_dimensions[0]:
        n = 0
        while n < a_dimensions[1]:
            matrix_a[i][n] += matrix_b[i][n]
            n += 1
        i += 1
    for row in matrix_a:
        row_string = ""
        for entry in row:
            row_string = row_string + " " + str(entry)
        print(row_string)
