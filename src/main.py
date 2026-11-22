
import cli
from input_handler import get_fields, check_fields, create_model


def main(ui):
    instances = {}

    models = ["Agency", "Client", "Vehicle"]

    for class_name in models:
        field_info = get_fields(class_name)
        input_data = ui.collect_input(field_info, class_name)

        errors = check_fields(field_info, input_data)

        if errors:
            ui.display_errors(errors)
            return

        try:
            instances[class_name] = create_model(class_name, input_data)
        except (ValueError, TypeError) as error:
            ui.display_message(f"Could not create {class_name}: {error}")
            return
    
    # coletar dados de campanha
    field_info = get_fields("Campaign")
    campaign_data = ui.collect_input(field_info, "Campaign")

    errors = check_fields(field_info, campaign_data)

    if errors:
        ui.display_errors(errors)
        return

    # Injeta os objetos já instanciados nos campos compostos
    campaign_data.update({
        "agency": instances["Agency"],
        "client": instances["Client"],
        "vehicle": instances["Vehicle"]
    })

    try:
        instances["Campaign"] = create_model(
            "Campaign",
            campaign_data
        )
    except (ValueError, TypeError) as error:
        ui.display_message(
            f"Could not create Campaign: {error}"
        )
        return

    ui.display_message("All entities created successfully.")


if __name__ == "__main__":
    main(cli)
