
from Frases_motivacionais import FrasesMotivacionais
from EscalaBeck import InventarioDeBeck
from cadastro import cadastros
from como_posso_ajudar import irformacao
from login import login



def Opcao(pessoas):
    opcao = int(input("Opcao: "))

    if opcao==1:
       InventarioDeBeck()
    elif opcao==2:
        FrasesMotivacionais()
    elif opcao==3:
        irformacao()
    elif opcao==4:
        pessoas=cadastros()
    elif opcao==5:
         login(cadastros)

    return pessoas
 