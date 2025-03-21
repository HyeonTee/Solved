import sys
input = sys.stdin.readline


def solve(board):
    row_mask = [0] * 9
    col_mask = [0] * 9
    box_mask = [0] * 9
    blanks = []

    def get_box_index(r, c):
        return (r // 3) * 3 + (c // 3)

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == 0:
                blanks.append((r, c))
            else:
                bit = 1 << (num - 1)
                row_mask[r] |= bit
                col_mask[c] |= bit
                box_mask[get_box_index(r, c)] |= bit

    def backtrack(index):
        if index == len(blanks):
            return True

        r, c = blanks[index]
        b = get_box_index(r, c)

        used = row_mask[r] | col_mask[c] | box_mask[b]
        available = (~used) & 0x1FF

        while available:
            pick = available & -available
            num = (pick.bit_length() - 1) + 1

            row_mask[r] |= pick
            col_mask[c] |= pick
            box_mask[b] |= pick
            board[r][c] = num

            if backtrack(index + 1):
                return True

            board[r][c] = 0
            row_mask[r] ^= pick
            col_mask[c] ^= pick
            box_mask[b] ^= pick

            available ^= pick

        return False

    backtrack(0)


def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

sudoku = []
for _ in range(9):
	row = list(map(int, input().split()))
	sudoku.append(row)

solve(sudoku)
print_board(sudoku)