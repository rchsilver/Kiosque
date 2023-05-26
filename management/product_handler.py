from menu import products
from collections import Counter


def get_product_by_id(id: int) -> dict:
    if type(id) != int:
        raise TypeError("product id must be an int")

    for product in products:
        if product["_id"] == id:
            return product

    return {}


def get_products_by_type(search: str) -> list:
    if type(search) != str:
        raise TypeError("product type must be a str")

    search_products = []
    for product in products:
        if product["type"] == search:
            search_products.append(product)

    return search_products


def add_product(menu: list[dict], **kwargs: dict) -> dict[str, dict]:
    if len(menu) == 0:
        kwargs["_id"] = 1
        menu.append(kwargs)
        return kwargs
    else:
        ids: list[int] = []
        for id in menu:
            ids.append(id["_id"])
        biggest_id = max(ids)
        kwargs["_id"] = biggest_id + 1
        menu.append(kwargs)

        return kwargs


def menu_report() -> str:
    product_count = len(products)
    total = 0.00
    products_types = []

    for product in products:
        products_types.append(product["type"])
        total += product["price"]
    count_values = Counter(products_types)
    most_common_type = count_values.most_common(1)[0][0]
    average_price = total/product_count

    return f"Products Count: {product_count} - Average Price: ${round(average_price, 2)} - Most Common Type: {most_common_type}"
