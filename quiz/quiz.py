import os #Importa a biblioteca do Sistema Operacional

score = 0

print("Começar o Quiz ? (S|N) \n")
choose = input("R: ") #choose get the input value
choose = choose.upper()

if choose != "S":
    quit() #Finish the execution

print("iniciando...")
print("Qual Empresa Criou Grand Theft Auto ? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
answer_1 = input("R: ")
answer_1 = answer_1.upper()

if answer_1 == "A":
    print("Correto!")
    score += 1
else:
    print("incorreto!")

print("Qual o nome do protagonista do jogo GTA San Andreas? \n (A) Carlos John \n (B) Carl Jonhson \n (C) Carl Jaqueline \n (D) Carlo Jonhson \n")
answer_2 = input("R: ")
answer_2 = answer_2.upper()

if answer_2 == "A" :
    print("Correto!")
    score += 1
else:
    print("incorreto!")

os.system('cls') #Limpa o Prompt de comando
print(f"O quiz acabou... pontuação: {score}/2")
