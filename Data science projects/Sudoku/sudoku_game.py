import time
import sys

# Increase recursion limit for deep backtracking searches
# Default is often 1000, which might be too low for complex Sudoku puzzles.
sys.setrecursionlimit(2000)


class Sudoku:
    """
    Implements a Sudoku game board and a brute-force backtracking solver.
    """

    def __init__(self, mode="normal"):
        self.mode = mode
        if mode == "test":
            self.game_board = self._generate_test_puzzle()
        else:
            self.game_board = self._generate_starting_puzzle()

        self.is_game_over = False
        # Store the initial state to prevent players from changing pre-filled cells
        self.initial_board = [row[:] for row in self.game_board]

    # --- Board Generation ---
    def _generate_test_puzzle(self):
        # A board that is complete except for one cell (4 is missing at row 0, col 2)
        # This is for testing the 'You Won!' condition quickly.
        return [
            [5, 3, 0, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]

    def _generate_starting_puzzle(self):
        # A standard, moderately difficult Sudoku starting puzzle (0 represents an empty cell)
        return [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

    # --- Display Function ---

    def print_board(self, title="Current Board"):
        print(f"\n--- {title} ---")
        print("    0 1 2 | 3 4 5 | 6 7 8")
        print("  -------------------------")
        for i, row in enumerate(self.game_board):
            if i % 3 == 0 and i != 0:
                print("  -------------------------")

            row_str = f"{i} | "
            for j, cell in enumerate(row):
                if j % 3 == 0 and j != 0:
                    row_str += "| "

                # Replace 0 with '-' for display
                display_value = str(cell) if cell != 0 else "-"
                row_str += display_value + " "

            print(row_str.strip())
        print("  -------------------------")

    # --- Player Move Handling (Used only in human play modes) ---

    def take_player_move(self):
        try:
            player_input = input("Enter move (row col value, e.g., 0 2 4): ").split()
            if len(player_input) != 3:
                raise ValueError("Requires exactly 3 inputs.")

            r, c, val = map(int, player_input)

            if not (0 <= r <= 8 and 0 <= c <= 8 and 1 <= val <= 9):
                print("Error: Row and column must be 0-8, value must be 1-9.")
                return

            # Prevent overwriting initial numbers
            if self.initial_board[r][c] != 0:
                print("Error: Cannot overwrite an initial pre-filled number.")
                return

            # Temporarily try the move, restoring the original value if invalid.
            original_val = self.game_board[r][c]
            self.game_board[r][c] = val

            # Check if the move makes the entire board invalid *at that position*
            if not self._is_safe(r, c, val):
                # Backtrack: Restore the original value and report error
                self.game_board[r][c] = original_val
                print(f"Error: Placing {val} at ({r}, {c}) violates Sudoku rules.")
                return

            # If valid, the board is already updated (by setting self.game_board[r][c] = val)

        except ValueError as e:
            print(f"Input Error: {e}. Please enter three integers separated by spaces.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # --- Validation Helpers for both Player and AI ---

    def _is_safe(self, r, c, val):
        """Checks if placing 'val' at (r, c) on the current board is valid."""

        # 1. Check Row (ensures 'val' is not already in the row, excluding the cell being checked)
        for col in range(9):
            if col != c and self.game_board[r][col] == val:
                return False

        # 2. Check Column
        for row in range(9):
            if row != r and self.game_board[row][c] == val:
                return False

        # 3. Check 3x3 Box
        start_row, start_col = 3 * (r // 3), 3 * (c // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if i != r and j != c and self.game_board[i][j] == val:
                    return False

        return True

    # --- Game Over / Solved Check ---

    def game_over(self):
        """Checks if the board is complete and correctly solved."""

        # Check if the board is completely filled (no zeros)
        for r in range(9):
            for c in range(9):
                if self.game_board[r][c] == 0:
                    return False

        # If it's full, check if it's correctly solved using the full validation logic
        if self._is_solved():
            print("\n🎉 CONGRATULATIONS! YOU WON! 🎉")
            self.is_game_over = True
            return True

        return False

    def _is_solved(self):
        """Performs a final, complete check on the whole board."""

        # Helper to check a list for unique 1-9
        def has_unique_1_to_9(nums):
            valid_nums = [n for n in nums if n != 0]
            return sorted(valid_nums) == list(range(1, 10))

        # Check all rows, columns, and boxes
        for i in range(9):
            # Check Row i
            if not has_unique_1_to_9(self.game_board[i]):
                return False

            # Check Column i
            col_list = [self.game_board[r][i] for r in range(9)]
            if not has_unique_1_to_9(col_list):
                return False

        # Check all 3x3 boxes
        for box_row in range(3):
            for box_col in range(3):
                box_list = []
                for r in range(box_row * 3, box_row * 3 + 3):
                    for c in range(box_col * 3, box_col * 3 + 3):
                        box_list.append(self.game_board[r][c])

                if not has_unique_1_to_9(box_list):
                    return False

        return True

    # --- AI Backtracking Solver ---

    def _find_empty_cell(self):
        """Finds the next empty cell (0) from top-left to bottom-right."""
        for r in range(9):
            for c in range(9):
                if self.game_board[r][c] == 0:
                    return r, c
        return None  # Board is full

    def solve_puzzle(self):
        """
        Main solver function using the backtracking algorithm.
        """
        start_time = time.time()

        # The recursive helper function
        if self._solve_recursive():
            end_time = time.time()
            elapsed = end_time - start_time
            print("\n==============================================")
            print("🤖 AI Solver Finished!")
            print(f"Time elapsed: {elapsed:.4f} seconds")
            print("==============================================")
            self.print_board(title="AI SOLVED BOARD")
            self.is_game_over = True
            return True
        else:
            print("\n❌ AI Solver failed. This puzzle has no solution.")
            return False

    def _solve_recursive(self):
        """
        Recursive core of the backtracking algorithm.
        """
        # 1. Find the next unassigned cell (Base Case)
        next_cell = self._find_empty_cell()
        if next_cell is None:
            # If no empty cell is found, the puzzle is solved.
            return True

        r, c = next_cell

        # 2. Try numbers 1 through 9 (Brute Force Step)
        for num in range(1, 10):
            # 3. Check if the number is legal (Constraint Check)
            # Temporarily place the number to check if it's safe
            self.game_board[r][c] = num

            if self._is_safe(r, c, num):
                # 4. Recursively try to solve the rest of the board
                if self._solve_recursive():
                    # If recursion returns True, we found a complete solution
                    return True

            # 5. Backtrack: If the current number didn't lead to a solution, 
            #    reset the cell to 0 and try the next number.
            self.game_board[r][c] = 0

        # 6. Failure: If no number from 1-9 worked, this branch fails.
        return False


def main():
    print("Welcome to Sudoku! Select a mode:")
    print("1. Normal Game (Human Play)")
    print("2. Test Game (Human Play, one move left)")
    print("3. AI Solve (Solver demonstrates solution)")

    selected_mode = input("Enter 1, 2, or 3: ")

    mode = "normal"
    if selected_mode == '2':
        mode = "test"
        print("\nStarting **Test Game** mode. Find the one missing number (Row 0, Col 2)!")
    elif selected_mode == '3':
        mode = "normal"  # Use the normal puzzle as the default AI target
        print("\nStarting **AI Solver** mode...")

        # Initialize the board for the AI
        ai_sudoku = Sudoku(mode=mode)
        ai_sudoku.print_board(title="Initial Puzzle for AI")

        # Run the solver
        ai_sudoku.solve_puzzle()
        return  # Exit main after AI finishes
    else:
        print("\nStarting **Normal Game** mode.")

    # Human Play Loop (Modes 1 and 2)
    my_sudoku = Sudoku(mode=mode)

    while not my_sudoku.is_game_over:
        my_sudoku.print_board()
        my_sudoku.take_player_move()
        # Check game state after the move
        my_sudoku.game_over()

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
