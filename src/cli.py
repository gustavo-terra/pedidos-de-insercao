def collect_input(field_info: list, title: str = "Input") -> dict:
    print(f"\n--- {title} ---")

    input_data = {}

    for field in field_info:
        prompt = field.name

        if not field.required:
            prompt += " (optional)"

        input_data[field.name] = input(f"{prompt}: ")

    return input_data


def display_errors(errors: list) -> None:
    print("\nPlease correct the following errors:")

    for error in errors:
        print(f"- {error.message}")


def display_message(message: str) -> None:
    print(message)