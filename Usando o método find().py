# Vimos nessa aula que o método find ajuda a capturar valores
# de uma forma mais dinâmica dentro de uma string qualquer.
# Analise o código abaixo:

# Com o objetivo de retirar o código de área sem os “()”,
# os valores de x e y podem ser substituídos por:

celular = "(41)96574-1728"
indiceInicialCodigoArea = celular.find('(')+1
indiceFinalCodigoArea   = celular.find(')')

print (celular[indiceInicialCodigoArea:indiceFinalCodigoArea])