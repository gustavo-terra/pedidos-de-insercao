from dataclasses import dataclass

@dataclass
class Agency:
    name: str
    razao_social: str
    id: str # CNPJ, por exemplo
    address: str | None = None
    phone: str | None = None
    email: str | None = None