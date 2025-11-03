# 8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. 
# -The function should return a string formatted like this: "Santiago, Chile"
# -Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(city, country):
    """Return a neatly formatted City and Country Output"""
    citys=f"{city.title()}, {country.title()}"
    return citys

print(city_country('santiago','chile'))
print(city_country('tokyo', 'japan'))
print(city_country('paris', 'france'))