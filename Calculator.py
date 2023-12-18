

while True:
    def sum(a , b):
        return a + b
    def mul(a , b):
        return a * b
    def pow(a , b):
        return a ** b
    def diff(a , b):
        if a > b:
            return a - b
        else: 
            return b - a
    def div(a , b):
        if a >= b:
            return a / b
        else :
            return b / a
    def percent(a, b):
        return (a/100)*b
    a = int(input('Enter the Number: '))
    b = int(input('Enter the Number: '))
    c = input('Enter the Operator: ')
    if c == '+':
        print(f' The sum of {a} and {b} is {sum(a , b)}')
    elif c == '*':
        print(f'The product of {a} and {b} is {mul(a, b)}')
    elif c == '**':
        print(f'{a} to the power {b} is {pow(a , b)}')
    elif c == '-':
        if a > b:
            print(f'The difference between {a} and {b} is {diff(a , b)}')
        else:
            print(f'The difference between {b} and {a} is {diff(a , b)}')
    elif c == '/':
        if a >= b:
            print(f'The division of {a} and {b} is {div(a , b)}')
        else:
            print(f'The division of {b} and {a} is {div(a , b)}') 
    elif c == '%':
        print(f'{a} % of {b} is {percent(a , b)}')  
    else:
        print('Invalid Operator')