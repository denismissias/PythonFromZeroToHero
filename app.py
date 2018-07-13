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

def menu():
    nomes = []
    escolha = ''

    while(escolha != '0'):
        print "Digite 1 para cadastrar, 2 para listar, 3 para remover e 0 para terminar"
        escolha = raw_input()

        if(escolha == '1'):
            cadastrar(nomes)

        if(escolha == '2'):
            listar(nomes)

        if(escolha == '3'):
            remover(nomes)

menu()