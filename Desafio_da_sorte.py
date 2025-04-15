import random
sorte = random.randint(1,2)
rodada = 0
placarM = 0
placarJ = 0
chance = 0


print("""

Bem vindo ao jogo da sorte.
      A regra é a seguinte:
      1° Você e a maquina não podem escolher o mesmo número caso aconteça, a maquina terá 50% de chance de ganhar na hora a partida
      2° Você deve escolher entre 1 e 5.
      3° Para marcar ponto o seu número deverá ser maior que o da Maquina
      """)


while placarJ < 5 or placarM < 5:

 escolhaJ = int(input("Escolha um número "))

 escolhaM = random.randint(1,5)

#  print(f"O número da sorte é: {sorte}")

 print(f"O jogador escolheu o seguinte número {escolhaJ} \n")
 print(f"O jogador escolheu o seguinte número {escolhaM} \n ")

# Jogador Ganhou
 if escolhaJ > escolhaM:
  print("Jogador marcou um ponto")
  placarJ += 1
  print(f"Placar: JxM {placarJ} x {placarM}")

#   Números iguais
 elif escolhaJ == escolhaM:
  print("Vocês escolheram os mesmos números")

  if sorte == 2:
   print("Fim de jogo, a Maquina ganhou.")
   break
  else: 
   print("Segue o jogo")
# Maquina ganhou
 else:
  print("Maquina marcou um ponto")
  placarM += 1
  print(f"Placar: JxM {placarJ} x {placarM}")

# Vencedores
  if placarJ >= 5:
   print(f"Vencedor: Jogador ganhou por {placarJ} X {placarM} ")

  elif placarM >= 5:
   print(f"Vencedor: Maquina ganhou por {placarJ} X {placarM} ")
# Continuar?
   continuar = input("Deseja continuar? (S/N)").upper()
   
   if continuar == "S":
    print("Continuando...")

   else:
    print("Saindo")
    break
