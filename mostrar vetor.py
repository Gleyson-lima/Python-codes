#criei o vetor para guardar os numeros
numeros = []

#laço itera 5 vezes recebendo valores pela variavel numero
for c in range(5):
    numero=int(input(f"insira o {c+1}º valor: "))
    #o vetor numeros puxa o valor da variavel numero atraves do metodo append
    numeros.append(numero)

#exibe o vetor numeros
print(numeros)
