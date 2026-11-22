from datetime import date
from decimal import Decimal

def validate_name(value):
    return bool(value and value.strip()) # True se string não vazia

def validate_email(value): # TODO
    return "@" in value

def validate_date_interval(start_date: date, end_date: date) -> bool:
    return end_date > start_date

def validate_amount(value: Decimal):
    return value >= 0

def validate_pct(value: Decimal):
    return value > 0 and value < 1 