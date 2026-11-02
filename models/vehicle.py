from dataclasses import dataclass

@dataclass
class Vehicle:
    name: str
    razao_social: str
    id: str
    address: str
    phone: str
    email: str