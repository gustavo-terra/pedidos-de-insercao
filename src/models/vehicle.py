from dataclasses import dataclass

@dataclass
class Vehicle:
    name: str
    razao_social: str
    id: str
    address: str | None = None
    phone: str | None = None
    email: str | None = None