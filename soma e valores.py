#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números
#criei o vetor para armazenar os numeros
numbers =[]

#estrutura de repetição para povoar o vetor com 5 valores
for c in range (5):
    number=int(input(f"informe o {c+1}° valor: "))
    numbers.append(number)

#variavel criada para armazenar a multiplicação, iniciada com 1 pois qualquer numero
#multiplicado por 1 retorna ele mesmo 
multiplicacao=1

#laço que itera uma vez para cada elemento armazenado no vetor
#toda vez que o laço itera o "elemento" assume o valor do indice do vetor ao qual esta iterando
for elemento in numbers:
    multiplicacao*=elemento

#saida
print(f"a multiplicação: {multiplicacao}\na soma: {sum(numbers)}\nnumeros {numbers}")

