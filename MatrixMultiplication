# Matrix A
# a_dimensions = ['2', '2']#input().split()
a_dimensions = input().split()
a_dimensions[0], a_dimensions[1] = int(a_dimensions[0]), int(a_dimensions[1])
matrix_a, matrix_b, matrix_c = [], [], []
i = 0
while i < a_dimensions[0]:
    # string_row = ['1', '1']#input().split()
    string_row = input().split()
    int_row = []
    for element in string_row:
        int_row.append(int(element))
    matrix_a.append(int_row)
    i += 1
# Matrix B
# b_dimensions = ['2', '2']#input().split()
b_dimensions = input().split()
b_dimensions[0], b_dimensions[1] = int(b_dimensions[0]), int(b_dimensions[1])
i = 0
while i < b_dimensions[0]:
    # string_row = ['1', '1']#input().split()
    string_row = input().split()
    int_row = []
    for element in string_row:
        int_row.append(int(element))
    matrix_b.append(int_row)
    i += 1

if a_dimensions[0] != b_dimensions[1]:
    print("ERROR")
else:
    # create an empty results matrix
    i = 0
    while i < a_dimensions[0]:
        matrix_c.append([])
        n = 0
        while n < b_dimensions[1]:
            matrix_c[i].append(0)
            n += 1
        i += 1
    # Multiply matrices
    i = 0
    while i < a_dimensions[0]:
        n = 0
        while n < b_dimensions[1]:
            #row will correspond to i in matrix a
            c, result = 0, 0
            for number in matrix_a[i]:
                #column will correspond to n in matrix b
                result += matrix_a[i][c] * matrix_b[n][c]
                c += 1
            # result = "result of row from a time column from b"
            matrix_c[i][n] = result
            # matrix_a[i][n] += matrix_b[i][n]
            n += 1
        i += 1

    # print matrix
    for row in matrix_c:
        row_string = ""
        for entry in row:
            row_string = row_string + " " + str(entry)
        print(row_string)
