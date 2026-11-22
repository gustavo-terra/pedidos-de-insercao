def validate_name(value):
    return bool(value and value.strip()) # True se string não vazia

def validate_email(value): # TODO
    return "@" in value