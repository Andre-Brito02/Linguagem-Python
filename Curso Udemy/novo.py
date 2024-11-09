# id = 'indiozinhos'
# nums = []

# for i in range(1, 11): 
#     nums.append(i)

# for i in range(0,9):
#     print(nums[i], end=' ')
#     if nums[i] %3 == 0:
#         print(id)

# print(nums[-1], 'no pequeno bote')

# for i in range(1, 6):
#     print('1 ' * i)

# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite um número: "))
# print("'+': soma\n'-': subtração\n'*': multiplicação\n'/': divisão")
# operacao = input("Digite a operação: ")
# print()

# if operacao == '+':
#     print(f'Resultado da soma = {num1 + num2}')
# elif operacao == '-':
#     print(f'Resultado da subtração = {num1 - num2}')
# elif operacao == '*':
#     print(f'Resultado da multiplicação = {num1 * num2}')
# elif operacao == '/':
#     print(f'Resultado da divisão = {num1 / num2}')

calculadora = input("Digite uma operação(Exemplo: 5 + 6): ")
partes = calculadora.split()

num1 = int(partes[0])
num2 = int(partes[2])

if '+' in calculadora:
    print(f'Resultado da soma = {num1 + num2}')
elif '-' in calculadora:
    print(f'Resultado da subtração = {num1 - num2}')
elif '*' in calculadora:
    print(f'Resultado da multiplicação = {num1 * num2}')
elif '/' in calculadora:
    print(f'Resultado da divisão = {num1 / num2:.2f}')
