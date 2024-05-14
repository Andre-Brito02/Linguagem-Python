import colorama
import random as rd
from colorama import Fore

colorama.init()

def introducao():
    print(Fore.BLACK + 'Enquanto viajavam por paisagens devastadas e enfrentavam perigos constantes, eles se depararam com uma transmissão de rádio misteriosa que falava de um lugar chamado "Nova Aurora".')
    print(Fore.BLACK + 'Rumores diziam que era uma comunidade isolada que havia conseguido se reerguer e oferecia segurança e prosperidade para aqueles que conseguissem chegar lá.')
    print(Fore.BLACK + 'Impulsionados pela esperança de uma vida melhor, o grupo decidiu embarcar em uma jornada perigosa para encontrar Nova Aurora.')
    print(Fore.WHITE + "No caminho para Nova Aurora, vocês são atacados por uma criatura")

def combate(personagem, vida_monstro):
    #Combate Emma
    if(personagem.capitalize() == 'Emma'):
        vida = 60
        ataque_inicial = 5
        bool = True
        while(bool):
            dado = rd.randrange(1,21)
            print(Fore.WHITE + f"Você tirou {dado} no dado")

            if(dado == 20):
                cmd_ataque = input(Fore.CYAN + "Pressione a para atacar: ")
                if(cmd_ataque.lower() == 'a'):
                    meu_ataque = rd.randrange(5,11) + ataque_inicial
                    vida_monstro -= meu_ataque
                    ataque_monstro = rd.randrange(1,6)
                    vida -= ataque_monstro
                    print(Fore.GREEN + f"Você causou {meu_ataque} de dano e está com {vida} de vida")
                    print(Fore.RED + f"O monstro causou {ataque_monstro} de dano e está com {vida_monstro} de vida")

                    if(vida_monstro <= 0 and vida <= 0):
                        print(Fore.YELLOW + "Ambos morreram")
                        bool = False
                        break
                    elif(vida_monstro <= 0):
                        print(Fore.BLUE + "A criatura morreu")
                        bool = False
                        break
                    elif(vida <= 0):
                        print(Fore.GREEN + "Você morreu")
                        bool = False
                        break

            elif(dado >= 12 and dado <= 19):
                cmd_ataque = input(Fore.CYAN + "Pressione a para atacar: ")
                if(cmd_ataque.lower() == 'a'):
                    meu_ataque = rd.randrange(4,10) + ataque_inicial
                    vida_monstro -= meu_ataque
                    ataque_monstro = rd.randrange(2,8)
                    vida -= ataque_monstro
                    print(Fore.GREEN + f"Você causou {meu_ataque} de dano e está com {vida} de vida")
                    print(Fore.RED + f"O monstro causou {ataque_monstro} de dano e está com {vida_monstro} de vida")

                    if(vida_monstro <= 0 and vida <= 0):
                        print(Fore.YELLOW + "Ambos morreram")
                        bool = False
                        break
                    elif(vida_monstro <= 0):
                        print(Fore.BLUE + "A criatura morreu")
                        bool = False
                        break
                    elif(vida <= 0):
                        print(Fore.GREEN + "Você morreu")
                        bool = False
                        break

            elif(dado >= 2 and dado <= 11):
                cmd_ataque = input(Fore.CYAN + "Pressione a para atacar: ")
                if(cmd_ataque.lower() == 'a'):
                    meu_ataque = rd.randrange(2,8) + ataque_inicial
                    vida_monstro -= meu_ataque
                    ataque_monstro = rd.randrange(4,10)
                    vida -= ataque_monstro
                    print(Fore.GREEN + f"Você causou {meu_ataque} de dano e está com {vida} de vida")
                    print(Fore.RED + f"O monstro causou {ataque_monstro} de dano e está com {vida_monstro} de vida")

                    if(vida_monstro <= 0 and vida <= 0):
                        print(Fore.YELLOW + "Ambos morreram")
                        bool = False
                        break
                    elif(vida_monstro <= 0):
                        print(Fore.BLUE + "A criatura morreu")
                        bool = False
                        break
                    elif(vida <= 0):
                        print(Fore.GREEN + "Você morreu")
                        bool = False
                        break

            elif(dado == 1):
                cmd_ataque = input(Fore.CYAN + "Pressione a para atacar: ")
                if(cmd_ataque.lower() == 'a'):
                    meu_ataque = rd.randrange(1,5) + ataque_inicial
                    vida_monstro -= meu_ataque
                    ataque_monstro = rd.randrange(5,11)
                    vida -= ataque_monstro
                    print(Fore.GREEN + f"Você causou {meu_ataque} de dano e está com {vida} de vida")
                    print(Fore.RED + f"O monstro causou {ataque_monstro} de dano e está com {vida_monstro} de vida")

                    if(vida_monstro <= 0 and vida <= 0):
                        print(Fore.YELLOW + "Ambos morreram")
                        bool = False
                        break
                    elif(vida_monstro <= 0):
                        print(Fore.BLUE + "A criatura morreu")
                        bool = False
                        break
                    elif(vida <= 0):
                        print(Fore.GREEN + "Você morreu")
                        bool = False
                        break
    #Combate Jack
    if(personagem.capitalize() == 'Jack'):
        vida = 70
        ataque_inicial = 10
        bool = True
        while(bool):
            dado = rd.randrange(1,21)
            print(Fore.WHITE + f"Você tirou {dado} no dado")

            if(dado == 20):
                cmd_ataque = input(Fore.CYAN + "Pressione a para atacar: ")
                if(cmd_ataque.lower() == 'a'):
                    meu_ataque = rd.randrange(5,11) + ataque_inicial
                    vida_monstro -= meu_ataque
                    ataque_monstro = rd.randrange(1,6)
                    vida -= ataque_monstro
                    print(Fore.GREEN + f"Você causou {meu_ataque} de dano e está com {vida} de vida")
                    print(Fore.RED + f"O monstro causou {ataque_monstro} de dano e está com {vida_monstro} de vida")

                    if(vida_monstro <= 0 and vida <= 0):
                        print(Fore.YELLOW + "Ambos morreram")
                        bool = False
                        break
                    elif(vida_monstro <= 0):
                        print(Fore.BLUE + "A criatura morreu")
                        bool = False
                        break
                    elif(vida <= 0):
                        print(Fore.GREEN + "Você morreu")
                        bool = False
                        break

            elif(dado >= 12 and dado <= 19):
                cmd_ataque = input(Fore.CYAN + "Pressione a para atacar: ")
                if(cmd_ataque.lower() == 'a'):
                    meu_ataque = rd.randrange(4,10) + ataque_inicial
                    vida_monstro -= meu_ataque
                    ataque_monstro = rd.randrange(2,8)
                    vida -= ataque_monstro
                    print(Fore.GREEN + f"Você causou {meu_ataque} de dano e está com {vida} de vida")
                    print(Fore.RED + f"O monstro causou {ataque_monstro} de dano e está com {vida_monstro} de vida")

                    if(vida_monstro <= 0 and vida <= 0):
                        print(Fore.YELLOW + "Ambos morreram")
                        bool = False
                        break
                    elif(vida_monstro <= 0):
                        print(Fore.BLUE + "A criatura morreu")
                        bool = False
                        break
                    elif(vida <= 0):
                        print(Fore.GREEN + "Você morreu")
                        bool = False
                        break

            elif(dado >= 2 and dado <= 11):
                cmd_ataque = input(Fore.CYAN + "Pressione a para atacar: ")
                if(cmd_ataque.lower() == 'a'):
                    meu_ataque = rd.randrange(2,8) + ataque_inicial
                    vida_monstro -= meu_ataque
                    ataque_monstro = rd.randrange(4,10)
                    vida -= ataque_monstro
                    print(Fore.GREEN + f"Você causou {meu_ataque} de dano e está com {vida} de vida")
                    print(Fore.RED + f"O monstro causou {ataque_monstro} de dano e está com {vida_monstro} de vida")

                    if(vida_monstro <= 0 and vida <= 0):
                        print(Fore.YELLOW + "Ambos morreram")
                        bool = False
                        break
                    elif(vida_monstro <= 0):
                        print(Fore.BLUE + "A criatura morreu")
                        bool = False
                        break
                    elif(vida <= 0):
                        print(Fore.GREEN + "Você morreu")
                        bool = False
                        break

            elif(dado == 1):
                cmd_ataque = input(Fore.CYAN + "Pressione a para atacar: ")
                if(cmd_ataque.lower() == 'a'):
                    meu_ataque = rd.randrange(1,5) + ataque_inicial
                    vida_monstro -= meu_ataque
                    ataque_monstro = rd.randrange(5,11)
                    vida -= ataque_monstro
                    print(Fore.GREEN + f"Você causou {meu_ataque} de dano e está com {vida} de vida")
                    print(Fore.RED + f"O monstro causou {ataque_monstro} de dano e está com {vida_monstro} de vida")

                    if(vida_monstro <= 0 and vida <= 0):
                        print(Fore.YELLOW + "Ambos morreram")
                        bool = False
                        break
                    elif(vida_monstro <= 0):
                        print(Fore.BLUE + "A criatura morreu")
                        bool = False
                        break
                    elif(vida <= 0):
                        print(Fore.GREEN + "Você morreu")
                        bool = False
                        break
    #Combate Sophia
    if(personagem.capitalize() == 'Sophia'):
        vida = 50
        ataque_inicial = 3
        bool = True
        while(bool):
            dado = rd.randrange(1,21)
            print(Fore.WHITE + f"Você tirou {dado} no dado")

            if(dado == 20):
                cmd_ataque = input(Fore.CYAN + "Pressione a para atacar: ")
                if(cmd_ataque.lower() == 'a'):
                    meu_ataque = rd.randrange(5,11) + ataque_inicial
                    vida_monstro -= meu_ataque
                    ataque_monstro = rd.randrange(1,6)
                    vida -= ataque_monstro
                    print(Fore.GREEN + f"Você causou {meu_ataque} de dano e está com {vida} de vida")
                    print(Fore.RED + f"O monstro causou {ataque_monstro} de dano e está com {vida_monstro} de vida")

                    if(vida_monstro <= 0 and vida <= 0):
                        print(Fore.YELLOW + "Ambos morreram")
                        bool = False
                        break
                    elif(vida_monstro <= 0):
                        print(Fore.BLUE + "A criatura morreu")
                        bool = False
                        break
                    elif(vida <= 0):
                        print(Fore.GREEN + "Você morreu")
                        bool = False
                        break

            elif(dado >= 12 and dado <= 19):
                cmd_ataque = input(Fore.CYAN + "Pressione a para atacar: ")
                if(cmd_ataque.lower() == 'a'):
                    meu_ataque = rd.randrange(4,10) + ataque_inicial
                    vida_monstro -= meu_ataque
                    ataque_monstro = rd.randrange(2,8)
                    vida -= ataque_monstro
                    print(Fore.GREEN + f"Você causou {meu_ataque} de dano e está com {vida} de vida")
                    print(Fore.RED + f"O monstro causou {ataque_monstro} de dano e está com {vida_monstro} de vida")

                    if(vida_monstro <= 0 and vida <= 0):
                        print(Fore.YELLOW + "Ambos morreram")
                        bool = False
                        break
                    elif(vida_monstro <= 0):
                        print(Fore.BLUE + "A criatura morreu")
                        bool = False
                        break
                    elif(vida <= 0):
                        print(Fore.GREEN + "Você morreu")
                        bool = False
                        break

            elif(dado >= 2 and dado <= 11):
                cmd_ataque = input(Fore.CYAN + "Pressione a para atacar: ")
                if(cmd_ataque.lower() == 'a'):
                    meu_ataque = rd.randrange(2,8) + ataque_inicial
                    vida_monstro -= meu_ataque
                    ataque_monstro = rd.randrange(4,10)
                    vida -= ataque_monstro
                    print(Fore.GREEN + f"Você causou {meu_ataque} de dano e está com {vida} de vida")
                    print(Fore.RED + f"O monstro causou {ataque_monstro} de dano e está com {vida_monstro} de vida")

                    if(vida_monstro <= 0 and vida <= 0):
                        print(Fore.YELLOW + "Ambos morreram")
                        bool = False
                        break
                    elif(vida_monstro <= 0):
                        print(Fore.BLUE + "A criatura morreu")
                        bool = False
                        break
                    elif(vida <= 0):
                        print(Fore.GREEN + "Você morreu")
                        bool = False
                        break

            elif(dado == 1):
                cmd_ataque = input(Fore.CYAN + "Pressione a para atacar: ")
                if(cmd_ataque.lower() == 'a'):
                    meu_ataque = rd.randrange(1,5) + ataque_inicial
                    vida_monstro -= meu_ataque
                    ataque_monstro = rd.randrange(5,11)
                    vida -= ataque_monstro
                    print(Fore.GREEN + f"Você causou {meu_ataque} de dano e está com {vida} de vida")
                    print(Fore.RED + f"O monstro causou {ataque_monstro} de dano e está com {vida_monstro} de vida")

                    if(vida_monstro <= 0 and vida <= 0):
                        print(Fore.YELLOW + "Ambos morreram")
                        bool = False
                        break
                    elif(vida_monstro <= 0):
                        print(Fore.BLUE + "A criatura morreu")
                        bool = False
                        break
                    elif(vida <= 0):
                        print(Fore.GREEN + "Você morreu")
                        bool = False
                        break
    #Combate Marcus
    if(personagem.capitalize() == 'Marcus'):
        vida = 65
        ataque_inicial = 8
        bool = True
        while(bool):
            dado = rd.randrange(1,21)
            print(Fore.WHITE + f"Você tirou {dado} no dado")

            if(dado == 20):
                cmd_ataque = input(Fore.CYAN + "Pressione a para atacar: ")
                if(cmd_ataque.lower() == 'a'):
                    meu_ataque = rd.randrange(5,11) + ataque_inicial
                    vida_monstro -= meu_ataque
                    ataque_monstro = rd.randrange(1,6)
                    vida -= ataque_monstro
                    print(Fore.GREEN + f"Você causou {meu_ataque} de dano e está com {vida} de vida")
                    print(Fore.RED + f"O monstro causou {ataque_monstro} de dano e está com {vida_monstro} de vida")

                    if(vida_monstro <= 0 and vida <= 0):
                        print(Fore.YELLOW + "Ambos morreram")
                        bool = False
                        break
                    elif(vida_monstro <= 0):
                        print(Fore.BLUE + "A criatura morreu")
                        bool = False
                        break
                    elif(vida <= 0):
                        print(Fore.GREEN + "Você morreu")
                        bool = False
                        break

            elif(dado >= 12 and dado <= 19):
                cmd_ataque = input(Fore.CYAN + "Pressione a para atacar: ")
                if(cmd_ataque.lower() == 'a'):
                    meu_ataque = rd.randrange(4,10) + ataque_inicial
                    vida_monstro -= meu_ataque
                    ataque_monstro = rd.randrange(2,8)
                    vida -= ataque_monstro
                    print(Fore.GREEN + f"Você causou {meu_ataque} de dano e está com {vida} de vida")
                    print(Fore.RED + f"O monstro causou {ataque_monstro} de dano e está com {vida_monstro} de vida")

                    if(vida_monstro <= 0 and vida <= 0):
                        print(Fore.YELLOW + "Ambos morreram")
                        bool = False
                        break
                    elif(vida_monstro <= 0):
                        print(Fore.BLUE + "A criatura morreu")
                        bool = False
                        break
                    elif(vida <= 0):
                        print(Fore.GREEN + "Você morreu")
                        bool = False
                        break

            elif(dado >= 2 and dado <= 11):
                cmd_ataque = input(Fore.CYAN + "Pressione a para atacar: ")
                if(cmd_ataque.lower() == 'a'):
                    meu_ataque = rd.randrange(2,8) + ataque_inicial
                    vida_monstro -= meu_ataque
                    ataque_monstro = rd.randrange(4,10)
                    vida -= ataque_monstro
                    print(Fore.GREEN + f"Você causou {meu_ataque} de dano e está com {vida} de vida")
                    print(Fore.RED + f"O monstro causou {ataque_monstro} de dano e está com {vida_monstro} de vida")

                    if(vida_monstro <= 0 and vida <= 0):
                        print(Fore.YELLOW + "Ambos morreram")
                        bool = False
                        break
                    elif(vida_monstro <= 0):
                        print(Fore.BLUE + "A criatura morreu")
                        bool = False
                        break
                    elif(vida <= 0):
                        print(Fore.GREEN + "Você morreu")
                        bool = False
                        break

            elif(dado == 1):
                cmd_ataque = input(Fore.CYAN + "Pressione a para atacar: ")
                if(cmd_ataque.lower() == 'a'):
                    meu_ataque = rd.randrange(1,5) + ataque_inicial
                    vida_monstro -= meu_ataque
                    ataque_monstro = rd.randrange(5,11)
                    vida -= ataque_monstro
                    print(Fore.GREEN + f"Você causou {meu_ataque} de dano e está com {vida} de vida")
                    print(Fore.RED + f"O monstro causou {ataque_monstro} de dano e está com {vida_monstro} de vida")

                    if(vida_monstro <= 0 and vida <= 0):
                        print(Fore.YELLOW + "Ambos morreram")
                        bool = False
                        break
                    elif(vida_monstro <= 0):
                        print(Fore.BLUE + "A criatura morreu")
                        bool = False
                        break
                    elif(vida <= 0):
                        print(Fore.GREEN + "Você morreu")
                        bool = False
                        break
    return vida


print(Fore.BLACK + "Após uma guerra global que deixou o mundo em ruínas, a sociedade humana entrou em colapso. Cidades outrora movimentadas foram reduzidas a escombros, e a civilização entrou em um estado de caos. Recursos básicos como água e comida se tornaram escassos, e criaturas violentas surgiram.") 
print(Fore.WHITE + "Seu grupo é composto por: ")    
print(Fore.LIGHTMAGENTA_EX + "Emma, uma ex-médica")
print(Fore.BLUE + "Jack, um ex-militar especialista em combate")
print(Fore.CYAN + "Sophia, uma engenheira habilidosa")
print(Fore.LIGHTGREEN_EX + "Marcus, um caçador experiente.")
personagem = input(Fore.WHITE + "Escolha seu personagem: ")
vida_monstro = 60

introducao()
vida = combate(personagem, vida_monstro)
print(vida)
colorama.deinit()