# 6-11. Cities: Make a dictionary called cities. 
# -Use the names of three cities as keys in your dictionary. 
# -Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city.
# -The keys for each city’s dictionary should be something like country, population, and fact.
# -Print the name of each city and all of the information you have stored about it.

cities = {
    'chicago':{
        'country':'USA',
        'population':'5 mil',
        'fact':'highest crime',
    },
    'phoenix':{
        'country':'USA',
        'population':'4 mil',
        'fact':'One of the hottest major cities',
    },
    'san diego':{
        'country':'U.S.',
        'population':'6_000_000',
        'fact': 'perfect weather',
    },
}
for city, info in cities.items():
    print(f"\n{city.title()}:")
    for key, value in info.items():
        print(f"\t{key.title()}: {value}")