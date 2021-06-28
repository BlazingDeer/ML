odd_cubes = [value ** 3 for value in range( 1, 30, 2 )]
for value in odd_cubes:
    print( value )

print( odd_cubes[0:10:2] )

animals = ["sara", "dino", "lolek", "kot1", "kot2", "kot3"]
animals2 = animals.copy()
animals2[1] = "Dino"
animals2.append( "kot4" )
psy = animals[:3]
koty = animals[3:]
psy[0] = "Sara"
koty[0] = "Kot"
print( animals )
print( animals2 )
print( psy )
print( koty )
