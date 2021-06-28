from build_profile import build_profile as bp
from make_pizza import make_pizza as mp

mp( 16, "piczearki", "kurczak", "ser", "pomidory" )
user_profile = bp( "danil", "florek", miasto="serniki", panstwo="polska" )
print( user_profile )
