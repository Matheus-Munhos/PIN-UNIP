while True:  # Loop PRINCIPAL 
    print('Olá, digite seu nome:')
    nome = input('>> ')
    
    print(' Seja bem vindo, ' + nome + ' qual a sua idade ? ')
    idade = input('>> ')
    print('Obrigado! Vamos continuar...')

    while True:  # Loop consentimento dos dados
        resposta = input('Aceita compartilhar dados? [1] Sim [2] Não: ')
        
        if resposta == "1":
            print('Ótimo! Prosseguindo...')
            break  # continua o programa
        elif resposta == "2":
            print('Reiniciando processo...')
            break  # sai do loop de dados e volta ao início (nome)
        else:
            print('ERRO: Digite apenas 1 ou 2!')
    if resposta == "2":
        continue  # volta para o início (nome)

    print('Agora vamos aprender um pouco sobre tecnologia da informação')
    print('A Tecnologia da Informação (TI) é o conjunto de recursos, ferramentas e sistemas utilizados para armazenar, processar, transmitir e gerenciar dados e informações. Ela abrange hardware (computadores, servidores, dispositivos), software (programas, aplicativos), redes (internet, intranet) e bancos de dados, além de práticas como segurança digital e suporte técnico.')

    while True:  # Loop etapa 3
        prosseguir = input('Para prosseguirmos, digite 0101: ')
        if prosseguir == '0101':
            print('Prosseguindo...')
            break
        else:
            print('ERRO: Digite : 0101')

    while True:  # Etapa 4 + etapa 5 dentro
        print('Já ouviu falar Sobre Pseudocódigo e Fluxograma ?')

        while True:  # Loop etapa 4
            etapa4 = input('Para conhecer mais, por gentileza escolha entre : 1 - Pseudocódigo e 2 - Fluxograma: ')

            if etapa4 == '1':
                print('O pseudocódigo é uma técnica que permite representar a lógica de um algoritmo de forma simples, utilizando uma linguagem próxima ao português estruturado. Ele não segue regras rígidas de sintaxe, mas mantém uma organização clara para facilitar o entendimento e a posterior tradução para uma linguagem de programação real. Sua principal vantagem é a capacidade de descrever processos complexos de maneira intuitiva, sem preocupações com detalhes técnicos de código.')
            elif etapa4 == '2':
                print('Fluxograma é uma representação visual de algoritmos ou processos, utilizando símbolos gráficos padronizados. Cada forma geométrica tem um significado específico: retângulos indicam ações, losangos representam decisões e setas definem o fluxo de execução. Essa ferramenta é especialmente útil para visualizar a sequência lógica de um sistema, permitindo identificar possíveis falhas ou otimizações antes da implementação prática.')
            else:
                print('ERRO : Digite 1 ou 2')
                continue

            while True:
                sair = input('Digite [1] para prosseguir ou [0] para voltar ao menu anterior: ')
                if sair == '1':
                    print('Prosseguindo...')
                    break  # vai para etapa 5
                elif sair == '0':
                    print('Retornando...')
                    break  # volta ao menu etapa 4
                else:
                    print('Digite [1] para prosseguir ou [0] para voltar ao menu anterior: ')

            if sair == '1':
                break  # sai do etapa4 e vai para etapa5

        while True:  # Etapa 5
            etapa5 = input('Para encerrar o sistema digite [1] ou [0] para continuar no sistema: ')
            if etapa5 == '0':
                print('Retornando...')
                break  # volta para etapa 4
            elif etapa5 == '1':
                print('Encerrando...')
                break  # sai da etapa 5 e volta ao início do programa
            else:
                print('ERRO: Digite apenas 0 ou 1')

        if etapa5 == '1':
            break  # volta ao início (nome)