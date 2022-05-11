import re
email1 = "Meu numero é 11111-1111"
email2 = "Fale comigo em 22222222 e 4444-5555"
email3 = "3333-33332 é o meu celular"

padrao = "[0-9]{4,5}-?[0-9]{4}"

retorno = re.findall(padrao, email2)
print(retorno)