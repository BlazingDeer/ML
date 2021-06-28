class cake():
    known_types= ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer=[]
    def __init__(self, name,kind,taste,addictions,filling):
        if(kind in self.known_types ):
            self.kind = kind
        else:
            self.kind='other'
        self.name=name
        self.taste=taste
        self.addictions=addictions
        self.filling=filling
        self.bakery_offer.append(self)


    def show_info(self):
        print(f"{self.name.title()} -({self.kind}) {self.taste}, {self.filling}")
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


cake01=cake("wafel kakaowy","wafel","kakao",["czekolada"],"krem")
print(f"Is cake01 an instance of cake = {isinstance(cake01,cake)}")
print(f"Vars of cake01: {vars(cake01)}")
print(f"Dir of cake01: {dir(cake01)}")