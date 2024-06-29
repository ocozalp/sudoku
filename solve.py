def get_sq_index(row, col, square_dim):
    return (row // square_dim, col // square_dim)

def get_coordinates(depth, max_num):
    return (depth // max_num, depth % max_num)

def solve(initial_board, square_dim):
    max_num = square_dim*square_dim
    total_num = max_num*max_num
    row_options = []
    col_options = []
    for _ in range(max_num):
        row_options.append(set(range(1, max_num+1)))
        col_options.append(set(range(1, max_num+1)))

    square_options = []
    for i in range(square_dim):
        square_options.append([])
        for j in range(square_dim):
            square_options[i].append(set(range(1, max_num+1)))
    
    for i in range(max_num):
        for j in range(max_num):
            if initial_board[i][j] != 0:
                row_options[i].remove(initial_board[i][j])
                col_options[j].remove(initial_board[i][j])
                sq_row, sq_col = get_sq_index(i, j, square_dim)
                square_options[sq_row][sq_col].remove(initial_board[i][j])
    
    solution = [list(row) for row in initial_board]

    def backtracking_search(depth):
        if depth == total_num:
            return True
        row, col = get_coordinates(depth, max_num)
        if solution[row][col] != 0:
            # already solved this cell, find next
            return backtracking_search(depth + 1)
        # unsolved cell, iterate
        sq_row, sq_col = get_sq_index(row, col, square_dim)
        possibilities = row_options[row] & col_options[col] & square_options[sq_row][sq_col]
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
