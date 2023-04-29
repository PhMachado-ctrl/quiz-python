print("Começar o Quiz ? (S|N) \n")
choose = input("R: ") #choose get the input value
choose = choose.upper()

if choose != "S":
    quit() #Finish the execution

print("iniciando...")
print("Qual Empresa Criou Grand Theft Auto ? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
answer_1 = input("R: ")

if answer_1 == "A" or answer_1 == "a":
    print("Correto!")
else:
    print("incorreto!")
