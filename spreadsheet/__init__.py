# spreadsheet/__init__.py
from .base import Spreadsheet
from .xlsx import XLSXSpreadsheet

__all__ = ["Spreadsheet", "XLSXSpreadsheet"]