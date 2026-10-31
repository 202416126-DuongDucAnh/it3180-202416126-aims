import sys
import unittest

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearch(unittest.TestCase):

    def test_search_by_title_case_insensitive(self):
        dvds = [
            DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95),
            DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 120, 24.95),
        ]
        results = search_by_title(dvds, "lion")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "The Lion King")


if __name__ == "__main__":
    unittest.main()
