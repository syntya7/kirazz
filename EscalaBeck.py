def InventarioDeBeck():
    indice_ansiedade = []
    print('''

Abaixo  está uma lista de sintomas comuns à ansiedade. Por favor, leia cuidadosamente cada 
item da lista. Identifique o quanto você tem sido incomodado(a) por cada um dos sintomas 
durante a última semana, incluindo hoje.

.....................................................................................................

    1°)Dormência ou  formigamento

    0-Absolutamente não
    1-Levemente(Não me incomodou muito)
    2-Moderadamente(Foi muito desagradável, mas pude suporta)
    3-Gravemente(Dificilmente pude suporta)
    
    ''')

    while True:
        resposta = int(input("Digite um numero de 0 á 3: "))
        if 0<=resposta<4:
            break
        else:
            print("Digite de 0 a 3")
    indice_ansiedade.append(resposta)
    print('''

...................................................................

    2°)Sensação de calor

    0-Absolutamente não
    1-Levemente(Não me incomodou muito)
    2-Moderadamente(Foi muito desagradável, mas pude suporta)
    3-Gravemente(Dificilmente pude suporta)
    
    ''')

    while True:
        resposta = int(input("Digite um numero de 0 á 3: "))
        if 0<=resposta<4:
            break
        else:
            print("Digite de 0 a 3")

    indice_ansiedade.append(resposta)
    print('''

.................................................................   

    3°)Tremores nas pernas

    0-Absolutamente não
    1-Levemente(Não me incomodou muito)
    2-Moderadamente(Foi muito desagradável, mas pude suporta)
    3-Gravemente(Dificilmente pude suporta)
    
    ''')

    while True:
        resposta = int(input("Digite um numero de 0 á 3: "))
        if 0<=resposta<4:
            break
        else:
            print("Digite de 0 a 3")

    indice_ansiedade.append(resposta)
    print('''

................................................................

    4°)Incapaz de relaxar
    
    0-Absolutamente não
    1-Levemente(Não me incomodou muito)
    2-Moderadamente(Foi muito desagradável, mas pude suporta)
    3-Gravemente(Dificilmente pude suporta)

     ''')

    while True:
        resposta = int(input("Digite um numero de 0 á 3: "))
        if 0<=resposta<4:
            break
        else:
            print("Digite de 0 a 3")

    indice_ansiedade.append(resposta)
    
    print('''

.................................................................

    5°)Medo que aconteça o pior

    0-Absolutamente não
    1-Levemente(Não me incomodou muito)
    2-Moderadamente(Foi muito desagradável, mas pude suporta)
    3-Gravemente(Dificilmente pude suporta)

    ''')

    while True:
        resposta = int(input("Digite um numero de 0 á 3: "))
        if 0<=resposta<4:
            break
        else:
            print("Digite de 0 a 3")

    indice_ansiedade.append(resposta)
    print('''

.................................................................

    6°)Atordoado (a) ou tonto (a)

    0-Absolutamente não
    1-Levemente(Não me incomodou muito)
    2-Moderadamente(Foi muito desagradável, mas pude suporta)
    3-Gravemente(Dificilmente pude suporta)

     ''')
    
    while True:
        resposta = int(input("Digite um numero de 0 á 3: "))
        if 0<=resposta<4:
            break
        else:
            print("Digite de 0 a 3")

    indice_ansiedade.append(resposta)
    

    print('''

.................................................................

    7°)Palpitação ou aceleração do coração

    0-Absolutamente não
    1-Levemente(Não me incomodou muito)
    2-Moderadamente(Foi muito desagradável, mas pude suporta)
    3-Gravemente(Dificilmente pude suporta)

     ''')
    
    
    while True:
        resposta = int(input("Digite um numero de 0 á 3: "))
        if 0<=resposta<4:
            break
        else:
            print("Digite de 0 a 3")

    indice_ansiedade.append(resposta)
    print('''

...................................................................

    8°)Sem equilíbrio/inseguro(a)

    0-Absolutamente não
    1-Levemente(Não me incomodou muito)
    2-Moderadamente(Foi muito desagradável, mas pude suporta)
    3-Gravemente(Dificilmente pude suporta)


     ''')

    while True:
        resposta = int(input("Digite um numero de 0 á 3: "))
        if 0<=resposta<4:
            break
        else:
            print("Digite de 0 a 3")

    indice_ansiedade.append(resposta)
    print('''

....................................................................

    9°)Aterrorizado (a)

    0-Absolutamente não
    1-Levemente(Não me incomodou muito)
    2-Moderadamente(Foi muito desagradável, mas pude suporta)
    3-Gravemente(Dificilmente pude suporta)


     ''')

    while True:
        resposta = int(input("Digite um numero de 0 á 3: "))
        if 0<=resposta<4:
            break
        else:
            print("Digite de 0 a 3")

    indice_ansiedade.append(resposta)
    print('''

....................................................................

    10°)Nervoso (a)

    0-Absolutamente não
    1-Levemente(Não me incomodou muito)
    2-Moderadamente(Foi muito desagradável, mas pude suporta)
    3-Gravemente(Dificilmente pude suporta)


''')

    while True:
        resposta = int(input("Digite um numero de 0 á 3: "))
        if 0<=resposta<4:
            break
        else:
            print("Digite de 0 a 3")

    indice_ansiedade.append(resposta)
    print('''

....................................................................

    11°)Sensação de sufocação


    0-Absolutamente não
    1-Levemente(Não me incomodou muito)
    2-Moderadamente(Foi muito desagradável, mas pude suporta)
    3-Gravemente(Dificilmente pude suporta)


''')

    while True:
        resposta = int(input("Digite um numero de 0 á 3: "))
        if 0<=resposta<4:
            break
        else:
            print("Digite de 0 a 3")

    indice_ansiedade.append(resposta)
    print('''

......................................................................

    12°)Tremores nas mãos


    0-Absolutamente não
    1-Levemente(Não me incomodou muito)
    2-Moderadamente(Foi muito desagradável, mas pude suporta)
    3-Gravemente(Dificilmente pude suporta)


''')

    while True:
        resposta = int(input("Digite um numero de 0 á 3: "))
        if 0<=resposta<4:
            break
        else:
            print("Digite de 0 a 3")

    indice_ansiedade.append(resposta)


    print('''

........................................................................

    13°)Trêmulo (a)



    0-Absolutamente não
    1-Levemente(Não me incomodou muito)
    2-Moderadamente(Foi muito desagradável, mas pude suporta)
    3-Gravemente(Dificilmente pude suporta)


''')

    while True:
        resposta = int(input("Digite um numero de 0 á 3: "))
        if 0<=resposta<4:
            break
        else:
            print("Digite de 0 a 3")
            
    indice_ansiedade.append(resposta)
    print('''

.......................................................................

    14°)Medo de perder o controle

    0-Absolutamente não
    1-Levemente(Não me incomodou muito)
    2-Moderadamente(Foi muito desagradável, mas pude suporta)
    3-Gravemente(Dificilmente pude suporta)


''')
    while True:
        resposta = int(input("Digite um numero de 0 á 3: "))
        if 0<=resposta<4:
            break
        else:
            print("Digite de 0 a 3")
    
    indice_ansiedade.append(resposta)
    print('''

........................................................................

    15°)Dificuldade de respirar

    0-Absolutamente não
    1-Levemente(Não me incomodou muito)
    2-Moderadamente(Foi muito desagradável, mas pude suporta)
    3-Gravemente(Dificilmente pude suporta)


''')

    while True:
        resposta = int(input("Digite um numero de 0 á 3: "))
        if 0<=resposta<4:
            break
        else:
            print("Digite de 0 a 3")

    indice_ansiedade.append(resposta)
    print('''

.........................................................................

    16°)Medo de morrer

    0-Absolutamente não
    1-Levemente(Não me incomodou muito)
    2-Moderadamente(Foi muito desagradável, mas pude suporta)
    3-Gravemente(Dificilmente pude suporta)


''')

    while True:
        resposta = int(input("Digite um numero de 0 á 3: "))
        if 0<=resposta<4:
            break
        else:
            print("Digite de 0 a 3")

    indice_ansiedade.append(resposta)
    print('''

...........................................................................

    17°)Assustado (a)


    0-Absolutamente não
    1-Levemente(Não me incomodou muito)
    2-Moderadamente(Foi muito desagradável, mas pude suporta)
    3-Gravemente(Dificilmente pude suporta)


''')

    while True:
        resposta = int(input("Digite um numero de 0 á 3: "))
        if 0<=resposta<4:
            break
        else:
            print("Digite de 0 a 3")

    indice_ansiedade.append(resposta)

    print('''

.............................................................................

    18°)Indigestão ou desconforto no abdômen

    0-Absolutamente não
    1-Levemente(Não me incomodou muito)
    2-Moderadamente(Foi muito desagradável, mas pude suporta)
    3-Gravemente(Dificilmente pude suporta)


''')

    while True:
        resposta = int(input("Digite um numero de 0 á 3: "))
        if 0<=resposta<4:
            break
        else:
            print("Digite de 0 a 3")

    indice_ansiedade.append(resposta)
    print('''

...............................................................................

    19°)Sensação de desmaio

    0-Absolutamente não
    1-Levemente(Não me incomodou muito)
    2-Moderadamente(Foi muito desagradável, mas pude suporta)
    3-Gravemente(Dificilmente pude suporta)


''')

    while True:
        resposta = int(input("Digite um numero de 0 á 3: "))
        if 0<=resposta<4:
            break
        else:
            print("Digite de 0 a 3")

    indice_ansiedade.append(resposta)
    print('''

................................................................................

    20°)Rosto afogueado (rubor facial)


    0-Absolutamente não
    1-Levemente(Não me incomodou muito)
    2-Moderadamente(Foi muito desagradável, mas pude suporta)
    3-Gravemente(Dificilmente pude suporta)


''')

    while True:
        resposta = int(input("Digite um numero de 0 á 3: "))
        if 0<=resposta<4:
            break
        else:
            print("Digite de 0 a 3")

    indice_ansiedade.append(resposta)
    print('''

..................................................................................

    21°)Suor (não devido ao calor)

    0-Absolutamente não
    1-Levemente(Não me incomodou muito)
    2-Moderadamente(Foi muito desagradável, mas pude suporta)
    3-Gravemente(Dificilmente pude suporta)


''')



    indice_ansiedade.append(resposta)
    restudo_ansiedade =sum(indice_ansiedade)

    if 0<=restudo_ansiedade<10:

        print(''' \033[1;36m"Dentro do limite mínimo (ansiedade mínima) \033[m Que ótimo que você fez o 
        inventário de ansiedade de Beck e o resultado foi bom!
        Isso significa que você está controlando sua ansiedade e não está deixando ela atrapalhar sua vida. 
        Você é uma pessoa calma e equilibrada. Mantenha esse ritmo!''')
    elif 11<=restudo_ansiedade<19:

        print('''\033[0;32m"Ansiedade leve\033[m
        Òtimo que você está dentro do limite mínimo de ansiedade! 
        Isso mostra que você tem confiança em si mesmo e não se deixa abalar 
        pelas incertezas da vida. ''')

    elif 20<=restudo_ansiedade<30:

        print('''\033[1;33mAnsiedade moderada!\033[Respire fundo e acalme esse seu doce coração. 
        Você tem muitas qualidades e potenciais que a ansiedade não pode apagar''')

    elif 31<=restudo_ansiedade<=63:

        print('''\033[1;31m Ansiedade grave!\033[m Uma palavra motivadora que eu posso te dar é: esperança. 
        Esperança de que as coisas vão melhorar, de que você vai superar os seus desafios, 
        de que você vai encontrar a sua felicidade. 
        Esperança de que você não está sozinho, de que você tem pessoas que te amam e te apoiam, 
        de que você tem um propósito na vida. 
        Esperança de que você é capaz, de que você tem valor, de que você merece ser feliz.
        Também quero te incentivar a buscar a ajuda de 
        um profissional se você sentir que a sua ansiedade está atrapalhando a sua vida. 
        Um psicólogo ou um psiquiatra pode te orientar a lidar 
        com os seus pensamentos e emoções de forma mais saudável e eficaz. 
        Não tenha medo ou vergonha de procurar ajuda. Isso é um ato de amor-próprio e de coragem. 
        Você não precisa enfrentar tudo sozinho. Você merece ser cuidado e acolhido.''')










