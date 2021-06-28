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

    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)

class SpecialCake(Cake):
    def __init__(self,name, kind, taste, additives, filling,ocassion,shape,ornaments,text):
        super().__init__(name,kind,taste,additives,filling)
        self.occasion=ocassion
        self.shape=shape
        self.ornaments=ornaments
        self.text=text

    def show_info(self):
        super().show_info()
        print(f"Occassion:     {self.occasion}")
        print(f"Shape:         {self.shape}")
        print(f"Ornaments:     {self.ornaments}")
        print(f"Text:          {self.text}")
        print("\n","="*25)

cake1=Cake("ciasto1","ciasto","slodkie",["czekolada"],"bita smietana")
special_cake01=SpecialCake("Sernik","Ciasto","sernikowate",["rodzynki","twarog"],"twarog",
                           "Birthday","walec","swieczki","happy birthday")
special_cake02=SpecialCake("Wz","Ciasto","słodkie",["bita smietana","czekolada"],"bita smietana",
                           "Wedding","prostakat","None","kobieta + mezczyzna")

#special_cake01.show_info()
#special_cake02.show_info()

for cake in Cake.bakery_offer:
    print(cake.full_name)
    cake.show_info()