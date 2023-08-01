import tkinter as tk

psicologos = [
  {
    "nome": "João da Silva",
    "crp": "01/12345",
    "endereco": "Rua A, 123",
    "telefone": "(11) 1111-1111",
    "email": "joao@gmail.com"
  },
  {
    "nome": "Maria dos Santos",
    "crp": "02/23456",
    "endereco": "Rua B, 456",
    "telefone": "(22) 2222-2222",
    "email": "maria@gmail.com"
  },
  {
    "nome": "Pedro de Souza",
    "crp": "03/34567",
    "endereco": "Rua C, 789",
    "telefone": "(33) 3333-3333",
    "email": "pedro@gmail.com"
  }
]

def buscar_psicologo():
  nome = entry_nome.get()

  text_resultado.delete("1.0", tk.END)
  
  if nome == "":
    
    text_resultado.insert(tk.END, "Por favor, digite um nome válido.")
  else:
    
    resultado = ""
    
    for psicologo in psicologos:
      
      if nome.lower() in psicologo["nome"].lower():
        
        resultado += f"Nome: {psicologo['nome']}\n"
        resultado += f"CRP: {psicologo['crp']}\n"
        resultado += f"Telefone: {psicologo['telefone']}\n"
        resultado += f"E-mail: {psicologo['email']}\n"
        resultado += "\n"
    
    if resultado == "":
      
      text_resultado.insert(tk.END, f"Não foi encontrado nenhum psicólogo com o nome {nome}.")
    else:
      
      text_resultado.insert(tk.END, resultado)


window = tk.Tk()
window.title("Projeto Oásis")


frame_servicos = tk.Frame(window)
frame_servicos.pack()


label_titulo = tk.Label(frame_servicos, text="Serviços", font=("Arial", 24))
label_titulo.pack()


label_busca = tk.Label(frame_servicos, text="Busque um psicólogo pelo nome:", font=("Arial", 16))
label_busca.pack()


entry_nome = tk.Entry(frame_servicos)
entry_nome.pack()


button_buscar = tk.Button(frame_servicos, text="Buscar", command=buscar_psicologo)
button_buscar.pack()


text_resultado = tk.Text(frame_servicos)
text_resultado.pack()


window.mainloop()
