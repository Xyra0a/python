tax = 0.11

def totalAmount(subTotal):
    total = subTotal + (subTotal * tax)
    return total

print(totalAmount(100))