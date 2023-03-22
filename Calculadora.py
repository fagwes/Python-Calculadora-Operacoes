#Dados
a = float(input('Digite um número: '))
operacao = input('Escolha a operação: ')
b = (input('Digite um número: '))

# Soma #
if operacao == "+":
    if b == '':
        b = '0'

    b = float(b)

    soma = a + b
    print(soma)

# Subtração #

elif operacao == "-":
    if b == '':
        b = '0'

    b = float(b)

    subtracao = a - b
    print(subtracao)

# Multiplicação #

elif operacao == "*":
    if b == '':
        b = '0'

    b = float(b)

    multiplicacao = a * b
    print(multiplicacao)

# Divisão #

elif operacao == "/":
    if b == '':
        b = '0'

    b = float(b)

    divisao = a / b
    print(divisao)

# Porcentagem #

elif operacao == '%':
    if b == '':
        b = '0'
    b = float(b)
    calc = (a * b) / 100
    print(' {} \n '.format(calc, b, a))

# Potenciação #

elif operacao == '**':
    if b == '':
        b = '0'
    b = float(b)
    potenciacao = a ** b
    print(potenciacao)

# Raiz #
elif operacao == 'r':
    e = (input('O número estará elevado a (caso seja ele mesmo, deixe em branco): '))
    if e == '':
        e = '1'
    e = float(e)
    r = float(input('Qual a raiz? '))
    raiz = a**(e/r)
    print(raiz)

# Tabuada #

elif operacao == 't':
    print('------------ \n {} x 1 = {} \n {} x 2 = {} \n {} x 3 = {} \n {} x 4 = {} \n {} x 5 = {}'
          '\n {} x 6 = {} \n {} x 7 = {} \n {} x 8 = {} \n {} x 9 = {} \n {} x 10 = {} '
          '\n ------------'
          .format(a, a*1, a, a*2, a, a*3, a, a*4, a, a*5, a, a*6, a, a*7, a, a*8, a, a*9, a, a*10))
    
else:
    print('Operação não existente') 
    
    
    
