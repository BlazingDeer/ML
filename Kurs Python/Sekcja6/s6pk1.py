class cake():
    def __init__(self, name,kind,taste,addictions,filling):
        self.name=name
        self.kind=kind
        self.taste=taste
        self.addictions=addictions
        self.filling=filling


cake1=cake("sernik","ciasto","dobry",["twaróg"],"twaróg")
cake2=cake("ciasto2","ciasto","zle",["gorzka czekolada"],"brak")
cake3=cake("ciasto3","ciasto","slodkie",["bita smietana"],"bita smietana")
bakery_offer=[cake1,cake2,cake3]

for cake in bakery_offer:
    print(f"{cake.name} - ({cake.kind}) main taste: {cake.taste} with additives of {cake.addictions}, filled with {cake.filling}")
