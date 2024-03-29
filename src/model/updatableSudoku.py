from src.model.field import Field


class UpdatableSudoku:
    def __init__(self, sudoku_array):
        self.field_dict = dict()
        for x in range(0, 9):
            for y in range(0, 9):
                self.field_dict[(x, y)] = Field(sudoku_array[y][x])

    def is_possible_state(self):
        return self.check_columns() and self.check_rows() and self.check_boxes()

    def check_columns(self):
        for x in range(0, 9):
            values_of_column = set()
            for y in range(0, 9):
                if self.field_dict[(x, y)].value != 0:
                    if self.field_dict[(x, y)].value in values_of_column:
                        return False
                    else:
                        values_of_column.add(self.field_dict[(x, y)].value)
        return True

    def check_rows(self):
        for y in range(0, 9):
            values_of_row = set()
            for x in range(0, 9):
                if self.field_dict[(x, y)].value != 0:
                    if self.field_dict[(x, y)].value in values_of_row:
                        return False
                    else:
                        values_of_row.add(self.field_dict[(x, y)].value)
        return True

    def check_boxes(self):
        for column in range(0, 3):
            for row in range(0, 3):
                if not self.check_box((column, row)):
                    return False
        return True

    def check_box(self, box):
        values = set()
        for x in range(box[0] * 3, box[0] * 3 + 3):
            for y in range(box[1] * 3, box[1] * 3 + 3):
                if self.field_dict[(x, y)].value != 0:
                    if self.field_dict[(x, y)].value in values:
                        return False
                    else:
                        values.add(self.field_dict[(x, y)].value)
        return True
