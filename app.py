# -*- coding: UTF-8 -*-

def listar(nomes):
    print "Listando nomes: "
    for nome in nomes:
        print nome

def cadastrar(nomes):
    print "Digite um nome:"
    nome = raw_input()
    nomes.append(nome)

def remover(nomes):
    print 'Qual nome você gostaria de remover?'
    nomes.remove(raw_input())

def alterar(nomes):
    print 'Qual nome vc gostaria de alterar?'
    nome_a_ser_alterado = raw_input()

    if nome_a_ser_alterado in nomes:
        print "Qual é o novo nome?"
        index = nomes.index(nome_a_ser_alterado)
        nomes[index] = raw_input()
    else:
        print nome_a_ser_alterado + " não existe na lista."

def procurar_regex(nomes):
    import re
    print('Digite a expressão regular')
    nomes_concatenados = ' '.join(nomes)
    resultados = re.findall(raw_input(), nomes_concatenados)
    print(resultados)

def procurar(nomes):
    print 'Digite nome a procurar:'
    nome_a_procurar = raw_input()

    if nome_a_procurar in nomes:
        print nome_a_procurar + " existe na lista."
    else:
        print nome_a_procurar + " NÃO existe na lista."

def menu():
    nomes = []
    escolha = ''

    while(escolha != '0'):
        print "Digite 1 para cadastrar, 2 para listar, 3 para remover, 4 para alterar, 5 para pesquisar, 6 busca por REGEX e 0 para terminar"
        escolha = raw_input()

        if(escolha == '1'):
            cadastrar(nomes)

        if(escolha == '2'):
            listar(nomes)

        if(escolha == '3'):
            remover(nomes)

        if(escolha == '4'):
            alterar(nomes)

        if(escolha == '5'):
            procurar(nomes)

        if(escolha == '6'):
            procurar_regex(nomes)

menu()