"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores."""

#declarei os vetores para guardar os valores 
numbers = []
par = []
impar = []

#repetição que itera 20 vezes recebendo valores atraves da variavel number 
for c in range(20):
    number = int(input(f"insira o {c+1}° numero: "))
    
    #o vetor number puxa o valor recebido pela variavel number a cada iteração, usando o metodo append
    numbers.append(number)

    #se o numero recebido por number for par ele tbm é armazenado no vetor par
    if number % 2 == 0 :
        par.append(number)
    
    #e se for impar ele é armazenado no vetor impar 
    else:
        impar.append(number)

#saida de dados
print(f"todos : {numbers}\npares: {par}\nimpares: {impar}")

