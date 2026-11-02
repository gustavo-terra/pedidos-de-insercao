from abc import ABC, abstractmethod
from typing import Any


class Spreadsheet(ABC):

    @abstractmethod
    def find_marker(self, marker: str) -> tuple[int, int] | None:
        pass

    @abstractmethod
    def read_cell(self, row: int, column: int) -> Any:
        pass

    @abstractmethod
    def write_cell(self, row: int, column: int, value: Any) -> None:
        pass

    @abstractmethod
    def save(self, filepath: str) -> None:
        pass