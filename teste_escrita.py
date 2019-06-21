arquivo = open('perfis.csv', 'a')
arquivo.write('Denis, 1198766-5432, Empresa A \n')
arquivo.write('Maria, 1198766-5123, Empresa B \n')
arquivo.write('Jose, 1198766-5456, Empresa C \n')
print arquivo.mode
arquivo.close()