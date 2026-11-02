from dataclasses import dataclass

@dataclass
class Agency:
    name: str
    razao_social: str
    id: str
    address: str
    phone: str
    email: str