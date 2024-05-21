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
        if basket.get("status") == "PAID":
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
    if not shopping_baskets or not isinstance(shopping_baskets, list):
        return 0
    customer_baskets = get_customer_baskets(email, shopping_baskets)
    return sum(
        item["price"] * item["quantity"]
        for basket in customer_baskets
        if basket["status"] in ["PAID", "DELIVERED"]
        for item in basket["items"]
    )


def get_top_customers(shopping_baskets):
    if not shopping_baskets or not isinstance(shopping_baskets, list):
        return []
    customer_spending = {}
    for basket in shopping_baskets:
        if basket["status"] in ["PAID", "DELIVERED"]:
            email = basket["email"]
            if email not in customer_spending:
                customer_spending[email] = 0
            for item in basket["items"]:
                customer_spending[email] += item["price"] * item["quantity"]
    top_customers = [
        {"email": email, "total": total} for email, total in customer_spending.items()
    ]
    top_customers.sort(key=lambda x: x["total"], reverse=True)
    return top_customers


def get_customers_with_open_baskets(shopping_baskets):
    """Get a list of customers who have open baskets."""
    if not shopping_baskets or not isinstance(shopping_baskets, list):
        return []
    open_customers = {
        basket["email"] for basket in shopping_baskets if basket["status"] == "OPEN"
    }
    return sorted(open_customers)
