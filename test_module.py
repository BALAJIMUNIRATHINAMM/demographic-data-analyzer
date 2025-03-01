import unittest
from demographic_data_analyzer import demographic_data_analyzer

class DemographicDataAnalyzerTest(unittest.TestCase):
    def setUp(self):
        self.results = demographic_data_analyzer()

    def test_race_count(self):
        self.assertTrue("White" in self.results["race_count"].index)

    def test_average_age_men(self):
        self.assertAlmostEqual(self.results["average_age_men"], 39.4, places=1)

    def test_percentage_bachelors(self):
        self.assertAlmostEqual(self.results["percentage_bachelors"], 16.4, places=1)

    def test_highest_earning_country(self):
        self.assertEqual(self.results["highest_earning_country"], "United-States")

if __name__ == "__main__":
    unittest.main()
