def qushish(a,b):
    result = a + b 
    return result

def ayirish(a,b):
    result = a - b 
    return result

def kupaytirish(a,b):
    result = a * b 
    return result

def bulish(a,b):
    result = a / b 
    return result

def main():
    a = float(input("a = "))
    b = float(input("b = "))

op = input("amal(+,-,*,/:)")

if op == '+':
    print(qushish)