def Combinations(products, promotions, customers):
        for product in products:
            for promotion in promotions:
                for customer in customers:
                    item_to_return = "{} - {} -{}".format(product, promotion, customer)
                    yield(item_to_return)

products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 2)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]

combinations = Combinations(products, promotions, customers)

for c in combinations:
    print(c)