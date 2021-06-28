class Cake:
    """Class describing properties of a Cake"""
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        """
        name - string name of a cake
        kind - string what kind of cake
        taste - string how the cake tastes like
        additives - list of addictions of the cake
        filling - string filling of a cake
        """

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        """Prints formatted info about object"""
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    @property
    def full_name(self):
        """Returns formatted name and kind of the cake"""
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)

help(Cake)
help(Cake.full_name)