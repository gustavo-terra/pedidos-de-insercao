from typing import Any

from openpyxl import load_workbook

from .base import Spreadsheet


class XLSXSpreadsheet(Spreadsheet):

    def __init__(self, filepath: str):
        self.workbook = load_workbook(filename=filepath)
        self.sheet = self.workbook.active

    def find_marker(self, marker: str) -> tuple[int, int] | None:
        for row in self.sheet.iter_rows():
            for cell in row:
                if isinstance(cell.value, str) and marker in cell.value:
                    return (cell.row, cell.column)

        return None

    def read_cell(self, row: int, column: int) -> Any:
        return self.sheet.cell(row=row, column=column).value

    def write_cell(self, row: int, column: int, value: Any) -> None:
        self.sheet.cell(row=row, column=column).value = value

    def save(self, filepath: str) -> None:
        self.workbook.save(filepath)