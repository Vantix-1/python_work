def get_formatted_city_coutry(city, country, population=''):
    """"Generate a neatly formatted City and Country."""
    if population:
        formatted_city_country = f"{city}, {country}, {population}"
    else:
        formatted_city_country = f"{city}, {country}"
    return formatted_city_country.title()