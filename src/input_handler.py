from dataclasses import dataclass, fields, MISSING
from typing import get_args

from models import Agency, Client, Vehicle, Campaign, mapped_classes

def get_base_type(annotation):
    args = get_args(annotation)

    if type(None) in args:
        return next(arg for arg in args if arg is not type(None))

    return annotation

@dataclass(frozen=True)
class FieldInfo:
    name: str
    type: type
    required: bool

@dataclass
class ValidationError:
    field: str
    message: str

def get_fields(class_name: str) -> list[FieldInfo]:
    model = mapped_classes.get(class_name)

    if model is None:
        raise ValueError(f"Specified class {class_name} does not exist.")
    
    return [
        FieldInfo(
            item.name,
            get_base_type(item.type),
            item.default is MISSING 
            and item.default_factory is MISSING
        )
        for item in fields(model)
        if get_base_type(item.type) not in mapped_classes.values() # ignora classes Agency,Vehicle e Client em Campaign, pois já validou
    ]

# check_fields: apenas verifica se há string vazia para campos requeridos ou tipo divergente
def check_fields(field_info: list[FieldInfo], input_data: dict) -> list[ValidationError]:

    errors: list[ValidationError] = []

    for field in field_info:
        value = input_data.get(field.name)

        if value is None or (isinstance(value, str) and not value.strip()):
            if field.required:
                errors.append(
                    ValidationError(
                        field=field.name,
                        message=f"{field.name} is required."
                    )
                )
            continue

        try:
            field.type(value)
        except (ValueError, TypeError):
            errors.append(
                ValidationError(
                    field=field.name,
                    message=f"Invalid value for {field.name}. Expected {field.type.__name__}."
                )
            )

    return errors

def create_model(class_name: str, input_data: dict):
    model = mapped_classes.get(class_name)

    if model is None:
        raise ValueError(f"Specified class {class_name} does not exist.")

    converted_data = {}

    for field in fields(model):
        if field.name not in input_data:
            continue

        field_type = get_base_type(field.type)
        value = input_data[field.name]

        if isinstance(value, str) and not value.strip():
            converted_data[field.name] = None
            continue

        if field_type in mapped_classes.values():
            converted_data[field.name] = value
        else:
            converted_data[field.name] = field_type(value)

    return model(**converted_data)
