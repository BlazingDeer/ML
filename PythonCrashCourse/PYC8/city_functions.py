def get_formatted_city_name(city,country,population=''):
    """Zwraca ladnie sformatowana nazwe miasta"""
    if population:
        city_name=f"{city}, {country} - {population}"
    else:
        city_name=f"{city}, {country}"
    return city_name.title()