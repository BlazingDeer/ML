ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

connections=[(p1,p2) for p1 in ports for p2 in ports]
print(connections)
print(len(connections))

connections=[(p1,p2) for p1 in ports for p2 in ports if p1!=p2]
print(connections)
print(len(connections))

connections=[(p1,p2) for i,p1 in enumerate(ports) for p2 in ports[i+1:]]
print(connections)
print(len(connections))

connections=[(p1,p2) for p1 in ports for p2 in ports if p1<p2]
print(connections)
print(len(connections))
