import random


x = random.choice([True, False])
p = False
if x != p:
    p = "blanc"
    x = "noir"
else:
    p = "noir"
    x = "blanc"

print(p , x)
