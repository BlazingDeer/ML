price=123
bonus=23
bonus_granted=False
price-= bonus if bonus_granted else 0
print(price)


rating=3
print("very good") if rating==5 else print("good") if rating==4 else print("weak")