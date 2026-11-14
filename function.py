def calculate_sum(a,b):
    print(a + b)

my_sum = calculate_sum(2, 7)
print(my_sum) #Default return of an function is None

tax_rate = 0.1

def calculate_tax(price):
    tax = price * tax_rate
    return tax

print(calculate_tax(50)) # 5.0
print(tax_rate) # 0.1
#print(tax) # NameError: name 'tax' is not defined