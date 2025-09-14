# -------- Avaliador de Notas ---------
# Docstring..

"""
Este Programa Demonstra Estruturas Conidicionais em Python
"""
print(" ------- Avaliador de Notas --------")
print("Descubra sua Situação com Base sua Nota Maximo no exame: \n")
nota_do_aluno_str = input("Por Favor, digite sua nota: (0 - 10) ")
aulas_assistidas = float(input("Quantas Aulas Assistiu em todo Semestre: "))
aulas_totais = 20
frequencia = aulas_assistidas / aulas_totais
nota_aluno = float(nota_do_aluno_str)
print(f"Sua nota é: {nota_aluno}")
print("")

if nota_aluno >= 9.0:
  if frequencia >= 0.75:
    print("Parabéns! Aprovado com Louvor")
    print("Excelente!")
  else:
    print("Sua Nota Foi boa, mas sua frequencia nao")
elif nota_aluno >= 7.0:
  print("Aprovado!")
  print("Bom Trabalho")
elif nota_aluno >= 5.0:
  print("Em recuperação")
  print("Precisa Estudar um Pouco Mais")
else:
  print("Reprovado")
  print("Revise o Conteudo")


print("\nObrigado por Utilizar o Programa")

