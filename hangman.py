import random
import os

def limpar_tela():  
  os.system('cls' if os.name == 'nt' else 'clear')

possiveis_palavras_animais = ['leão', 'tigre', 'elefante']
possiveis_palavras_comidas = ['pizza', 'hambúrguer', 'sushi']
possiveis_palavras_quaisquer = ['computador', 'python', 'openai']

def display_hangman(tries):
  stages = [
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """
  ]
  return stages[tries]

def forca(palavra_decidida):
  tentativas = 0
  palavra_formada = '_' * len(palavra_decidida)
  letras_usadas = []
  
  while palavra_formada != palavra_decidida and tentativas < 6:
    limpar_tela()
    print(display_hangman(tentativas))
    print(f'Palavra: {palavra_formada}')
    print(f'Letras usadas: {", ".join(letras_usadas)}')
    letra = input('Digite uma letra: ').lower()

    if letra in letras_usadas:
      print('Você já usou essa letra. Tente outra.')
      continue

    letras_usadas.append(letra)

    if letra in palavra_decidida:
      palavra_formada = ''.join([letra if letra == palavra_decidida[i] else palavra_formada[i] for i in range(len(palavra_decidida))])
    else:
      tentativas += 1
      print(f'Letra errada. Você tem {6 - tentativas} tentativas restantes.')

  limpar_tela()
  if palavra_formada == palavra_decidida:
    print(display_hangman(tentativas))
    print(f'Parabéns! Você adivinhou a palavra: {palavra_decidida}')
  else:
    print(display_hangman(tentativas))
    print(f'Você perdeu. A palavra era: {palavra_decidida}')

def main():
  print('Olá, bem-vindo ao jogo da forca. Escolha uma das seguintes opções')
  tipo_palavra_escolhida = ['1- Animais', '2- Comidas', '3- Qualquer', '4- Mix', '5- Escolher']
  for x in tipo_palavra_escolhida:
    print(x)

  try:
    escolha = int(input('#'))

    if escolha == 1:
      print('Você escolheu jogar com animais, vamos começar')
      palavra_decidida = random.choice(possiveis_palavras_animais)
      forca(palavra_decidida)

    elif escolha == 2:
      print('Você escolheu jogar com comidas, vamos começar')
      palavra_decidida = random.choice(possiveis_palavras_comidas)
      forca(palavra_decidida)

    elif escolha == 3:
      print('Você escolheu jogar com qualquer palavra, vamos começar')
      palavra_decidida = random.choice(possiveis_palavras_quaisquer)
      forca(palavra_decidida)

    elif escolha == 4:
      print('Você escolheu jogar com todas, vamos começar')
      palavra_decidida = random.choice(possiveis_palavras_animais + possiveis_palavras_comidas + possiveis_palavras_quaisquer)
      forca(palavra_decidida)

    elif escolha == 5:
      print('Você deseja escolher a palavra, vamos começar')
      palavra_decidida = input('Digite a palavra: ')
      forca(palavra_decidida)

    else:
      print('Opção inválida. Tente novamente.')

  except ValueError:
    print('Opção inválida. Tente novamente.')
