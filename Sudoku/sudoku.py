import itertools
import functools
def generate_permutations(elems):
    return list(itertools.permutations(elems))

def generate_combinations(permutations):
    return list(map(list, list(itertools.combinations(permutations,4))))

def is_valid(row):
    return sorted(row)==list(range(1,5))

def test_matrix(matrix):
    check_rows = [is_valid(row) for row in matrix]
    check_columns = [is_valid([matrix[i][j] for i in range(0,4)]) for j in range(0,4)]
    check_first_sub = is_valid(matrix[0][0:2] + matrix[1][0:2])
    check_second_sub = is_valid(matrix[0][2:4] + matrix[1][2:4])
    check_third_sub = is_valid(matrix[2][0:2] + matrix[3][0:2])
    check_forth_sub = is_valid(matrix[2][2:4] + matrix[3][2:4])
    return not(False in check_rows) and not(False in check_columns) and not check_first_sub and not check_second_sub and not check_third_sub and not check_forth_sub

def sudoku():
    matrixes = generate_combinations(generate_permutations(range(1,5)))
    matrixes = sorted(sum([list(generate_permutations(elem)) for elem in matrixes],[]))
    i = 0
    while i < len(matrixes) :
        if test_matrix(matrixes[i]):
            yield matrixes[i]
        i+=1
