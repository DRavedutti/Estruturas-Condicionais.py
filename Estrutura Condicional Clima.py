print("Qual Melhor Atividade Fisica Posso Fazer")
clima_atual = input("Informa como está o clima hoje: ")
qnt_de_graus = float(input("Informe o °C: "))
nivel_de_energia = input("Informe o Nivel de Energia: ")


if qnt_de_graus >= 24.0:
  print("Correr 5Km no Parque")
elif qnt_de_graus >= 20.0:
  print("Faça Atvidade na Esteira da Academia")
elif qnt_de_graus >= 15.0:
  print("O Clima não está bom. Assista um filme")
else:
  print("Clima Turbulento. Se Abrigue - TORNADO")
