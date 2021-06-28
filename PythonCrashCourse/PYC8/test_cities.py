import unittest
from city_functions import get_formatted_city_name

class CityTestCase(unittest.TestCase):
    """Testy dla city_functions.py"""

    def test_city_country(self):
        """Czy działa dla Warszawa, Polska"""
        city_country_name=get_formatted_city_name("Warszawa","Polska")
        self.assertEqual(city_country_name,"Warszawa, Polska")

    def test_city_country_population(self):
        """Czy dziala Santiago Chile 5400000"""
        city_country_population_name=get_formatted_city_name("Santiago","Chile","5400000")
        self.assertEqual(city_country_population_name,"Santiago, Chile - 5400000")

if __name__=="__main__":
    unittest.main()
