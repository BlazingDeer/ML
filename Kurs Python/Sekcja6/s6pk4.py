class cake():
    known_types= ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer=[]
    def __init__(self, name,kind,taste,addictions,filling,gluten_free):
        if(kind in self.known_types ):
            self.kind = kind
        else:
            self.kind='other'
        self.name=name
        self.taste=taste
        self.addictions=addictions
        self.filling=filling
        self.bakery_offer.append(self)
        self.__gluten_free=gluten_free


    def show_info(self):
        print(f"{self.name.title()} -({self.kind}) {self.taste}, {self.filling}")
        print(f"Gluten free - {self.__gluten_free}")
        if self.addictions:
            print("Addictions:")
            for a in self.addictions:
                print(a)
        print("-"*20)

    def set_filling(self,filling):
        self.filling=filling
        return self.filling

    def add_additives(self,additives):
        self.addictions+=additives
        return self.addictions


cake01=cake("wafel kakaowy","wafel","kakao",["czekolada"],"krem",True)
cake01.__gluten_free=False
cake01.show_info()
print(dir(cake01))
cake01._cake__gluten_free=False
cake01.show_info()

