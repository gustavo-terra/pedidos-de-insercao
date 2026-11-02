from dataclasses import dataclass

@dataclass
class Client:
    name: str
    razao_social: str
    id: str
    address: str
    phone: str
    email: str