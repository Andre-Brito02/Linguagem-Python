list = []
list_par = []
list_impar = []

for i in range(1,21):
    numero = int(input("Digite um número: "))
    list.append(numero)
    
    if(numero %2 == 0):
        list_par.append(numero)
    else:
        list_impar.append(numero)
        
print(f"Vetor completo = {list}")
print(f"Vetor par = {list_par}")
print(f"Vetor impar = {list_impar}")
