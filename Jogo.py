import random

while True:

    print("""

As regas do jogo são as seguintes:
          digite 1 para ganhar 1 ponto.
          Digite 2 para não ganhar um ponto.

          A escolha da maquina é aleatoria.1


    """)

    rodada = 0
    pj  = 0
    pm = 0

    while rodada < 5:

     rodada += 1

     escolha = int(input("O jogador quer um ponto? \n"))

     if escolha == 1:
       print("O jogador desejou ganhar um ponto \n")
       pj += 1
       print(f"Placar do jogo: Jogador {pj} X Maquina {pm} \n")

    
     else:
        print("O jogador não quis ganhar um ponto \n")

     escolhaM = random.randint(1,2)

     if escolhaM == 1:
       print("A maquina desejou ganhar um ponto \n")
       pm += 1
       print(f"Placar do jogo: Jogador {pj} X Maquina {pm} \n")

     else: 
       print("A maquina não deseja ganhar um ponto \n")
       print(f"Placar do jogo: Jogador {pj} X Maquina {pm} \n")
    
    if rodada == 5:
      print("Fim de jogo.")
      if pj == 5:
        print("---Vencedor: Jogador -----")

      elif pm == 5:
        print("---Vencedor: Maquina -----")



    continuar = input("Deseja continuar a jogar (S/N)").upper()
    if continuar == "S":
      print("Reiniciando o jogo")
      continue

    else:
      print("Saindo")
      break

        