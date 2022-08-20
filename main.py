# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_sudoku(sudoku):
    for y in range(0, 9):
        if y > 0 and y % 3 == 0:
            print(27*'-')
        line_str = [str(x) for x in sudoku[y]]
        print('  '.join(line_str[0: 3]) + " | " + '  '.join(line_str[3: 6]) + " | " + '  '.join(line_str[6: 9]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('sudoku-solver')
    sudoku_1 = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]

    print_sudoku(sudoku_1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
