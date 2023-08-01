
def cadastros (pessoas):

 

  nome = input("Digite o nome: ")
  idade = int(input("Digite a idade: "))
  email = input("Digite o email: ")
  senha = input("senha: ")

  pessoa = {"nome": nome, "idade": idade, "email": email, "senha":senha}

  pessoas.append(pessoa)
  
  print("\033[0;32mCadastro Realizado com sucesso\033[m")

  return pessoas

input()