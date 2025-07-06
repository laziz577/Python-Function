def is_even(number):
    return number % 2 == 0

def print_even_message(number):
    print(f"{number} juft son")

def print_odd_message(number):
    print(f"{number} toq son")

son = 9 
if is_even(son):
    print_even_message(son)
else:
    print_odd_message(son)

