"""Faça um Programa que peça as quatro notas de 10 alunos, calculee armazene num vetor
   a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0."""

#criei um vetor para guardar as medias
medias=[]

#esse laço vai iterar 10 vezes representando 10 alunos
for c in range (10):
   
    #essas variaveis são necessarias para zerar os valores que irão receber posteriormente a cada iteração
    notas=0
    media=0
    #e esse vai iterar 4 vezes onde serão recebidas as 4 notas 
    for b in range (4):
        nota=float(input(f"informe a {b+1}° nota: "))
        notas+=nota
        media=notas/4
        
        #se a variavel media armazenar um valor maio ou igual a 7 esse valor e
        #armazenado no vetor medias atraves o metodo append
        if media >= 7:
            medias.append(media)

#ira exibir o tamanho do vetor, e como todos os valores q estão armazenados
#são medias maiores ou igual a 7 o seu tamanho representa a quantidade de alunos com media 7 ou superior
print(f"o numero de alunos com media maior ou igual a 7 são: {len(medias)}")
