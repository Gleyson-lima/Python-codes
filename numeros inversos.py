#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

#criei um vetor
numeros=[]

#laço itera 10 vezes, a cada iteração o vetor puxa o valor de "num" para si
for c in range (10):
    num=int(input(f"infome o {c+1}º numero: "))
    numeros.append(num)

#a estrutura abaixo imprimira os indices do vetor em ordem decrescente
print("os numeros em ordem decrescente ficam assim:")
for c in range (9,-1,-1):
    print(numeros[c]," ",end='') #o end faz com que tudo seja impresso na msm linha
