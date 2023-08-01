def login (cadastros):
    
    email=input("email: ")
    senha=input("senha: ")

    for i in cadastros:
        acesso=""
        sem_acesso=""
        if i["email"]==email and i["senha"]==senha:
          acesso="acesso permitido"
        else:
            sem_acesso="acesso negado"
    if acesso !="":  
        print(acesso)     

    else: 
        print(sem_acesso)

    input()


