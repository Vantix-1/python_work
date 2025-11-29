from city_functions import get_formatted_city_coutry

def test_city_country():
    """"Do cities like 'Santiago, Chile' work?"""
    formatted_city_country = get_formatted_city_coutry('santiago', 'chile')
    assert formatted_city_country == 'Santiago, Chile'

def test_city_country_population():
    """Do cities and countries with added population work"""
    formatted_city_country = get_formatted_city_coutry('santiago','chile', '500000')
    assert formatted_city_country == 'Santiago, Chile, 500000'