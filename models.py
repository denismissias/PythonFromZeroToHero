# -*- coding: UTF-8 -*-

class Perfil(object):
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def imprimir(self):
        print "Nome: %s, Telefone: %s, Empresa: %s" % (self.nome, self.telefone, self.empresa)

    def curtir(self):
        self.__curtidas+=1

    def obter_curtidas(self):
        return self.__curtidas

    @classmethod
    def gerar_perfis(classe, nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        perfis = []
        for linha in arquivo:
            valores = linha.split(',')
            perfis.append(classe(*valores))
        arquivo.close()
        return perfis

class Perfil_Vip(Perfil):
    'Classe padrão para perfis de usuários vip'

    def __init__(self, nome, telefone, empresa, apelido = ''):
        super(Perfil_Vip, self).__init__(nome, telefone, empresa)
        self.apelido = apelido

    def obter_creditos(self):
        return super(Perfil_Vip, self).obter_curtidas() * 10.0

class Data(object):
    "Classe usada para formatar uma data"

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprime(self):
        print "%d/%d/%d" % (self.dia, self.mes, self.ano)

class Pessoa(object):
    "Classe usasda para calcular o IMC de uma pessoa"

    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def imprime(self):
        imc = float(self.peso) / (float(self.altura) * float(self.altura))
        print "Imc de %s: %f" % (self.nome, imc)
        