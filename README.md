# Budget App

A Python budget tracker that records deposits, withdrawals and transfers across spending categories, and draws a text-based bar chart of spending by category.

## Features

- **Categories**: create budget categories such as Food, Clothing and Auto, each with its own ledger
- **Deposits and withdrawals**: record money in and out with optional descriptions
- **Fund checks**: withdrawals and transfers are refused if the balance is too low
- **Transfers**: move money between categories, logged on both ledgers
- **Printable ledger**: each category prints a formatted statement with its total
- **Spend chart**: a bar chart of the percentage spent per category, rounded down to the nearest 10%

## Tech Stack

- Python 3, with no external dependencies

## How to Run

```bash
git clone https://github.com/talarianupama/budget-app.git
cd budget-app
python
```

```python
>>> from budget_app import Category, create_spend_chart
>>> food = Category("Food")
>>> food.deposit(1000, "initial deposit")
>>> food.withdraw(10.15, "groceries")
>>> clothing = Category("Clothing")
>>> food.transfer(50, clothing)
True
>>> print(food)
*************Food*************
initial deposit        1000.00
groceries               -10.15
Transfer to Clothing    -50.00
Total: 939.85
>>> print(create_spend_chart([food, clothing]))
```

## What I Learned

- Designing a class with state (a ledger) and methods that work together
- Validating actions before changing data, such as checking funds before a withdrawal
- Formatting aligned text output with f-strings
- Turning data into a chart using plain string building

## Author

**Anupama**: [GitHub](https://github.com/talarianupama)