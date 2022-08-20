class Field:
    def __init__(self, value):
        self.value = value
        self.preset = value != 0

    def to_string(self):
        if self.value == 0:
            return " "
        return str(self.value)