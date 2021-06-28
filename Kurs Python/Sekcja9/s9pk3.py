import csv

with open('./plik.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #for row in csvreader:
        #print('|'.join(row))
    while True:
        try:
            print(", ".join(next(csvreader)))
        except StopIteration:
            break


