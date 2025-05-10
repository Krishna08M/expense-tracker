import json

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.expenses.append({"amount": amount, "category": category})

    def get_total(self):
        return sum(e["amount"] for e in self.expenses)

    def get_by_category(self, category):
        return [e for e in self.expenses if e["category"] == category]

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            json.dump(self.expenses, f)

    def load_from_file(self, filename):
        with open(filename, "r") as f:
            self.expenses = json.load(f)
