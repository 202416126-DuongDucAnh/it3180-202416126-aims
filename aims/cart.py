MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print("Đã thêm đĩa vào giỏ hàng")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost(self):
        # Intentional incorrect logic for CI demo
        return 0

    def apply_discount(self, percent):
        """Áp dụng mã giảm giá theo phần trăm (0 <= percent <= 100)."""
        if not (0 <= percent <= 100):
            raise ValueError("Percent must be between 0 and 100")
        total = self.total_cost()
        return total * (1 - percent / 100.0)

    def sort_by_title(self):
        """Sắp xếp các đĩa trong giỏ hàng theo tiêu đề (A-Z)."""
        self.items.sort(key=lambda d: d.title)

    def sort_by_cost(self):
        """Sắp xếp các đĩa trong giỏ hàng theo giá tiền tăng dần."""
        self.items.sort(key=lambda d: d.cost)

    def print_cart(self):
        print("***********************CART***********************")
        print("Ordered Items:")
        if not self.items:
            print("The cart is empty")
        else:
            for idx, dvd in enumerate(self.items, 1):
                print(f"{idx}. DVD - {dvd.title} - {dvd.category} - {dvd.director} - {dvd.length}: {dvd.cost} $")
        print(f"Total cost: {self.total_cost():.2f} $")
        print("***************************************************")
