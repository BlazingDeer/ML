class NoDuplicates:
    def __init__(self,lista):
        self.lista=lista

    def __call__(self, new_items):
        for item in new_items:
            if item not in self.lista:
                self.lista.append(item)
        print("self.lista =",self.lista)

my_no_dup_list=NoDuplicates(["keyboard","mouse"])
print(my_no_dup_list.lista)
my_no_dup_list(["keyboard","mouse","pendrive"])
my_no_dup_list(["pendrive","charger"])