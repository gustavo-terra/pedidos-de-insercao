from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from .agency import Agency
from .client import Client
from .vehicle import Vehicle

from validators.common import validate_date_interval, validate_amount, validate_pct

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
        if not validate_date_interval(self.start_date, self.end_date):
            raise ValueError("Invalid start/end date combination")
        
        if not validate_amount(self.total_budget):
            raise ValueError("Invalid total budget")
        
        if not validate_pct(self.agency_commission_pct):
            raise ValueError("Invalid comission percentage")