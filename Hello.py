import random

# O computador "pensa" em um número secreto entre 1 e 20.
numero_secreto = random.randint(1, 20)

# Deixamos uma variável para contar quantas tentativas você fez.
tentativas = 0

# Dizemos ao jogador o que fazer.
print("Olá! Estou pensando em um número entre 1 e 20.")
print("Tente adivinhar qual é.")

# Criamos um "loop" para que você possa tentar várias vezes.
while tentativas < 6:
    # Pedimos para você chutar um número.
    seu_chute = int(input("Digite o seu palpite: "))

    # Aumentamos o contador de tentativas.
    tentativas = tentativas + 1

    # Damos as dicas!
    if seu_chute < numero_secreto:
        print("Seu chute é muito baixo.")
    elif seu_chute > numero_secreto:
        print("Seu chute é muito alto.")
    else:
        # Se você acertou, o jogo acaba!
        break  # O comando `break` serve para sair do loop.

# Agora, o jogo acabou. Vamos dizer se você ganhou ou perdeu.
if seu_chute == numero_secreto:
    print(f"Parabéns! Você acertou em {tentativas} tentativas!")
else:
    print(f"Que pena! O número que eu estava pensando era {numero_secreto}.")

