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
scalar = int(input())
# scale matrix by constant
i = 0
while i < a_dimensions[0]:
    n = 0
    while n < a_dimensions[1]:
        matrix_a[i][n] *= scalar
        n += 1
    i += 1
for row in matrix_a:
    row_string = ""
    for entry in row:
        row_string = row_string + str(entry) + " "
    print(row_string)
