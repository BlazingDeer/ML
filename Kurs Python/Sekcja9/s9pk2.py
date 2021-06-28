class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers

    def __getitem__(self, item):
        if item> len( self.products)*len( self.promotions)*len( self.customers):
            raise StopIteration()

        pos_products=int(item/(len( self.promotions)*len( self.customers)))
        item=int(item%(len( self.promotions)*len( self.customers)))
        pos_promotions=int(item/len( self.customers))
        item=int(item%len( self.customers))
        pos_customers=item

        return (self.products[pos_products],self.promotions[pos_promotions],self.customers[pos_customers])



products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 6)]

combinations = Combinations(products, promotions, customers)

#for i in range(0,31):
    #print(combinations[i])

it=iter(combinations)
for c in it:
    pass