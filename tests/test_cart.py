import sys
import unittest

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()

    def test_add_dvd(self):
        dvd = DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95)
        self.assertTrue(self.cart.add_dvd(dvd))
        self.assertEqual(len(self.cart.items), 1)

    def test_add_dvd_until_full(self):
        """Kiểm tra thêm 20 đĩa thành công, đĩa thứ 21 phải bị từ chối."""
        for i in range(MAX_NUMBERS_ORDERED):
            dvd = DigitalVideoDisc(f"DVD {i+1}", "Animation", "Director", 90, 10.0)
            self.assertTrue(self.cart.add_dvd(dvd))

        self.assertEqual(len(self.cart.items), MAX_NUMBERS_ORDERED)

        # Thêm đĩa thứ 21
        extra_dvd = DigitalVideoDisc("DVD 21", "Animation", "Director", 90, 10.0)
        self.assertFalse(self.cart.add_dvd(extra_dvd), "Giỏ hàng đã đầy, đĩa thứ 21 không được thêm vào")
        self.assertEqual(len(self.cart.items), MAX_NUMBERS_ORDERED)

    def test_remove_dvd(self):
        dvd = DigitalVideoDisc("Aladdin", "Animation", "John Musker", 90, 18.99)
        self.cart.add_dvd(dvd)
        self.assertTrue(self.cart.remove_dvd(dvd))
        self.assertFalse(self.cart.remove_dvd(dvd))

    def test_total_cost(self):
        dvd1 = DigitalVideoDisc("DVD 1", "Animation", "Dir 1", 90, 10.0)
        dvd2 = DigitalVideoDisc("DVD 2", "Animation", "Dir 2", 90, 20.0)
        self.cart.add_dvd(dvd1)
        self.cart.add_dvd(dvd2)
        self.assertAlmostEqual(self.cart.total_cost(), 30.0)

    def test_apply_discount(self):
        dvd = DigitalVideoDisc("DVD 1", "Animation", "Dir 1", 90, 100.0)
        self.cart.add_dvd(dvd)
        discounted = self.cart.apply_discount(20)
        self.assertAlmostEqual(discounted, 80.0)
        with self.assertRaises(ValueError):
            self.cart.apply_discount(-5)
        with self.assertRaises(ValueError):
            self.cart.apply_discount(105)

    def test_sort_by_title(self):
        dvd1 = DigitalVideoDisc("The Lion King", "Animation", "Dir", 90, 19.95)
        dvd2 = DigitalVideoDisc("Aladdin", "Animation", "Dir", 90, 18.99)
        dvd3 = DigitalVideoDisc("Beauty and the Beast", "Animation", "Dir", 90, 15.0)
        self.cart.add_dvd(dvd1)
        self.cart.add_dvd(dvd2)
        self.cart.add_dvd(dvd3)
        self.cart.sort_by_title()
        titles = [d.title for d in self.cart.items]
        self.assertEqual(titles, ["Aladdin", "Beauty and the Beast", "The Lion King"])

    def test_sort_by_cost(self):
        dvd1 = DigitalVideoDisc("DVD 1", "Animation", "Dir", 90, 30.0)
        dvd2 = DigitalVideoDisc("DVD 2", "Animation", "Dir", 90, 10.0)
        dvd3 = DigitalVideoDisc("DVD 3", "Animation", "Dir", 90, 20.0)
        self.cart.add_dvd(dvd1)
        self.cart.add_dvd(dvd2)
        self.cart.add_dvd(dvd3)
        self.cart.sort_by_cost()
        costs = [d.cost for d in self.cart.items]
        self.assertEqual(costs, [10.0, 20.0, 30.0])


if __name__ == "__main__":
    unittest.main()
