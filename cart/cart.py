PAID = "PAID"
DELIVERED = "DELIVERED"
OPEN = "OPEN"


def filter_baskets_by_status(shopping_baskets, status):
    return [basket for basket in shopping_baskets if basket["status"] == status]


def calculate_total(items):
    return sum(item["price"] * item["quantity"] for item in items)


def get_customer_baskets(email, shopping_baskets):
    if not shopping_baskets or not isinstance(shopping_baskets, list):
        return []
    return [basket for basket in shopping_baskets if basket["email"] == email]


def get_all_customers(shopping_baskets):
    if not shopping_baskets or not isinstance(shopping_baskets, list):
        return []
    email_set = {
        basket["email"] for basket in shopping_baskets if isinstance(basket, dict)
    }
    return sorted(email_set)


def get_required_stock(shopping_baskets):
    if not shopping_baskets or not isinstance(shopping_baskets, list):
        return []
    required_stock = {}
    for basket in shopping_baskets:
        if basket.get("status") == PAID:
            for item in basket.get("items", []):
                if "name" in item and "quantity" in item:
                    required_stock[item["name"]] = (
                        required_stock.get(item["name"], 0) + item["quantity"]
                    )
    return [
        {"name": name, "quantity": quantity}
        for name, quantity in required_stock.items()
    ]


def get_total_spent(email, shopping_baskets):
    customer_baskets = get_customer_baskets(email, shopping_baskets)
    return sum(
        calculate_total(basket["items"])
        for basket in customer_baskets
        if basket["status"] in [PAID, DELIVERED]
    )


def get_top_customers(shopping_baskets):
    customer_spending = {}
    for basket in shopping_baskets:
        if basket["status"] in [PAID, DELIVERED]:
            customer_spending[basket["email"]] = customer_spending.get(
                basket["email"], 0
            ) + calculate_total(basket["items"])
    top_customers = [
        {"email": email, "total": total} for email, total in customer_spending.items()
    ]
    top_customers.sort(key=lambda x: x["total"], reverse=True)
    return top_customers


def get_customers_with_open_baskets(shopping_baskets):
    open_customers = {
        basket["email"] for basket in filter_baskets_by_status(shopping_baskets, OPEN)
    }
    return sorted(open_customers)
