def get_dimensions(nth_matrix=""):
    if nth_matrix == "":
        dimensions = input("Enter size of matrix: > ").split()
    else:
        dimensions = input(f"Enter size of {nth_matrix} matrix: ").split()
    return [int(dimensions[0]), int(dimensions[1])]


def get_matrix(rows, nth_matrix=""):
    i = 0
    input_matrix = []
    if nth_matrix == "":
        print("Enter matrix:")
    else:
        print(f"Enter {nth_matrix} matrix:")
    return_int = True
    while i < rows:
        string_row = input("").split()
        float_row = []
        for element in string_row:
            if '.' in element:
                return_int = False
            float_element = float(element)
            float_row.append(float_element)
        input_matrix.append(float_row)
        i += 1
    if return_int:
        i = 0
        while i < rows:
            n = 0
            while n < len(input_matrix[i]):
                input_matrix[i][n] = int(input_matrix[i][n])
                n += 1
            i += 1
    return input_matrix


def print_matrix(output_matrix):
    print("The result is:")
    for row in output_matrix:
        row_string = ""
        for entry in row:
            row_string = row_string + str(entry) + " "
        print(row_string)


def add_matrices(a_dimensions=[], a_matrix=[], b_dimensions=[], b_matrix=[]):
    # Add matrices
    if a_dimensions != b_dimensions:
        print("The operation cannot be performed.")
    else:
        i = 0
        while i < a_dimensions[0]:
            n = 0
            while n < a_dimensions[1]:
                a_matrix[i][n] += b_matrix[i][n]
                n += 1
            i += 1
        print_matrix(a_matrix)


def scale_matrix(a_dimensions, a_matrix, scalar_constant):
    i = 0
    while i < a_dimensions[0]:
        n = 0
        while n < a_dimensions[1]:
            a_matrix[i][n] *= scalar_constant
            n += 1
        i += 1
    print_matrix(a_matrix)

# a_dimenions[0] = rows a_dimensions[1] = columns
#ERROR IN MATRIX MULTIPLIER
def multiply_matrices(a_dimensions=[], a_matrix=[], b_dimensions=[], b_matrix=[]):
    # print("Matrix A")
    # print_matrix(a_matrix)
    # print("Matrix B")
    # print_matrix(b_matrix)
    c_matrix = []
    if a_dimensions[1] != b_dimensions[0]:
        print("The operation cannot be performed.")
    else:
        # create an empty results matrix
        i = 0
        while i < a_dimensions[0]:
            c_matrix.append([])
            n = 0
            while n < b_dimensions[1]:
                c_matrix[i].append(0)
                n += 1
            i += 1

        # Multiply matrices
        i = 0
        while i < a_dimensions[0]:
            n = 0
            while n < b_dimensions[1]:
                # row will correspond to i in matrix a
                c, result = 0, 0
                execution_walkthrough = ""
                for number in a_matrix[i]:
                    # column will correspond to n in matrix b
                    result += a_matrix[i][c] * b_matrix[c][n]
                    # execution_walkthrough += f"{a_matrix[i][c]} * {b_matrix[c][n]}"
                    # if c < a_dimensions[0]:
                    #     execution_walkthrough += " + "
                    # print(f"{execution_walkthrough} = {result}")
                    c += 1
                c_matrix[i][n] = result
                n += 1
            i += 1
        print_matrix(c_matrix)


running = True
state = "select action"
while running:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("0. Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        # add
        matrix_a_dimensions = get_dimensions("first")
        matrix_a = get_matrix(matrix_a_dimensions[0], "first")
        matrix_b_dimensions = get_dimensions("second")
        matrix_b = get_matrix(matrix_b_dimensions[0], "second")
        # add_matrices(a_dimensions=[], a_matrix=[], b_dimensions=[], b_matrix=[])
        add_matrices(matrix_a_dimensions, matrix_a, matrix_b_dimensions, matrix_b)
    elif choice == 2:
        # scale
        matrix_dimensions = get_dimensions()
        matrix = get_matrix(matrix_dimensions[0])
        constant = float(input("Enter constant: "))
        # scale_matrix(a_dimensions, a_matrix, scalar_constant)
        scale_matrix(matrix_dimensions, matrix, constant)
    elif choice == 3:
        # multiply
        matrix_a_dimensions = get_dimensions("first")
        matrix_a = get_matrix(matrix_a_dimensions[0], "first")
        matrix_b_dimensions = get_dimensions("second")
        matrix_b = get_matrix(matrix_b_dimensions[0], "second")
        multiply_matrices(matrix_a_dimensions, matrix_a, matrix_b_dimensions, matrix_b)
    elif choice == 0:
        running = False
        break
    # elif choice == 5:
    #     # check implicit float to int conversion
    #     matrix_dimensions = get_dimensions()
    #     matrix = get_matrix(matrix_dimensions[0])
    #     print_matrix(matrix)




