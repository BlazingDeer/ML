colors=["red","orange","green","violet","blue","yellow"]

def fun(colors,n):
    return colors[:n]

for i in range(len(colors)+1):
    print(fun(colors,i))

text="Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli."
nawias_otwarty=text.find("(")
nawias_zamkniety=text.find(")")

print(text[int(nawias_otwarty)+1:int(nawias_zamkniety)])