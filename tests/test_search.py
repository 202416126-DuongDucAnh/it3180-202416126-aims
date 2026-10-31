import sys
import unittest

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title, search_by_category


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.dvds = [
            DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95),
            DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 120, 24.95),
            DigitalVideoDisc("Aladdin", "Animation", "John Musker", 90, 18.99),
        ]

    def test_search_by_category(self):
        results = search_by_category(self.dvds, "Animation")
        self.assertEqual(len(results), 2)
        results_lower = search_by_category(self.dvds, "science")
        self.assertEqual(len(results_lower), 1)
        self.assertEqual(results_lower[0].title, "Star Wars")

    def test_search_by_category_empty(self):
        self.assertEqual(search_by_category(self.dvds, ""), [])
        self.assertEqual(search_by_category(self.dvds, "Action"), [])

    def test_search_by_title(self):
        results = search_by_title(self.dvds, "Lion")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "The Lion King")

    def test_search_by_title_case_insensitive(self):
        results = search_by_title(self.dvds, "lion")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "The Lion King")


if __name__ == "__main__":
    unittest.main()
