def make_pizza(size, *toppings):
    print( toppings )
    print( f"Robie {size}-centymetrowa pizze z nastepujacymi skladnikami:" )
    for topping in toppings:
        print( f"- {topping}" )
