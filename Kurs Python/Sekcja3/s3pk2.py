ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

connections_gen=((p1, p2) for p1 in ports for p2 in ports)
connections_len=0
for con in connections_gen:
    print(con,end=" ")
    connections_len+=1

print("\n",connections_len)

connections_gen=((p1,p2) for p1 in ports for p2 in ports if p1!=p2)
connections_len = 0
for con in connections_gen:
    print(con,end=" ")
    connections_len += 1

print("\n",connections_len)


connections_gen=((p1,p2) for i,p1 in enumerate(ports) for p2 in ports[i+1:])
connections_len = 0
for con in connections_gen:
    print(con,end=" ")
    connections_len += 1

print("\n",connections_len)


connections_gen=((p1, p2) for p1 in ports for p2 in ports if p1 < p2)
connections_len = 0
for con in connections_gen:
    print(con,end=" ")
    connections_len += 1

print("\n",connections_len)
