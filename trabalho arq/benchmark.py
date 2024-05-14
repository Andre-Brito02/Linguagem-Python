import time # Necessário para utilizar a função que calcula o tempo
import math # Necessário para utilizar as funções trigonométricas
import psutil # Necessário para monitorar o uso de processador e memória

def seno():
    print("------------Função seno------------") # Melhoria na exibição
    # Criar uma variável que calcula o tempo inicial
    tempoInicial = time.time()

    # Criar uma lista para armazenar os valores do seno
    valorSeno = []

    # Obtém o uso de memória antes do loop
    process = psutil.Process() #Variável criada para obter informações sobre o processo Python atual(programa que está sendo executando)
    usoMemoriaAntes = process.memory_info().rss # Variável criada para obter a quantidade de memória residente usada pelo processo.  
    # RSS é a quantidade de memória fisicamente residente (não trocada para disco) ocupada pelo processo.

    # Variável criada para armazenar o valor do uso do processador antes do laço
    usoCPUAntes = psutil.cpu_percent(interval=1)

    # Laço for para calcular os valores do seno
    for angulo in range(0, 10000): # Laço for para pegar os valores de 0 a 10001
        radiano = math.radians(angulo) # Converte graus para radianos
        valorSeno.append(math.sin(radiano)) # Calcula o seno e adiciona à lista

    # Obtém o uso de memória depois do loop
    usoMemoriaDepois = process.memory_info().rss

    # Uso do processador depois do loop
    usoCPUDepois = psutil.cpu_percent(interval=1)

    # Criar uma variável para representar o fim da medição do tempo
    tempoFinal = time.time()

    # Calcula a diferença de memória antes e depois do calculo
    memoriaUsada = usoMemoriaDepois - usoMemoriaAntes

    # Calcular o tempo total de execução
    tempoTotal = tempoFinal - tempoInicial

     # Exibir o tempo de execução
    print(f"Tempo de execução: {tempoTotal:.5f} segundos") 
    # Exibir o uso de memória em MB
    print(f"Uso de memória: {memoriaUsada / (1024 * 1024):.5f} MB") 
    # Exibir o uso da CPU antes e depois do laço 
    print(f"Uso de CPU: {usoCPUAntes}%, {usoCPUDepois}%")
    print("-----------------------------------") # Melhoria na exibição
    print() # Pular uma linha

def cosseno():
    print("------------Função Cosseno------------") # Melhoria na exibição
    # Criar uma variável que calcula o tempo inicial
    tempoInicial = time.time()

    # Criar uma lista para armazenar os valores do Cosseno
    valorCosseno = []

    # Obtém o uso de memória antes do loop
    process = psutil.Process() #Variável criada para obter informações sobre o processo Python atual(programa que está sendo executando)
    usoMemoriaAntes = process.memory_info().rss # Variável criada para obter a quantidade de memória residente usada pelo processo.  
    # RSS é a quantidade de memória fisicamente residente (não trocada para disco) ocupada pelo processo.

    # Variável criada para armazenar o valor do uso do processador antes do laço
    usoCPUAntes = psutil.cpu_percent(interval=1)

    # Laço for para calcular os valores do seno
    for angulo in range(0, 15000): # Laço for para pegar os valores de 0 a 10001 
        radiano = math.radians(angulo) # Converte graus para radianos
        valorCosseno.append(math.cos(radiano)) # Calcula o seno e adiciona à lista

    # Obtém o uso de memória depois do loop
    usoMemoriaDepois = process.memory_info().rss

    # Uso do processador depois do loop
    usoCPUDepois = psutil.cpu_percent(interval=1)

    # Criar uma variável para representar o fim da medição do tempo
    tempoFinal = time.time()

    # Calcula a diferença de memória antes e depois do calculo
    memoriaUsada = usoMemoriaDepois - usoMemoriaAntes

    # Calcular o tempo total de execução
    tempoTotal = tempoFinal - tempoInicial

     # Exibir o tempo de execução
    print(f"Tempo de execução: {tempoTotal:.5f} segundos") 
    # Exibir o uso de memória em MB
    print(f"Uso de memória: {memoriaUsada / (1024 * 1024):.5f} MB")
    # Exibir o uso da CPU antes e depois do laço 
    print(f"Uso de CPU: {usoCPUAntes}%, {usoCPUDepois}%")
    print("--------------------------------------") # Melhoria na exibição
    print() # Pular uma linha

def tangente():
    print("------------Função Tangente------------") # Melhoria na exibição
    # Criar uma variável que calcula o tempo inicial
    tempoInicial = time.time()

    # Criar uma lista para armazenar os valores da tangente
    valorTangente = []

    # Obtém o uso de memória antes do loop
    process = psutil.Process() #Variável criada para obter informações sobre o processo Python atual(programa que está sendo executando)
    usoMemoriaAntes = process.memory_info().rss # Variável criada para obter a quantidade de memória residente usada pelo processo.  
    # RSS é a quantidade de memória fisicamente residente (não trocada para disco) ocupada pelo processo.

    # Variável criada para armazenar o valor do uso do processador antes do laço
    usoCPUAntes = psutil.cpu_percent(interval=1) # método que retorna a percentagem de utilização da CPU no período de tempo especificado pelo parâmetro interval

    # Laço for para calcular os valores do seno
    for angulo in range(0, 20000): # Laço for para pegar os valores de 0 a 10001 
        radiano = math.radians(angulo) # Converte graus para radianos
        valorTangente.append(math.tan(radiano)) # Calcula o seno e adiciona à lista

    # Obtém o uso de memória depois do loop
    usoMemoriaDepois = process.memory_info().rss

    # Uso do processador depois do loop
    usoCPUDepois = psutil.cpu_percent(interval=1)

    # Criar uma variável para representar o fim da medição do tempo
    tempoFinal = time.time()

    # Calcula a diferença de memória antes e depois do calculo
    memoriaUsada = usoMemoriaDepois - usoMemoriaAntes

    # Calcular o tempo total de execução
    tempoTotal = tempoFinal - tempoInicial

    # Exibir o tempo de execução
    print(f"Tempo de execução: {tempoTotal:.5f} segundos") 
    # Exibir o uso de memória em MB
    print(f"Uso de memória: {memoriaUsada / (1024 * 1024):.5f} MB") 
    # Exibir o uso da CPU antes e depois do laço 
    print(f"Uso de CPU: {usoCPUAntes}%, {usoCPUDepois}%")
    print("---------------------------------------") # Melhoria na exibição
    print() # Pular uma linha

# Chamar a função seno
seno()
# Chamar a função cosseno
cosseno()
# Chamar a função tangente
tangente()