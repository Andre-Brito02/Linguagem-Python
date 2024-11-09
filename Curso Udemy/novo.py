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

# calculadora = input("Digite uma operação(Exemplo: 5 + 6): ")
# partes = calculadora.split()

# num1 = int(partes[0])
# num2 = int(partes[2])

# if '+' in calculadora:
#     print(f'Resultado da soma = {num1 + num2}')
# elif '-' in calculadora:
#     print(f'Resultado da subtração = {num1 - num2}')
# elif '*' in calculadora:
#     print(f'Resultado da multiplicação = {num1 * num2}')
# elif '/' in calculadora:
#     print(f'Resultado da divisão = {num1 / num2:.2f}')

# num = int(input("Digite um número: "))
# num_inicial = num
# fatorial = 1

# if num < 0:
#     print("Números negativos não são permitidos!")
# else:
#     while(num > 0):
#         fatorial *= num
#         num -= 1

# print(f"Resultado do fatorial de {num_inicial} é {fatorial}")

vogais = ['a', 'e', 'i', 'o', 'u']
vogais_utilizadas = []
consoantes_utilizadas = []
contador = 0
qtd_vogais = 0
qtd_consoantes = 0

frase = input("Digite uma frase: ")

while True:
    if contador == len(frase):
        break
    
    for i in range(len(frase)):
        if frase[i] in vogais:
            vogais_utilizadas.append(frase[i])
            contador += 1
        else:
            consoantes_utilizadas.append(frase[i])
            contador += 1

if ' ' in consoantes_utilizadas:
    consoantes_utilizadas.remove(' ')

qtd_vogais = len(vogais_utilizadas)
qtd_consoantes = len(consoantes_utilizadas)

print(f"\nFrase: {frase}")
print(f'Vogais utilizadas: {vogais_utilizadas}')
print(f'Consoantes utilizadas: {consoantes_utilizadas}')
print(f'Quantidade de vogais utilizadas: {qtd_vogais}')
print(f'Quantidade de Consoantes utilizadas: {qtd_consoantes}')

# vogais = ['a', 'e', 'i', 'o', 'u']
# consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
# vogais_utilizadas = {}
# consoantes_utilizadas = {}

# frase = input("Digite uma frase: ").lower()

# for char in frase:
#     if char in vogais:
#         if char in vogais_utilizadas:
#             vogais_utilizadas[char] += 1
#         else:
#             vogais_utilizadas[char] = 1
#     elif char in consoantes:
#         if char in consoantes_utilizadas:
#             consoantes_utilizadas[char] += 1
#         else:
#             consoantes_utilizadas[char] = 1

# print(f"\nFrase: {frase}")
# print(f'Vogais utilizadas: {vogais_utilizadas}')
# print(f'Consoantes utilizadas: {consoantes_utilizadas}')
