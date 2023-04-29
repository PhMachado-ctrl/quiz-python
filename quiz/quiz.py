print("Começar o Quiz ? (S|N) \n")
choose = input("R: ") #choose recebe o qye escrever no input

if choose != "S" or choose !="s":
    quit() #Fechar a execução

print("iniciando...")
print("Qual Empresa Criou Grand Theft Auto ? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
answer_1 = input("R: ")

if answer_1 == "A" or answer_1 == "a":
    print("Correct!")
