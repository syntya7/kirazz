from EscalaBeck import InventarioDeBeck
from Frases_motivacionais import FrasesMotivacionais
from cadastro import cadastros
from como_posso_ajudar import irformacao
from login import login
from menu import menu
from cadastro import cadastros

pessoas=[{"nome":"wagner","idade":18, "email":"@gmail.com", "senha":"1234"}]

while True:
   
    menu()
    opcao = int(input("Opcao: "))
   
    if opcao==1:
       InventarioDeBeck()
    elif opcao==2:
        FrasesMotivacionais()
    elif opcao==3:
        irformacao()
    elif opcao==4:
        pessoas=cadastros(pessoas)
    elif opcao==5:
        login(pessoas)
    elif opcao==0:
        print(" VOLTE SEMPRE !!!")
        break

    else:
        print(opcao)
        print("\033[1;31m Opção Inválida! Precione Enter\033[m")
    
    input()