from management import product_handler
from management import tab_handler
from menu import products

if __name__ == "__main__":
    # Seus prints de teste aqui
    # print(product_handler.get_product_by_id(28))
    # print(product_handler.get_products_by_type("vegetable"))
    # new_product: dict = {
    #     "description": "Sweet fresh strawberry on the wooden table",
    #     "price": 28.59,
    #     "rating": 4,
    #     "title": "Fresh strawberry",
    #     "type": "fruit",
    # }
    # # print(product_handler.add_product(products, **new_product))
    # print(product_handler.add_product([], **new_product))
    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]

    print(tab_handler.calculate_tab(table_1))
    print(tab_handler.calculate_tab(table_2))
    print("Fim")
