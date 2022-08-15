class Cell:
    def __init__(self, value, is_editable) -> None:
        """Initialize the cell"""
        self.value = value
        self.is_editable = is_editable

    def is_editable(self) -> bool:
        """Return editability status of the cell"""
        return self.is_editable
    
    def cell_value(self) -> int:
        """Return the value of the cell"""
        return self.value

    def set_cell_value(self, value) -> None:
        """Update the value of the cell"""
        self.value = value