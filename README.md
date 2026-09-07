💰 Object Oriented Programming Lab – Part 2: Cash Register
This lab builds on Part 1 (Bookstore) by introducing more advanced Object-Oriented Programming (OOP) concepts such as properties, validation, and state management. The goal is to model a Cash Register object that simulates real-world checkout operations for an e-commerce site.

📖 Scenario
You are tasked with building a Cash Register class to represent checkout operations in an online store. The register should support adding items, applying discounts, and voiding transactions. This lab emphasizes encapsulation, validation, and dynamic behavior.

🛠️ Tools & Resources
Python Classes Documentation

GitHub Repo: oop-p2-cash-register-lab (github.com in Bing)

⚙️ Setup Instructions
Clone the repository

bash
git clone https://github.com/giftmutua-alt/oop-p2-cash-register-lab.git
cd oop-p2-cash-register-lab
Install dependencies

bash
pipenv install
pipenv shell
Run tests

bash
pytest lib/testing/
🏗️ Cash Register Class
File: lib/cash_register.py

Attributes
discount → integer (0–100), default 0

total → float, default 0

items → list, default empty

previous_transactions → list, default empty

Properties
discount → validates that the value is an integer between 0–100.

If invalid, prints "Not valid discount".

Methods
add_item(item, price, quantity)

Adds item(s) to the register.

Updates total.

Stores transaction details in previous_transactions.

apply_discount()

Applies discount percentage to total.

If no discount, prints "There is no discount to apply.".

void_last_transaction()

Removes the last transaction from previous_transactions.

Updates total and items accordingly.

If no transactions exist, prints "No transaction to void.".

🧪 Example Usage
python
from lib.cash_register import CashRegister

register = CashRegister(discount=20)

register.add_item("Book", 15.00, 2)
register.add_item("Coffee", 3.50, 1)

print(register.total)  # 33.50
print(register.items)  # ['Book', 'Book', 'Coffee']

register.apply_discount()
print(register.total)  # 26.80

register.void_last_transaction()
print(register.total)  # 30.00
print(register.items)  # ['Book', 'Book']
✅ Testing
This project is test-driven. Tests are located in lib/testing/:

cash_register_test.py → validates the CashRegister class.

Run tests with:

bash
pytest lib/testing/
📄 Documentation & Maintenance
Code includes comments explaining purpose and logic.

README updated to reflect functionality.

Stale branches removed after merging.

Sensitive data excluded via .gitignore.

🏆 Submission & Grading
CodeGrade will automatically score your submission based on the latest commit.

Ensure you push your changes before submitting.

Review your score in Canvas after submission.