from dataclasses import dataclass

@dataclass
class Client:
    name: str
    razao_social: str
    id: str # CPF, CNPJ
    address: str | None = None
    phone: str | None = None
    email: str | None = None