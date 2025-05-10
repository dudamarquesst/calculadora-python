def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero."
    return a / b

def menu():
    print('\nCalculadora em phyton')
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('0 - Sair')

while True:
    menu()
    escolha = input('Escolha uma das opções: ')
    
    if escolha == '0':
        print('Encerrando...')
        break

    if escolha not in ['1', '2', '3', '4']:
        print('Opção inválida')
        continue

    try:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
    except ValueError:
        print('Entrada inválida, digite apenas números.')
        continue

    if escolha == '1':
        resultado = somar(num1, num2)
    elif escolha == '2':
        resultado = subtrair(num1, num2)
    elif escolha == '3':
        resultado = multiplicar(num1, num2)
    elif escolha == '4':
        resultado = dividir(num1, num2)

    print("Resultado:", resultado)
    print("-" * 30)
    