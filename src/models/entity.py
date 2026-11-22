from dataclasses import dataclass

from validators.common import validate_name, validate_email
from validators.documents import validate_cpf, validate_cnpj

@dataclass
class Entity:
    name: str
    razao_social: str
    id: str
    address: str | None = None
    phone: str | None = None
    email: str | None = None

    def __post_init__(self):
        if not validate_name(self.name):
            raise ValueError("Invalid name")

        if self.email is not None and not validate_email(self.email):
            raise ValueError("Invalid email")

        if not validate_cnpj(self.id) and not validate_cpf(self.id):
            raise ValueError("Invalid id")