#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

#Criei um vetor
notas=[]

#receber as notas, atraves do .append o vetor notas puxa cada valor digitado pra si
for c in range (4):
    nota=float(input(f"informe a {c+1}º nota: "))
    notas.append(nota)

#sum(notas) soma todos os valores do vetor #len(notas) tamanho do vetor
#media é igual a soma dos valores do vetor dividida pelo numeros de elementos armazenados nelee
media=sum(notas)/len(notas)

print(f"sua media final foi: {media}")