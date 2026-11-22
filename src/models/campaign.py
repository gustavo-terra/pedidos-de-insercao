from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from .agency import Agency
from .client import Client
from .vehicle import Vehicle

@dataclass
class Campaign:
    id: str
    name: str
    product: str
    client: Client
    agency: Agency
    start_date: date
    end_date: date
    total_budget: Decimal
    vehicles: Vehicle
    agency_commission_pct: Decimal
    payment_terms: str
    notes: str | None = None

    def __post_init__(self):
        if self.end_date < self.start_date:
            raise ValueError("end_date não pode ser anterior a start_date")