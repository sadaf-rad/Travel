import pandas as pd

def load_country_data():
    """Load the data for visited places."""
    data = {
        # Turkey
        'Istanbul': {'Country': 'Turkey', 'Latitude': 41.0082, 'Longitude': 28.9784, 'Flag': 'https://flagcdn.com/tr.svg'},

        # UAE
        'Dubai': {'Country': 'UAE', 'Latitude': 25.276987, 'Longitude': 55.296249, 'Flag': 'https://flagcdn.com/ae.svg'},
        'Sharjah': {'Country': 'UAE', 'Latitude': 25.346255, 'Longitude': 55.420924, 'Flag': 'https://flagcdn.com/ae.svg'},

        # Saudi Arabia
        'Makkah': {'Country': 'Saudi Arabia', 'Latitude': 21.4225, 'Longitude': 39.8262, 'Flag': 'https://flagcdn.com/sa.svg'},
        'Madinah': {'Country': 'Saudi Arabia', 'Latitude': 24.4714, 'Longitude': 39.6117, 'Flag': 'https://flagcdn.com/sa.svg'},

        # Lebanon
        'Beirut': {'Country': 'Lebanon', 'Latitude': 33.8888, 'Longitude': 35.4955, 'Flag': 'https://flagcdn.com/lb.svg'},

        # Syria
        'Damascus': {'Country': 'Syria', 'Latitude': 33.5138, 'Longitude': 36.2765, 'Flag': 'https://flagcdn.com/sy.svg'},

        # Netherlands
        'Leiden': {'Country': 'Netherlands', 'Latitude': 52.1601, 'Longitude': 4.4970, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Den Haag': {'Country': 'Netherlands', 'Latitude': 52.0705, 'Longitude': 4.3007, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Delft': {'Country': 'Netherlands', 'Latitude': 52.0116, 'Longitude': 4.3571, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Utrecht': {'Country': 'Netherlands', 'Latitude': 52.0907, 'Longitude': 5.1214, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Maastricht': {'Country': 'Netherlands', 'Latitude': 50.8514, 'Longitude': 5.6900, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Amsterdam': {'Country': 'Netherlands', 'Latitude': 52.3676, 'Longitude': 4.9041, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Rotterdam': {'Country': 'Netherlands', 'Latitude': 51.9225, 'Longitude': 4.47917, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Valkenburg': {'Country': 'Netherlands', 'Latitude': 50.8686, 'Longitude': 5.8233, 'Flag': 'https://flagcdn.com/nl.svg'},

        # UK
        'London': {'Country': 'UK', 'Latitude': 51.5074, 'Longitude': -0.1278, 'Flag': 'https://flagcdn.com/gb.svg'},
        'Nottingham': {'Country': 'UK', 'Latitude': 52.9548, 'Longitude': -1.1581, 'Flag': 'https://flagcdn.com/gb.svg'},
        'Manchester': {'Country': 'UK', 'Latitude': 53.4808, 'Longitude': -2.2426, 'Flag': 'https://flagcdn.com/gb.svg'},

        # Iran
        'Rasht': {'Country': 'Iran', 'Latitude': 37.2824, 'Longitude': 49.5894, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Mazandaran': {'Country': 'Iran', 'Latitude': 36.6349, 'Longitude': 53.0658, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Astara': {'Country': 'Iran', 'Latitude': 38.4240, 'Longitude': 48.8470, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Karaj': {'Country': 'Iran', 'Latitude': 35.8324, 'Longitude': 50.9919, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Tehran': {'Country': 'Iran', 'Latitude': 35.6892, 'Longitude': 51.3890, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Mashhad': {'Country': 'Iran', 'Latitude': 36.2605, 'Longitude': 59.6168, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Yazd': {'Country': 'Iran', 'Latitude': 31.8974, 'Longitude': 54.3646, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Shiraz': {'Country': 'Iran', 'Latitude': 29.5917, 'Longitude': 52.5833, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Isfahan': {'Country': 'Iran', 'Latitude': 32.0590, 'Longitude': 51.6772, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Qazvin': {'Country': 'Iran', 'Latitude': 36.2833, 'Longitude': 50.0042, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Fardis': {'Country': 'Iran', 'Latitude': 35.7826, 'Longitude': 50.9715, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Shahriar': {'Country': 'Iran', 'Latitude': 35.6636, 'Longitude': 51.1855, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Qeshm': {'Country': 'Iran', 'Latitude': 26.9983, 'Longitude': 56.2705, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Bandar Abbas': {'Country': 'Iran', 'Latitude': 27.1938, 'Longitude': 56.2677, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Boroujerd': {'Country': 'Iran', 'Latitude': 33.8949, 'Longitude': 48.6900, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Hamedan': {'Country': 'Iran', 'Latitude': 34.7942, 'Longitude': 48.5154, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Qom': {'Country': 'Iran', 'Latitude': 34.6395, 'Longitude': 50.8760, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Natanz': {'Country': 'Iran', 'Latitude': 33.4021, 'Longitude': 51.8269, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Abianeh': {'Country': 'Iran', 'Latitude': 33.3093, 'Longitude': 51.7348, 'Flag': 'https://flagcdn.com/ir.svg'},

        # France
        'Paris': {'Country': 'France', 'Latitude': 48.8566, 'Longitude': 2.3522, 'Flag': 'https://flagcdn.com/fr.svg'},

        # Germany
        'Essen': {'Country': 'Germany', 'Latitude': 51.4556, 'Longitude': 7.0116, 'Flag': 'https://flagcdn.com/de.svg'},
        'Neuss': {'Country': 'Germany', 'Latitude': 51.2020, 'Longitude': 6.6873, 'Flag': 'https://flagcdn.com/de.svg'},
        'Düsseldorf': {'Country': 'Germany', 'Latitude': 51.2217, 'Longitude': 6.7762, 'Flag': 'https://flagcdn.com/de.svg'},
        'Köln': {'Country': 'Germany', 'Latitude': 50.9375, 'Longitude': 6.9603, 'Flag': 'https://flagcdn.com/de.svg'},

        # Belgium
        'Brussels': {'Country': 'Belgium', 'Latitude': 50.8503, 'Longitude': 4.3517, 'Flag': 'https://flagcdn.com/be.svg'},
        'Antwerp': {'Country': 'Belgium', 'Latitude': 51.2194, 'Longitude': 4.4025, 'Flag': 'https://flagcdn.com/be.svg'},

        # Italy
        'Padua': {'Country': 'Italy', 'Latitude': 45.4064, 'Longitude': 11.8768, 'Flag': 'https://flagcdn.com/it.svg'},
        'Venice': {'Country': 'Italy', 'Latitude': 45.4408, 'Longitude': 12.3155, 'Flag': 'https://flagcdn.com/it.svg'},
        'Milan': {'Country': 'Italy', 'Latitude': 45.4642, 'Longitude': 9.1900, 'Flag': 'https://flagcdn.com/it.svg'},
        'Verona': {'Country': 'Italy', 'Latitude': 45.4384, 'Longitude': 10.9916, 'Flag': 'https://flagcdn.com/it.svg'}
    }

    return pd.DataFrame.from_dict(data, orient='index')
