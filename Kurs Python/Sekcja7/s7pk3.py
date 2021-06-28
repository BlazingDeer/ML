class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
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

    def __str__(self):
        message="-"*15+f"\n{self.name} - {self.kind}\nAdditives: {self.additives}"
        return message

    def __iadd__(self, other):
        if isinstance(other,str):
            if other not in self.additives:
                self.additives.append(other)
            return self
        elif isinstance(other,list):
            for item in other:
                if item not in self.additives:
                    self.additives.append(item)
            return self
        else:
            raise Exception(f"Wrong type of argument - {type(other)}")


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
print(cake01)
cake01+="cream"
print(cake01)
cake01+=['chocolade', 'nuts',"strawberries"]
print(cake01)
#cake01+=1
