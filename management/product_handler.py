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


def add_product(menu: list[dict], **kwargs: dict):
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
