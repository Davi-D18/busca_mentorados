from datetime import datetime


def convert_date(date_str, input_format="%Y-%m-%d", output_format="%d/%m/%Y"):
    try:
        date_obj = datetime.strptime(date_str, input_format)
        return date_obj.strftime(output_format)
    except ValueError:
        raise ValueError("Formato de data inválido.")
