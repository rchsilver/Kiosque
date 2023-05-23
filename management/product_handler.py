from menu import products


def get_product_by_id(id: int):
    for product in products:
        if product["_id"] == id:
            return product
    return {}


def get_products_by_type(search: str):
    search_products = []
    for product in products:
        if product["type"] == search:
            search_products.append(product)
    return search_products
