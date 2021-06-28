class cake():
    def __init__(self, name,kind,taste,addictions,filling):
        self.name=name
        self.kind=kind
        self.taste=taste
        self.addictions=addictions
        self.filling=filling

    def show_info(self):
        print(f"{self.name.title()} - {self.taste}, {self.filling}")
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



cake1=cake("Vanilla cake","Cake","Vanilla",["Chocolate","nuts"],"Cream")

cake1.show_info()
print(cake1.set_filling("Vanilla Cream"))
print(cake1.add_additives(["Sugar","Something"]))
cake1.show_info()