import unittest
import json
from cart.cart import (
    get_customer_baskets,
    get_all_customers,
    get_required_stock,
    get_total_spent,
    get_top_customers,
    get_customers_with_open_baskets,
)


class TestShoppingCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Loading test data from a JSON file (assuming it's named 'data.json' and in the same directory)
        with open("data.json", "r") as file:
            cls.shopping_baskets = json.load(file)

    def test_get_customer_baskets(self):
        # Test retrieving baskets for a specific customer
        baskets = get_customer_baskets("tshepo@umuzi.org", self.shopping_baskets)
        self.assertEqual(
            len(baskets), 4
        )  # Assuming 'tshepo@umuzi.org' has 4 baskets in the test data

    def test_get_all_customers(self):
        # Test retrieving all unique customer emails
        customers = get_all_customers(self.shopping_baskets)
        self.assertIn("tshepo@umuzi.org", customers)
        self.assertIn("sally@umuzi.org", customers)
        self.assertIn("mpho@umuzi.org", customers)
        self.assertIn("ryan@umuzi.org", customers)
        self.assertIn("mo@umuzi.org", customers)
        self.assertEqual(len(customers), 5)  # Total unique customers

    def test_get_required_stock(self):
        # Test calculating required stock for delivery
        stock = get_required_stock(self.shopping_baskets)
        self.assertTrue(
            any(
                item["name"] == "128 GB SSD Hard drive" and item["quantity"] == 2
                for item in stock
            )
        )

    def test_get_total_spent(self):
        # Test calculating total spent by a specific customer
        total_spent = get_total_spent("sally@umuzi.org", self.shopping_baskets)
        self.assertEqual(total_spent, 3589)  # Sum up the totals from the JSON provided

    def test_get_top_customers(self):
        # Test retrieving top customers sorted by total amount spent
        top_customers = get_top_customers(self.shopping_baskets)
        self.assertTrue(
            top_customers[0]["email"] == "sally@umuzi.org"
            or top_customers[0]["email"] == "mo@umuzi.org"
        )

    def test_get_customers_with_open_baskets(self):
        # Test getting customers with open baskets
        open_customers = get_customers_with_open_baskets(self.shopping_baskets)
        self.assertIn("mpho@umuzi.org", open_customers)
        self.assertEqual(
            len(open_customers), 2
        )  # Assuming 'mpho@umuzi.org' and 'tshepo@umuzi.org' have open baskets

    def test_empty_input(self):
        """Test functions with empty list input."""
        self.assertEqual(get_customer_baskets("example@umuzi.org", []), [])
        self.assertEqual(get_all_customers([]), [])
        self.assertEqual(get_required_stock([]), [])

    def test_invalid_input(self):
        """Test functions with invalid non-list input."""
        self.assertEqual(get_customer_baskets("example@umuzi.org", "not a list"), [])
        self.assertEqual(get_all_customers("not a list"), [])
        self.assertEqual(get_required_stock("not a list"), [])


if __name__ == "__main__":
    unittest.main()
