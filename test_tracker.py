import unittest
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'expense_tracker')))

from tracker import ExpenseTracker
from tracker import ExpenseTracker

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = ExpenseTracker()

    def test_add_expense(self):
        self.tracker.add_expense(100, "Food")
        self.assertEqual(len(self.tracker.expenses), 1)

    def test_total(self):
        self.tracker.add_expense(100, "Food")
        self.tracker.add_expense(200, "Travel")
        self.assertEqual(self.tracker.get_total(), 300)

    def test_by_category(self):
        self.tracker.add_expense(100, "Food")
        self.tracker.add_expense(200, "Travel")
        food = self.tracker.get_by_category("Food")
        self.assertEqual(len(food), 1)
        self.assertEqual(food[0]["amount"], 100)

    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.tracker.add_expense(-50, "Food")

if __name__ == '__main__':
    unittest.main()
