from solve import solve, get_coordinates, get_sq_index
from random import shuffle, randint

def get_random_pos(possibilities):
    nxt = randint(0, len(possibilities)-1)
    return list(possibilities)[nxt]

def generate(square_dim):
    max_num = square_dim*square_dim
    total_num = max_num*max_num

    row_options = []
    col_options = []
    solution = [] 
    for _ in range(max_num):
        row_options.append(set(range(1, max_num+1)))
        col_options.append(set(range(1, max_num+1)))
        solution.append([0]*max_num)

    square_options = []
    for i in range(square_dim):
        square_options.append([])
        for _ in range(square_dim):
            square_options[i].append(set(range(1, max_num+1)))

    def backtracking_search(depth):
        if depth == total_num:
            return True

        row, col = get_coordinates(depth, max_num)
        sq_row, sq_col = get_sq_index(row, col, square_dim)
        possibilities = list(row_options[row] & col_options[col] & square_options[sq_row][sq_col])
        shuffle(possibilities)
        for p in possibilities:
            col_options[col].remove(p)
            row_options[row].remove(p)
            square_options[sq_row][sq_col].remove(p)
            solution[row][col] = p

            res = backtracking_search(depth + 1)
            if res:
                return True

            solution[row][col] = 0
            square_options[sq_row][sq_col].add(p)
            row_options[row].add(p)
            col_options[col].add(p)
        return False

    backtracking_search(0)
    return solution

def mask_numbers(solution, number_of_cells, max_num):
    indices_to_del = [i for i in range(max_num*max_num)]
    shuffle(indices_to_del)
    for i in indices_to_del[:-number_of_cells]:
        row, col = get_coordinates(i, max_num)
        solution[row][col] = 0
    return solution

if __name__ == '__main__':
    square_dim = 4
    res = generate(square_dim)
    # mask 25%
    mask_numbers(res, (square_dim**4)//4, square_dim**2)
    for row in res:
        print(row)
    print('===')
    solution = solve(res, square_dim)
    for row in solution:
        print(row)