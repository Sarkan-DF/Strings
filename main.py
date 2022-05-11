from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "http://bytebank.com/cambio?Moedaorigem=moedadestino&moedadeStino=dolar&valor=1500"

argumentosUrl1 = ExtratorArgumentosUrl(url)
argumentosUrl2 = ExtratorArgumentosUrl(url)
# moedaOrigem, moedaDestino = argumentosUrl.extraiArgumento()
# valor = argumentosUrl.extraiValor()
# print(moedaOrigem, moedaDestino, valor,"\n")
#
# print("Tamanho url:",len(argumentosUrl),"\n")
#
# print(argumentosUrl)
print(id(argumentosUrl1))
print(id(argumentosUrl2))
print(argumentosUrl1 == argumentosUrl2)