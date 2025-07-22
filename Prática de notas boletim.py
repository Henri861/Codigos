#Prática de notas boletim


nota = int(input('Qual é a nota do aluno?'))

if nota >= 9:
    print("Ótimo! O aluno foi aprovado com excelencia!")
elif nota >= 7:
    print('Você foi muito bom!')
elif nota >= 5:
    print('Você passou, mas precisa mehorar')
else:
    print('Você foi reprovado!')