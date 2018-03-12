def identity(n):
    """
    Return the identity matrix of size n
    :param n: size of the identity matrix to return
    :return: identity matrix represented by a 2 dimensional array of size n*n
    """
    return [[1 if i == j else 0 for i in range(n)] for j in range(n)]


def null(n):
    """
    Return the null matrix of size n
    :param n: size of the null matrix to return
    :return: null matrix represented by a 2 dimensional array of size n*n
    """
    return [[0 for _ in range(n)] for _ in range(n)]


def show(matrix):
    """
    Print the matrix in the console
    :param matrix: a 2 dimensional array
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" " if j != len(matrix[0])-1 else "")
        print("")


def add(a, b):
    """
    Return the result of a+b
    :param a: a 2 dimensional array of numbers
    :param b: a 2 dimensional array of numbers
    :return: a 2 dimensional array of numbers
    """
    return [[a[i][j] + b[i][j] for j in range(len(a[i]))] for i in range(len(a))]


def multiply_matrix_by_matrix(a, b):
    """
    Return result of a*b
    :param a: a 2 dimensional array
    :param b: a 2 dimensional array
    :return: a 2 dimensional array
    """
    c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(c)):
        for j in range(len(c[i])):
            x = 0
            for k in range(len(b[0])):
                x += a[i][k] * b[k][j]
            c[i][j] = x
    return c


def multiply_matrix_by_real(a, real):
    """
    Return result of real*a
    :param a: a 2 dimensional array
    :param real: a real
    :return: a 2 dimensional array
    """
    return [[j*real for j in i] for i in a]


def subtract(a, b):
    """
    Return the result of a+b
    :param a: a 2 dimensional array
    :param b: a 2 dimensional array
    :return: a 2 dimensional array
    """
    return add(a, multiply_matrix_by_real(b, -1))


def delete_row(a, rownumber):
    """
    Return the matrix a without row rownumber
    If rownumber is not correct (between 0 et len(a)-1) the function return the a matrix without modification
    :param a: a 2 dimensional array
    :param rownumber: an int between 0 et len(a)-1
    :return: a 2 dimensional array
    """
    return [[a[i][j] for j in range(len(a[i]))] for i in range(len(a)) if i != rownumber]


def delete_col(a, colnumber):
    """
    Return the matrix a without row colnumber
    If colnumber is not correct (between 0 et len(a[0])-1) the function return the a matrix without modification
    :param a: a 2 dimensional array
    :param colnumber: an int between 0 et len(a[0])-1
    :return: a 2 dimensional array
    """
    return [[a[i][j] for j in range(len(a[i])) if j != colnumber] for i in range(len(a))]


def transpose(a):
    """
    Return the transpose of a
    :param a: a 2 dimensional array
    :return: a 2 dimensional array
    """
    return [[a[j][i] for j in range(len(a[i]))] for i in range(len(a))]


def determinant(a):
    """
    Return the determinant of the matrix a
    :param a: a 2 dimensional array
    :return: a real
    """
    if len(a) == 2:
        return a[0][0]*a[1][1]-a[0][1]*a[1][0]
    else:
        det = 0
        for i, j in enumerate(a[0]):
            det += pow(-1, i) * j * determinant(delete_row(delete_col(a, i), 0))
        return det


def adjugate(a):
    """
    Return the adjugate matrix of a
    :param a: a 2 dimensional array
    :return: a 2 dimensional array
    """
    return [[pow(-1, i+j) * determinant(delete_col(delete_row(a, j), i)) for i in range(len(a))] for j in range(len(a))]
