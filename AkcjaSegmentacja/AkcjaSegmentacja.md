# Akcja segmentacja 
## Cel 
Celem wyzwania jest wykorzystanie uczenia nienadzorowanego do wykonania segmentacji klientów
## Środowisko
Wykorzystaj Jupyter Notebooka i język Pythona 
##  Opis zadania
1. Dla podanego pliku customers.csv z cechami opisującymi zachowania zakupowe klientów, należy za pomocą wybranego algorytmu uczenia nienadzorowanego wykonać segmentację klientów.
2. Należy się zastanowić czy wykonać skalowanie lub normalizacja danych oraz jak podejść do ewentualnych wartości odstających
3. W pliku customers.csv mamy 6 kolumn: 
    * CustomerID - unikalny identyfikator klienta
    * Profit - jaką profitowość przynosi klient, wartość bez jednostki, im wyższa wartość tym lepiej
    * Recency - ile dni temu było ostatnie zamówienie klienta, ilość w dniach, im niższa wartość tym lepiej
    * Frequency	 - jak często klient zamawiał produkty, wartość bez jednostki, im wyższa wartość tym lepiej
    * Monetary	- całkowita wartość zamówionych produktów przez klienta, jednostka PLN, im wyższa wartość tym lepiej
    * Variance - ilość różnorodnych produktów, które zostały zamówione przez klienta, wartość bez jednostki, im wyższa wartość tym lepiej


## Wynik
Jako wynik wyzwania należy przesłać plik customers.csv z uzupełnioną informacją w kolumnie SegmentId o nadanym mu segmencie przez wybrany algorytm uczenie nienadzorowanego. Swoją pracę udokumentuj w notebooku.
### Zadanie opcjonalne
Spróbuj nazwać uzyskane segmenty analizując dane klientów przydzielonych do poszczególnej grup i umieść te nazwy w kolumnie SegmentName. Np na podstawie ich zachowań zakupowych: klienci aktywni, nieaktywni, nowi, odchodzący, itp.


## Przydatne linki
Uczenie nienadzorowane:
https://en.wikipedia.org/wiki/Unsupervised_learning

Przykładowy opis segmentacji klientów:
https://towardsdatascience.com/customer-segmentation-with-machine-learning-a0ac8c3d4d84

Opis słowny segmentów: 
https://rfm.rsquaredacademy.com/articles/rfm-customer-level-data.html#segments
