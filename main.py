class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False

        self.ledger.append({
            "amount": -amount,
            "description": description
        })
        return True

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*")
        lines = [title]

        for item in self.ledger:
            description = item["description"][:23]
            amount = f'{item["amount"]:.2f}'
            lines.append(f"{description:<23}{amount:>7}")

        lines.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(lines)


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"

    total_spent = sum(
        -item["amount"]
        for category in categories
        for item in category.ledger
        if item["amount"] < 0
        and not item["description"].startswith("Transfer to ")
    )

    percentages = []

    for category in categories:
        spent = sum(
            -item["amount"]
            for item in category.ledger
            if item["amount"] < 0
            and not item["description"].startswith("Transfer to ")
        )

        if total_spent == 0:
            percentage = 0
        else:
            percentage = int((spent / total_spent) * 100)

        percentages.append((percentage // 10) * 10)

    for level in range(100, -1, -10):
        chart += f"{level:>3}|"
        for percentage in percentages:
            if percentage >= level:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1)

    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        chart += "\n     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i]
            else:
                chart += " "
            chart += "  "

    return chart.rstrip("\n")