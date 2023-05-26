from menu import products


def calculate_tab(order_list) -> dict[str, str]:
    total = []
    for order in order_list:
        for product in products:
            if product["_id"] == order["_id"]:
                total.append(product["price"] * order["amount"])

    return {"subtotal": f"${round(sum(total), 2)}"}
