class cake():
    known_types= ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer=[]
    def __init__(self, name,kind,taste,addictions,filling,gluten_free,text):
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind='other'
        self.name=name
        self.taste=taste
        self.addictions=addictions
        self.filling=filling
        self.bakery_offer.append(self)
        self.__gluten_free=gluten_free
        self.__text=""
        self.Text=text

    def __Get_text(self):
        return self.__text
    def __Set_text(self,text):
        if self.kind=="cake" or text=="":
            self.__text=text
        else:
            self.__text=""
            print("Text can only be set if kind='cake'")

    Text=property(__Get_text,__Set_text,None,"Text to be written on a cake")

    def show_info(self):
        print(f"{self.name.title()} -({self.kind}) {self.taste}, {self.filling}")
        print(f"Gluten free - {self.__gluten_free}")
        print(f"Text - {self.__text}")
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

cake01=cake("wafel kakaowy","wafel","kakao",["czekolada"],"krem",True,"Napis jakis")
cake01.Text="wefel"
cake01.show_info()
cake02=cake("tort waniliowy","cake","wanilia",["czekolada","krem waniliowy"],"krem",True,"Napis jakis")
cake02.show_info()
cake02.Text="urodziny"
cake02.show_info()