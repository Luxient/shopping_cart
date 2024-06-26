# Shopping Cart Calculations

This project implements various functionalities for managing shopping cart data for an online shopping startup. The project includes functions to retrieve customer-specific data, calculate totals, and determine stock requirements based on the provided shopping basket data.

## Directory Structure

```
├── README.md
└── shopping_cart/
    └── shopping_cart.py
```

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository (replace `your-username` with your GitHub username if different):
    ```sh
    git clone https://github.com/your-username/shopping_cart.git
    ```

2. Navigate to the project directory:
    ```sh
    cd shopping_cart
    ```

### Usage

To use the functions, you can import them from `shopping_cart.py` and call them with the appropriate parameters.

#### Example

```python
from shopping_cart import (
    get_customer_baskets,
    get_all_customers,
    get_required_stock,
    get_total_spent,
    get_top_customers,
    get_customers_with_open_baskets
)

# Sample data
shopping_baskets = [
    {
        "email": "john@example.com",
        "status": "OPEN",
        "items": [
            {"name": "hamster", "quantity": 2, "price": 20},
            {"name": "saw dust", "quantity": 1, "price": 20},
            {"name": "hamster-cage", "quantity": 1, "price": 150},
            {"name": "book: how to care for your hamster", "quantity": 1, "price": 150}
        ]
    },
]

customer_baskets = get_customer_baskets("john@example.com", shopping_baskets)
all_customers = get_all_customers(shopping_baskets)
required_stock = get_required_stock(shopping_baskets)
total_spent = get_total_spent("john@example.com", shopping_baskets)
top_customers = get_top_customers(shopping_baskets)
customers_with_open_baskets = get_customers_with_open_baskets(shopping_baskets)

print(customer_baskets)
print(all_customers)
print(required_stock)
print(total_spent)
print(top_customers)
print(customers_with_open_baskets)
```

## Functions Documentation

- **`get_customer_baskets(email, shopping_baskets)`**
  - **Parameters**:
    - `email` (str): The email address of the customer.
    - `shopping_baskets` (list): A list of all shopping baskets.
  - **Returns**: List of shopping baskets for the specified customer.

- **`get_all_customers(shopping_baskets)`**
  - **Returns**: Sorted list of unique customer email addresses.

- **`get_required_stock(shopping_baskets)`**
  - **Returns**: List of dictionaries with item names and quantities required for delivery.

- **`get_total_spent(email, shopping_baskets)`**
  - **Returns**: Total amount spent by the customer.

- **`get_top_customers(shopping_baskets)`**
  - **Returns**: List of customers ordered by total amount spent.

- **`get_customers_with_open_baskets(shopping_baskets)`**
  - **Returns**: Sorted list of email addresses for customers with open baskets.

## Author

- Butho James Mthethwa

## License

This project is licensed under the [MIT License](https://mit-license.org/).
